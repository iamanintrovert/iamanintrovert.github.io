---
title: Research
permalink: /research/
---
---------------------------
# Spiking Neural Network
Spiking neural networks are thought to be the next generation of neural networks for machine  learning. After the success of deep neural networks in classification and prediction tasks it became necessary to perform these tasks in the edge devices rather than in cloud for security reasons. However, training and prediction using deep networks requries huge memory and power that typically requries GPU. This makes it difficult to implement deep networks in low power chips without any modification like in memory computation, low power multiply accumulate circuit. Spiking neural network on the other hand consumes power only when neuron spikes and thus is a promising candidate for impelementing low power machine leanring chips. In my research I am trying to build a spiking neural network in silicon chip that reduces power and area by orders of magnitude in MNIST or CIFAR-10 classification task. 

# Analog Spiking Neuron Design
Numerous neuron design has been proposed after the first proposal of silicon spiking neuron by [Carver Mead](https://dl.acm.org/citation.cfm?id=64998). While some neuron designs are driven by the desire to reduce power many are driven by the desire to implement biologically realistic neurons as much as possible.
Recently [dynamical systems design](https://www.izhikevich.org/publications/spikes.htm) has emerged as a tool to model biologically realistic neurons. Using dynamical systems and [log-domain circuit design](https://ieeexplore.ieee.org/document/5648387) low power neuron circuits has been made. But they use a lot of transistors thereby increasing area which is prohibitive for large scale neural networks. In my research I am designing a neuron circuit that uses fewer transistors, low power and produces biologically realistic spiking patterns. 

# Spiking Neural Network Simulation
Unlike TensorFlow/PyTorch/Keras, a widely used standard of spiking neural network simulator is still in its early stages. Up until now, [brian2](https://brian2.readthedocs.io/en/stable/) has been a popular simulator primarily for computational neurocience. In my research I am using brian2 for testing neural networks I am planning to tape out. However, real neurons in silicon hardware has a lot of non-idealities that are not readily/easily modeled by differential equations in brian2. I am integrating cadence simulation of circuit blocks to help the brian2 simulator to inlcude device non-idealities in order to make hardware realistic simulation. 

# Analog Design Automation 
Although it is difficult to automate analog circuit design using behavioral description like digital design, some repeatitive analog circuit design can be automated. Neural networks have such repeative structures. In my research I am using tools such as SKILL scripting, interprocess communication from python to cadence to draw schematics and layout and do simulation using OCEAN scripting. I am using [skillbridge](https://unihd-cag.github.io/skillbridge/) to ease the process of writing SKILL/OCEAN commands by writing them directly in python.  


