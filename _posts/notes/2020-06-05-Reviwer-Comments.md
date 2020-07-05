---
title: Reviewer Comments
categories:
  - notes
---

Types of reviewer comments on submitted manuscripts. Things reviwers are looking for in an article for it to be accepted.

## Language, Writing style, Typo
* Even though the work is interesting, the paper is poorly written and need significant modification to maintain the scientific rigour of this work.
* paper is not easy to follow
* there are many places whre the language is poor
* language shuold be imporved for e.g. ...an exerpt from manuscript...
* However, the writing needs to be improved. Some sentences need to be revised, for example, ...
* Authors are advised to closely check for grammar and spelling errors (typos here and there) from a native English speaker
* Please revise the grammar to improve the readability.
* Replace 'Eq. 1' with standard notation of (1) in the text


It is necessary to submit a typo free mansucript to make a good impression. It has a psychological effect on the reviewer. A manuscript with a lot of typos paints a negetive image of the writer on the reviwer's mind even if the intellectual content of the paper is sound. Missing articles, subject-verb singular plural agreement can be annoying for a native speaker. However, even after having the manuscript formatted by the university writing center, some reviewers complain of poor writing. This problem is hard to address. Specially when one reviewer says this paper is well written and easy to follow but another reviwer, for the same paper, complains of poor writing.
{: .notice--warning}

## Statistical skeptisism
* A modified algo. is provided. The proposed approach offers 3% more accuracy on a data set. However, this has to be confirmed over various data sets and the convergence result established.
* You should provide several plots to show that the chosen parameter value works for a wide range of input current. Because it is always possible to obtain a good match for one particular input which does not work for other inputs.  

## Comparison to other relevant works
* Also, I have not seen any hardware results relevant to circuit design of the proposed method or any comparison to [7] or [8]. 
* A detailed comparison with other recent and relevant work is needed to clearly show the advantage of the proposed method.
* The comparison with state-of-the-art techniques is missing for e.g. ...some refs...
* A comparison table can be added to list key specification parameters for comparison. 


## Clarity of key aspects
* The paper does not clearly describe the key modifications in the algorithm?
* The author mentioned, "Throughout the paper the modified algorithm is referred to as new network for simplicity" in Section I and "third set with the reconstructed images of the first set using new algorithm" in Section V. Did the author propose a new network or a new algorithm? It should be clear.
* The authors should mention in their manuscript that what spiking model of neurons they have implemented. Is it LIF or any other model.
* but in this work the overall novelty should be clearly stated.

Not sure why some reviewers use question marks on comments which are clearly not questions.
{: .notice--warning}

## Scaling of device and system
* Does the system scale up?
* Big question is how do you plan to create a network from this circuit? 
* it is pretty large. That will degrade the neuron packing density?
* Please use gm-Id topology to scaling the transistor (and noise contributions during the initiation current, Iin is ON)
*  Why are these dimensions optimal? Please also comment on why the minimum length was not used in the 13nm process. In general, it would be helpful to include analysis/descriptions that give insights into the rationale of how the transistors were sized in the circuit with compensation. 

## Process, Voltage and Temperature (PVT) variation
* Are these multiple types of signals robust (in terms of multiple run)? Please use some statistical tests to see upper and lower bound of variations. 


## Follow up questions
*  The author wrote , “this process is repeated until a stable solution is reached.” Will there be an unstable solution in this process? If possible, it is better to explain the unstable situation, too?
* Does the proposed method generalize to 3 or 4 dimensional case?
* Your neuron only accepts a single input, whereas, biological neurons can take several inputs. How do you plan to accommodate this?


## Literature survey
* The literature survey is weak and outdated.

