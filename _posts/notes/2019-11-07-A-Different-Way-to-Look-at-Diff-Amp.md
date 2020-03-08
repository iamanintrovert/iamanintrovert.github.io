---
title: A Different Way to Look at Diff Amp
categories:
  - notes
tags:
  - research
---

Lets look at inverter. For rail to rail input voltage pulse the invert outputs inverted rail to rail voltage pulse. When input is at ground, PMOS is active (ready to conduct a lot of current) but the NMOS is inactive (conducts only leakage current). From the graphical solution, we get top rail voltage as output voltage. The current at this stage is very low (equal to the leakage current of NMOS). When input is at top rail voltage the opposite happens and we get bottom rail voltage as output. When input is halfway between the top and bottom rail voltage, both PMOS and NMOS is able to conduct current. From the graphical solution we see that the output is somewhere in between the rail voltages. But the important thing to notice is that the current is quite high at this stage. When the input is halfway between the rail voltages, at 0.5V, the gate to source voltage for both PMOS and NMOS 0.5V. This much gate to soure voltage is enough to produce several hundrades of nano amperes of current even when operating in subthreshold regime. For low power application, this is a lot of current. To reduce power consumption during the transition period we have to reduce the current. 

<center>
<img width="80%" src="{{site.url}}{{site.baseurl}}/assets/site-images/notes/diff-amp/inv.png" />
</center>

To reduce the current, we can decrease the gate to source voltages. We can split the input into PMOS and NMOS input. Then supply lower gate to source voltages as in the following figure. But how would we get two seperate lower gate to source voltages? The input will not come this format. We decreased the gate to source voltage to decrease the current. Alternatively, we can decide how much current we want and create gate to source voltage from that.

<center>
<img width="80%" src="{{site.url}}{{site.baseurl}}/assets/site-images/notes/diff-amp/inv-2.png" />
</center>

We need two different voltages. One that turns ON one MOS while the second turns OFF other MOS. A diff pair can be used for that. As in the following figure, with the help of a reference voltage, tail current can be streed into two legs. When input is 0, all the tail current is flowing in one leg while another leg gets nothing. The opposite thing happens when input is 1. Now we need to convert the current to voltage using diode connected MOS. The resulting voltages at the gate of the diode connected MOS will appropriately set themselves according to the current flowing. But both the voltages are PMOS gate to source voltages. We need one NMOS gate to source voltage.

<center>
<img width="60%" src="{{site.url}}{{site.baseurl}}/assets/site-images/notes/diff-amp/diff-pair.png" />
</center>

This task is simple. We can simply copy the current from one leg and use NMOS diode connected load to produce gate to source voltage for NMOS. Now we have both PMOS and NMOS gate to source voltages for an amount of currnet given by the tail current of diff pair. If we connect these two voltages to the split up connections of the inverter, we have our desired inverter. Now we can control how much power is consumed during inverter transition by controlling the tail current of the diff pair. As added bonus now we can also control the switching threshold using reference voltage. 

<center>
<img width="50%" src="{{site.url}}{{site.baseurl}}/assets/site-images/notes/diff-amp/diff-amp.png" />
</center>

Quite an elaborate way to make a low power invter. Hang on! Is that a wide range diff amp?