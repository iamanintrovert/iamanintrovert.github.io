---
title: Running Spectre Simulation from Python
categories:
  - notes
tags:
  - research
  - CAD
---

Running Virtuoso Spectre simulation using OCEAN scripts can be very powerful way to get much out of the simulator. But OCEAN scripts are written in SKILL syntax which in my opinion is not very user friendly and modern. It would be much nicer if those scripts could be written in syntax like python. Although that luxury is not provied, we can use python scripts to communicate to Cadence Virtuoso through inter process communication and access SKILL/OCEAN functions and have those data manipulate in the usual way we manipulate data in python. A python toolbox [skillbridge](https://github.com/unihd-cag/skillbridge) does exactly that.
