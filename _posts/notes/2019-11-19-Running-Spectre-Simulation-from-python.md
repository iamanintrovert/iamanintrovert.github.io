---
title: Running Spectre Simulation from Python
categories:
  - notes
tags:
  - research
  - CAD
---

Running Virtuoso Spectre simulation using OCEAN scripts can be very powerful way to get much out of the simulator. But OCEAN scripts are written in SKILL syntax which in my opinion is not very user friendly and modern. It would be much nicer if those scripts could be written in syntax like python. Although that luxury is not provied, we can use python scripts to communicate to Cadence Virtuoso through inter process communication and access SKILL/OCEAN functions and have those data manipulate in the usual way we manipulate data in python. A python toolbox [skillbridge](https://github.com/unihd-cag/skillbridge) does exactly that.

## skillbridge structure
skillbridge sets up a python server from Virtuoso which takes instructions from python script, sends it to Virtuoso SKILL console and returns restuls back to python script. It allows calling SKILL schematic/layout functions from python. Python equivalent of SKILL functions are structured by their prefix. For example SKILL function `geGetEditCellView()` has prefix `ge` and all the functions begining with `ge` prefix will be grouped under `ge` in python. So from python that function would be `ge.get_edit_cell_view()` as explained in the [documentation](https://unihd-cag.github.io/skillbridge/examples/basic.html). 

That is great! But I also needed to access the OCEAN functions from python too. OCEAN functions are not structured with prefixes like schematic/layout functions for example `run()`,`simulator()`, `modelFile()` etc. so they are not accessible. 

## Workaround
The following function registration method is no longer valid after `skillbridge-1.0.4`. Any SKILL function can now be called directly using `ws['skillFunc'](...)` like statement.
{: .notice--danger}

Fortunately skillbridge allows for user function registration. One can register user defined SKILL functions. So I can use that functionality to register only those OCEAN functions that I need like this.
```python
from skillbridge import Workspace
from skillbridge.client.functions import Function

ws = Workspace.open()
ws.user += Function("modelFile", "documentation string of some kind", set())

ws.user.model_file(...)
```
## Workflow
I use python in anaconda environtment.
* from a shell activate the environment where skillbridge is installed.
* from that same shell start Virtuoso so that Virtuoso sees the same python envornment skillbridge is in. Make sure that License checkout is not set to prompt. From `Options->License->Ordering` set all to `always`. Otherwise everytime simulation is run, that annoying popup winodw appears to chose license and obstructs simulation.
* Start python server from Virtuoso by `pyStartServer ?timeout nil`. Timeout value of `nil` sets the server to run forever unless it is killed mannually.
* start spyder and write simulation code as one would write in OCEAN.

## Tips
* if simulation is stopped midway (CTRL+C) in python then restart the python kernel. Otherwise simulation stops working.
* function arguments are strings with comma seperation.
* some OCEAN function requires arguments like `'spectre`, `'dcOp` with apostrophe in the front. Those has to be supplied as `skillbridge.client.translator.Symbol` class like `Symbol('dcOp')`.
* `t` also has to be `Symbol('t')` type.
* looks like skillbridge cannot process datatype returned by `select_result()`. But the function evalues fine. Since the returned data is not needed anyway, `select_result()` is placed in a `try` block so that python script does not run into error.
* if you have your own skillfunctions registered make sure that those files are loaded in Virtuoso using `load()` before using those functions.
* for easier OCEAN script to python script conversion, do a simulation in ADE and `session->save ocean` and from that OCEAN script start converting functions to python.

## Example code
`utils.py`
```python
from skillbridge import Workspace
from skillbridge.client.functions import Function

# any values in ocean containing apostrophe like 'tran use Symbol('tran') in python
# use Symbol('tran') to set 'tran ; client.translator import Symbol

def define_ocean_functions(ws):
    ws.user += Function('simulator', 'ocean simulator()', set())
    ws.user += Function('design', 'ocean design()', set())
    ws.user += Function('resultsDir', 'ocean design()', set())
    ws.user += Function('modelFile', 'ocean design()', set())
    ws.user += Function('analysis', 'ocean analysis()', set()) 
    ws.user += Function('desVar', 'ocean desVar()', set())
    ws.user += Function('envOption', 'ocean envOption()', set())
    ws.user += Function('save', 'ocean save()', set())
    ws.user += Function('converge', 'ocean converge()', set())
    ws.user += Function('temp', 'ocean temp()', set())
    ws.user += Function('run', 'ocean run()', set())
    ws.user += Function('selectResult', 'ocean selectResult()', set())
    
    
model_files = [
    ["/path/to/models/Spectre/design.scs", ""],
    ["/path/to/models/Spectre/allModels.scs", "tt"],
    ["/path/to/models/Spectre/wafer.scs", ""]
    ]
```
`main_file.py`
```python
from skillbridge import Workspace
from skillbridge.client.translator import Symbol
import numpy as np
import matplotlib.pyplot as plt
import utils

def waveform_to_vector(waveforms):
    vectors =[]
    global ws
    for wave in waveforms:
        y_wave = ws.dr.get_waveform_y_vec(wave)
        y_vec = []
        for i in range(ws.dr.vector_length(y_wave)):
            y_vec.append(ws.dr.get_elem(y_wave, i))
        vectors.append(y_vec)
        
    # x vector is same for all these y vector
    x_wave = ws.dr.get_waveform_x_vec(wave)
    x_vec = []
    for i in range(ws.dr.vector_length(x_wave)):
        x_vec.append(ws.dr.get_elem(x_wave, i))
        
    return vectors, x_vec

##########
vdd = 1
INa = 10e-9
vth = 350e-3
v_syn_p = 854e-3
v_syn_n = 100e-3
vwidth = 750e-3
vrfc = 80e-3
cap = 50e-15
###initial cond#####
v = 0
u = 0
##################

# connect to server
ws = Workspace.open()
# register required ocean functions
utils.define_ocean_functions(ws)

# set simulator
ws.user.simulator(Symbol('spectre'))
# set schematic
ws.user.design('/tmp/simulation/for_brian_sim_neuron_tran/spectre/schematic/netlist/netlist')
# set model files
ws.user.model_file(utils.model_files[0],utils.model_files[1],utils.model_files[2])
# transient analysis
stop_time = '10m'
ws.user.analysis(Symbol('tran'),'?stop',stop_time)
# set design variables
ws.user.des_var(	  "cap", cap	)
ws.user.des_var(	  "v_syn_n", v_syn_n	)
ws.user.des_var(	  "v_syn_p", v_syn_p	)
ws.user.des_var(	  "vrfc", vrfc	)
ws.user.des_var(	  "INa", INa	)
ws.user.des_var(	  "vdd", vdd	)
ws.user.des_var(	  "vth", vth	)
ws.user.des_var(	  "vwidth", vwidth	)
# analysis order in case of multiple analysis
ws.user.env_option(Symbol('analysisOrder'), ['tran'])
# to be saved currents
ws.user.save( Symbol('i'), "/syn_p/D", "/syn_n/D", "/pos_feed/D", "/neg_feed/D", "/width_p/D", "/refrac_n/D" )
# set initial conditions
ws.user.converge( Symbol('ic'), "/v", '%f'%(v))
ws.user.converge( Symbol('ic'), "/u", '%f'%(u))
# set temp and run
ws.user.temp(27)
ws.user.run()
try: # skillbridge cannot parse stdobj@0xhexnumber type data. But I don't need any parsing of that data so keeping it in try to prevent error
    ws.user.select_result(Symbol('tran')) 
except:
    print('stdobj0x type data encountered! nothing to panic about.')
# extract waveforms
waveforms = [ws.get.data('/v'), ws.get.data('/u')]

# plot
vec, time = waveform_to_vector(waveforms)
plt.plot(time, vec[0])
plt.plot(time, vec[1])
plt.show()
```

