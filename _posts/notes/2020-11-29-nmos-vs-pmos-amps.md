---
title: nmos vs pmos amps
categories:
  - notes
tags:
  - research
---
Unity gain followers help us measure on chip signals by providing large currents. It also helps in isolating the measurement device node and the actual on chip circuit node thus
preveting the measureing device from affecting the circuit operation. We have two choice when using unity gain follower. One is nmos tail diff amp and other is pmos tail diff amp. 
Depending on the circumstances one is a better choice than the other. 

## Problem with nmos diff amp as unity gain followers
When the input voltage drops at the gate, the follower gate voltage also drops. This makes the drain voltage of the nmos tail current source to drop also. After the input voltage drops 
below the gate voltage of the nmos tail current source, the drain voltage of the nmos tail current source becomes close to the source voltage. This stops the current flow which prevents the output node
to dischage. As a result output node voltage stays at a relatively higher voltage and tracking low voltage does not work. To solve this we need to make sure that there are sufficient drain to source
voltage at the nmos tail current source so that enough current can flow. Simply reducing the vss voltage from ground to a more negative voltage does the trick and it can track low voltages which
are close to the gournd. We can use seperate vss for the unity gain follower. However, using more negative voltage at vss means that the all the body terminals of the nmos transistors in chip is now 
connected to the negative vss because all the nmos has the same substrate. This is not what we want. To solve this we would need independet body terminal for nmos devices. This is not possible in a
single well process.

<figure class="third">
	<a href="/assets/site-images/notes/nmos-vs-pmos-amps/nmos-diff.png"><img src="/assets/site-images/notes/nmos-vs-pmos-amps/nmos-diff.png"></a>
	<a href="/assets/site-images/notes/nmos-vs-pmos-amps/nmos-slow.png"><img src="/assets/site-images/notes/nmos-vs-pmos-amps/nmos-slow.png"></a>
	<a href="/assets/site-images/notes/nmos-vs-pmos-amps/nmos-fast.png"><img src="/assets/site-images/notes/nmos-vs-pmos-amps/nmos-fast.png"></a>
	<figcaption>Unity gain follower with nmos diff amp.</figcaption>
</figure>

## Solution using pmos diff amp as unity gain followers
That is why pmos tail current diff amp is used because the body termial votlage can be changed independently of other pmos devices in the chip. When vdd is the same as the maxiumum volage of the input,
we see the same effect as nmos diff amp but this time when tracking higher voltage. But now we can increase the vdd of the diff amp wihtout affecting the pmos body terminals of other circuits in the chip.

<figure class="third">
	<a href="/assets/site-images/notes/nmos-vs-pmos-amps/pmos-diff.png"><img src="/assets/site-images/notes/nmos-vs-pmos-amps/pmos-diff.png"></a>
	<a href="/assets/site-images/notes/nmos-vs-pmos-amps/pmos-slow.png"><img src="/assets/site-images/notes/nmos-vs-pmos-amps/pmos-slow.png"></a>
	<a href="/assets/site-images/notes/nmos-vs-pmos-amps/pmos-fast.png"><img src="/assets/site-images/notes/nmos-vs-pmos-amps/pmos-fast.png"></a>
	<figcaption>Unity gain follower with pmos diff amp.</figcaption>
</figure>
