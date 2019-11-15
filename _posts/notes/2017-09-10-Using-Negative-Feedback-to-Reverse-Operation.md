---
title: Using Negative Feedback to Reverse Operation
categories:
  - notes
---

Every engineering student is familiar with the concept of negative feedback. In electrical engineering it is a useful tool in increasing the stability of a system, increasing bandwith of the system, increase input resistance, decrease output resistance, improve noise performace etc. However there is another important application that it is used for and almost no textbook mentions it. It is a fundamental principle that some familiar circuits use but they are not presented/explained that way. 

In simple terms negative feedback means anyting that reduces the effect of input to the output. Usually we are introduced with negative feedback system with the following figure. 

![basic]({{site.url}}{{site.baseurl}}/assets/site-images/notes/inverse-operation/basic.png){: .align-center}

However, not every feedback system has a physical loop connecting output to the input as shown in the figure. For example the Common Source (CS) amplifier with degeneration resistor uses the negative feedback principle but there is no physical feedback loop. The resistor takes the output current build up a voltage across the resistor which reduces available input voltage $$V_{GS}$$. 

![CS]({{site.url}}{{site.baseurl}}/assets/site-images/notes/inverse-operation/CS.png){: .align-center}

Now going back at the basic feedback loop figure, if the forward gain $$a(s)$$ is high enough the transfer function of the system is reduced to $$1/f(s)$$.

$$
\begin{align}
X_{out} &= \frac{a(s)}{1+a(s)f(s)}X_{in} \nonumber \\
X_{out} &= \frac{1}{f(s)}X_{in} \nonumber \\
X_{in} &= f(s) X_{out} \nonumber \\
X_{in} &= F(X_{out}) \nonumber \\
X_{out} &= F^{-1}(X_{in}) \nonumber
\end{align}
$$

The input of the feedback path is the output of the closed loop system. Hence the closed loop system is actually implementing the inverse function of the feedback path[^1]. Explained differently, when the error $$\epsilon(s)$$ is zero or close to zero the feedback path $$F(.)$$ is taking $$X_{out}$$ as input and producing $$X_{in}$$ as output which is actually the closed loop input quantity. Effectively, the closed loop system is implementing the $$F^{-1}(.)$$ function where $$F(.)$$ is the feedback path function.

This is a very powerful conclusion because it lets us implement $$F^{-1}(.)$$ even when simply forcing an exitation at the output node is physically impossible to achieve some respose at the input node. This is the case for the transistors. The input exitation for a transistor is voltage and the output respose is current. However, it is not possible to inject current at the drain/collector and subsequently produce a voltage at the input node $$V_{GS}$$/$$V_{be}$$. (Because current cannot be produced without lowering the built in potential which requires voltage). 

One of the most important circuit in analog design is the current mirror which converts input current to a fixed voltage ($$V_{GS}$$/$$V_{be}$$) and then converts that voltage to current effectively mirroring that current. But how do we produce a voltage from current in a transistor which cannot implement this reverse function? The solution is to use negative feedback and place the transistor in the feedback path. Current is injected in the drain node. Lets visualize how the system should work. When the voltage at the output increases the current through the transistor increases which draws in the input current thereby starving the forward path of input current. Hence the feedback from the gate to drain is negative. If there is more current in the transistor which means there have to be more voltage $$V_{GS}$$ at the gate (assuming the source is at fixed potential). Hence the feedback from the drain to gate is positive[^2]. Since there is automatic gain in the forward path we do not need to implement $$a(s)$$. Only the loop needs to be completed which is done by simply connecting the drain to gate[^3]. As a result we get the familiar diode connected MOSFET.   

<center>
<img src="{{site.url}}{{site.baseurl}}/assets/site-images/notes/inverse-operation/ItoV_1.png" />
<img src="{{site.url}}{{site.baseurl}}/assets/site-images/notes/inverse-operation/ItoV_2.png" />
</center>

To me it is far more insightful to know the principle behinde the operation of the circuit rather than taking the circuit as an special case for granted which does not clearify the operation. I find it very upsetting that almost no book in analog design describes this circuit this way. This priciple of using negative feedback this way led me to understand other circutis like latch and other memory circuits that use positive feedback  to pull the output to one of the rail voltages. 

Usually the drain node is used as input node in current to voltage conversion. But this need not be the case. We can use the souce terminal as input node as well. Lets check this case for BJT. When the base voltage is increased it increases the emitter current which starves the forward path of input current. So the feedback from the output to the input is negative. However, when the emitter current increases it means $$V_{be}$$ increases. But $$V_{be}$$ can increase by decreasing emitter voltage and without any change to base voltage[^3]. So feedback from emitter to base is not necessarilly positive. Hence we need additional transistors to make the feedback positive[^2].  

![source_input]({{site.url}}{{site.baseurl}}/assets/site-images/notes/inverse-operation/source_input.png){: .align-center}

As this configuration needs additional transistors to make the forward feedback positive this is not a popular choice for the current mirror. 

--------------------------------------------

[^1]: Rahul Sarpeshker, Chapter 2, **Ultra Low power Bioelectronics, Fundamentals**, Biomedical Applications and Bio-inspired Systems. 
[^2]: Jörg Kramer, Chapter 5, *Liu, Kramer, Indiveri, Delbrück, Douglas*, **Analog VLSI: Circuits and Principles**, 
[^3]: I don't know how accurate this statement is. I am explaining them in my own way. They are not explicitly described this way in the other two references. 
