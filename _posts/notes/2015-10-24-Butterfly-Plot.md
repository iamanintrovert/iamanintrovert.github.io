---
title: How to Plot Butterfly Curve of SRAM in cadence
categories:
  - notes
tags:
  - research
  - CAD
---

## Schematic

Setup your SRAM back to back intverts in schematic. On one of the inverter input attache a DC voltage source and assign the DC voltage to a name instead of a value for DC sweep.

![butterfly1]({{ site.url }}{{ site.baseurl }}/assets/site-images/notes/butterfly/butterfly1.png){: .align-center}

------------------------------------

## Simulation Setup

In the ADE simulation window set the spectre simulation mode, model libraries and necessary stimulous. Set DC sweep settings. Plot both input and output of the inverter to which DC voltage source was attached to. For my case output was V2 and input was V1. Then in the graphing window go to Axis->Y vs Y. Set trace to /V2, plot destination to new subwindow, hit ok. Now click on the original plot to select the original plot subwindow. Again go to Axis->Y vs Y but this time set trace to /V1. You should have V1 vs V2 graph and V2 vs V1 graph in two subwindows. Drag one of them on to another and you should have a butterfly plot.

![butterfly2]({{ site.url }}{{ site.baseurl }}/assets/site-images/notes/butterfly/butterfly2.png){: .align-center}
