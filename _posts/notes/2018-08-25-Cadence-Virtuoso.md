---
title: Cadence Virtuoso
categories:
  - notes
tags:
  - research
  - CAD
toc: true
---

Although school IT dept would generally provide the starting script for cadence virtuoso, I have devised my own way of making the startscript
to start virtuoso in a specific state that is conducive to my productivity. This can be done by using .cdsenv and .cdsinit files. Some variables
used in .cdsinit are defined in the startscipt for flexibility. Using the startscript we can decide which tools we want to be integrated with
virtuoso environment.

The basic idea of starting any application in linux is to run the application command (in a terminal). For the system/terminal to know the existance
of the command, its path has to be specified in the `$PATH` environment variable which says the system/terminal where to look for the commands.
Let us first decide which applications we want to run.

### Selecting the applications
 1. `virtuoso` from IC suit.
 2. `spectre` simulator from MMSIM/SPECTRE suit for doing analog simulation.
 3. `ncsim` simulator from IUS/INCISIV suit for mixed signal simulation.
 4. `pvs` verification tools from PVS suit. pvs can be replaced by assura/calibre depending on the pdk specification.
 5. application from EXT suit for parasitic extraction. Don't know which specific program.
 6. also define variables for .cdsinit/.cdslib like `CDS_HOME`,`AMS_HOME` etc. Export paths.
 7. set the licese.
 
    ```
    #!/bin/bash

    ################################################################################
    # 1. Define the path to the IC installation
    ################################################################################
    IC_HOME="/path/to/IC/directory"
    IC_PATH="${IC_HOME}/bin:${IC_HOME}/tools/bin:${IC_HOME}/tools/dfII/bin"
    ################################################################################
    # cds.lib path name helper
    # both are same. use whichever name is in cds.lib
    CDS="${IC_HOME}"
    CDS_HOME="${IC_HOME}" # used in cds.lib to include analogLib, ahdLib etc

    ################################################################################
    # 2. Define the path to the installation MMSIM (SPECTRE)
    ################################################################################
    MMSIM_HOME="/path/to/SPECTRE/directory"
    MMSIM_PATH="${MMSIM_HOME}/bin:${MMSIM_HOME}/tools/bin:${MMSIM_HOME}/tools/inca/bin"

    ################################################################################
    # 3. Define the path to the installation IUS (INCISIV)
    ################################################################################
    IUS_HOME="/path/to/IUS/directory"
    IUS_PATH="${IUS_HOME}/bin:${IUS_HOME}/tools/bin:${IUS_HOME}/tools/inca/bin"
    ################################################################################
    # additional cds.lib path name helper
    AMS_HOME="${IUS_HOME}" # used in cds.lib to include mixed signal libs

    ################################################################################
    # 4. Define the path to the PVS installation
    ################################################################################
    PVS_HOME="/path/to/PVS/directory"
    PVS_PATH="${PVSHOME}/tools/bin:${PVSHOME}/bin"
    ################################################################################
    # PVS color
    PV_COLOR_DIR="${PVSHOME}/tools/pvs/samples/color_setup"

    ################################################################################
    # 5. Define the path to the QRC installation
    ################################################################################
    QRC_HOME="/path/to/QRC/directory"
    QRC_PATH="${PATH}:${QRC_HOME}/tools/bin:${QRC_HOME}/bin"

    ################################################################################
    # 6. export cds.lib, .cdsinit and path variables
    ################################################################################
    export CDS_HOME
    export AMS_HOME
    export PVS_HOME
    export QRC_HOME
    export PV_COLOR_DIR
    export export PATH="${IC_PATH}:${MMSIM_PATH}:${IUS_PATH}:${PVS_PATH}:${QRC_PATH}:${PATH}"

    ################################################################################
    # 7. specify license
    ################################################################################
    export LM_LICENSE_FILE="license-file" # contact IT for this
    export CDS_LIC_FILE=${LM_LICENSE_FILE}
    ```

 8. set pdk paths.
 
    ```
    ################################################################################
    # 8. PDK specific settings here
    ################################################################################
    export PDKHOME="/path/to/pdk"
    export PVSTECHDIR="/path/to/pvs/techdir"
    ```

 9. create the directory where design files will be kept. create a directory `log` also inside. We will send the logs     to this dir 
    so that logs doesn't clutter up home dir.
 
    ```
    ################################################################################
    # 9. set work directory
    ################################################################################
    export WORK_DIR="/path/to/work/dir"
    cd ${WORK_DIR}
    # set log path so it doesn't clutter up work area
    export CDS_LOG_PATH="${WORK_DIR}/log"
    ```
 10. set some initialization.
 
     ```
     ################################################################################
     # 10. set some env vars
     ################################################################################
     #export CDS_LOAD_ENV="CWD" # load .cdsenv only from current working dir
     export SPECTRE_DEFAULTs="-E"
     export CDS_Netlisting_Mode="Analog"
     ```

 11. start `virtuoso`
 
     ```
     ################################################################################
     # 11. start virtuoso; CDS_AUTO_64BIT can also be set to start in 64 bit mode
     ################################################################################
     exec virtuoso -64 &
     ```

See `${IC_HOME}/doc/dfIIconfig/dfIIconfig.pdf` for available env vars of cadence.

-----------------------------

## Some tips and tips and tricks
### changing BEOL stack
 CIW -> Tools -> Technology Fille Manager -> Load -> Navigate to tech file, check all classes, set the library, check merge -> ok.
 see page 231 of doc BiCMOS_8HP8XP_Training.doc. new libs with complied ASCII tech also works.

 This updates the tech.db file in the PDK. Every time PDK is loads, it uses this file to set the beol stack. You need to have write
 access to tech.db file to make this change permanent. Otherwise you would need to load techfiles everytime virtuoso starts.

### IBM PDK menu in CIW
 done by adding skill commands in .cdsinit file

### Environment variables with name ****HOME
 I think it doesn't matter what is the name of these variables. They are usally set to the path of where it is located. The only
 path varable that must not chage is PATH and LD_LIBRARY_PATH. They point to the bin and libs respectively

### CDSHOME, AMSHOME, PDKHOME
 CDSHOME is path to the cadence IC folder (like IC617). Setting this path to a recognizable name like helps path management easier
 in cds.lib file. It doesn't have to be stricly CDSHOME though.

 AMSHOME is path to the cadence IUS folder.

 PDKHOME is IBMPDK folder.

### starting a cadence program
 All we need to do is load the necessary paths in the PATH variable in a shell and type the program name (like virtuoso) in the
 same shell. Starting scipts does this job in a managable manner. It is important to add the -64 cmdline option with virtuoso for
 64 bit operation i.e. start program like this
 $ virtuoso -64

 I have split up path management of different modules in different files (ic.sh, mmsim.sh etc) and loaded them in startcad script.
 That way when you don't have to run virtuoso but other programs like SimVision you just have to load incisiv.sh.

### popping library manager open at startup
 `ddsOpenLibManager()` in .cdsinit

### setting work area, log file path
 1. work area is set to where the ./startscript is issued from. If the startscript is at some place but the ./startscript is issued from
    home, then work area is home folder. Using cd to desired work directory in the stratscript gets the work directory to desired place.
    When the script runs the cd command changes the directory and the commands in the scirpt runs wrt to that directory.
 2. log files are created in home folder. But it can be directed to some other place by CDS_LOG_PATH environment variable.
 3. make a log folder in the working directory and set the CDS_LOG_PATH to it. cadence does not create the folder itself


### issues faced
 1. without -64 cmdline option spectre simulation doesn't work
 2. irun has to be run with -64 cmdline option as well
 3. without "${IC_HOME}/tools/dfII/bin" in the path ams sim from adexl fails. But sim from adel works fine.
 4. without a display.drf schematics and layouts opening may show warning about diplay packet information missing. Fix that by
    Tools->Display Resource Manager->Merge, set the order by clicking the .drf files, set a destination file, hit ok. When exiting
    virtuoso, it will ask to save the display file. Save it as display.drf.
 5. for some reason I needed to include the inca/bin path. I don't remember why. (probably for verilog/ams)

### setting stopLevel in .cdsenv
this decides how many layers are shown in layout. 32 shows all the layers.
```
layout		stopLevel 	int	32
```

### some settings using skill in .cdsinit
 from [^1]
 1. set default simulation dir
 ```
 envSetVal("asimenv.startup" "projectDir" 'string strcat("/scratch/" getShellEnvVar("USER")))
 ```
 2. set ADEL model files [^2] [^3]
 ```
 envSetVal("spectre.envOpts" "modelFiles" 'string "path1.scs;section1 path2.scs;section2")
 ```
 asiSetEnvOptionVal( asiGetTool('spectre) 'modelFiles '(("/model_file_path" "")) )  <- not sure
 
-----------------------------

 [^1]: https://secure.engr.oregonstate.edu/wiki/ams/index.php/Cadence/TipsAndTricks
 [^2]: https://community.cadence.com/cadence_technology_forums/f/custom-ic-design/33217/how-to-add-a-list-of-model-files-into-ade-form-through-command-line
 [^3]: https://wiki.to.infn.it/doku.php?id=vlsi:workbook:analog:cdsenv
