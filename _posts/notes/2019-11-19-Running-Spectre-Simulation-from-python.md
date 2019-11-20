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

That is great! But I also needed to access the OCEAN functions from python too. OCEAN functions are not structured with prefixes like schematic/layout functions for example `run()`,`simulator()` etc. so they are not accessible. 

## Workaround
Fortunately skillbridge allows for user function registration. One can register user defined SKILL functions. So I can use that functionality to register only those OCEAN functions that I need like this.
```
from skillbridge import Workspace
from skillbridge.client.functions import Function

ws = Workspace.open()
ws.user += Function("run", "documentation string of some kind", set())

ws.user.run(...)
```
