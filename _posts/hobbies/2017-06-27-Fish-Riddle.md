---
title: Fish Riddle
categories:
   - hobbies
tags:
  - riddles
---

I found this riddle in a TEDEd vieo. The reason I am including it here is that it is one of those problems that helped me learn to put together simple tools to solve an unknown problem. Another reason is that I solved it myself not using the method shown in the video. ;)

<iframe width="854" height="480" src="https://www.youtube.com/embed/lLOALyWls2k?list=PLJicmE8fK0EiFRt1Hm5a_7SJFaikIFW30" frameborder="0" allowfullscreen></iframe>

The simplified riddle statement goes like this. There are few fish tanks carried by a ship across the ocean. Each tank has equal number of fishe. On the ships voyage the ship is struck by storm in a shark infested water. All of the fish tanks are thrown overboard. The ships log book is missing and no one remembers how many fish tanks were on board. The captain of the ship scans the ocean floor using a device on the ship and finds there are total 50 creatures in the water including the sharks. Then the captain devides the scanned region in three sectors and starts sanning again on the sectors one by one. He finds 2 sharks and 4 tanks on sector 1. 4 sharks and 2 tanks sector 2. But then the device gets broken before the captain could scan third sector. The captain needs to know how many tanks are there in sector 3.

<center>
<img src="{{site.url}}{{site.baseurl}}/assets/site-images/hobbies/riddles/sectors.png" />
</center>

The captain some additional information. The ship had a maximum of 13 fish tanks. And the sectors of the ocean floors he scanned has such a property that each sector has at least 1 and a maximum of 7 sharks. No two sectors has the same number of sharks. In summery the available informations are as follows.

1. There are total 50 creatures total. That includes sharks outside the tanks and fish inside.
2. Each sector has anywhere from 1 to 7 sharks, with no two sectors having the same number of sharks.
3. Each tank  has an eaual number of fish.
4. In total, there are 13 or fewer tanks.
5. sector 1 has 2 sharks and 4 tanks.
6. sector 2 has 4 sharks and 2 tanks.

How many tanks are there in sector 3?

### Solution
Lets formulate the problem this way. There are $$x$$ fishes in each tank. In sector 3, there are total $$S$$ sharks and there are total $$T$$ fish tanks. Then the total number of creatures can be written as

$$
\begin{align}
50 &= 2 + 4x + 4 + 2x + S + Tx \nonumber\\
44 &= x(6 + T) + S \label{eq:rule}
\end{align}
$$

Additionally we know that there could be a total of 13 tanks. So sector 3 must have 7 or fewer tanks. Since no two sectors has the same number of sharks the number of sharks would be any number from 1 to 7 except 2 and 4. So value of S and T could be 

$$
\begin{align}
S &= 1, 3, 5, 6, 7 \nonumber \\
T &= 1, 2, 3, 4, 5, 6, 7 \nonumber
\end{align}
$$

So we have three unknows $$x, T, S$$, one equation Eq.\ref{eq:rule}. We have two range of values for $$S$$ and $$T$$. Which we can consider as another two equation. So we have three equation and three unknowns. Which means the problem is solvable. But since we have a range of values for two equations the solution would also be a range of values. How will we find out the actual solution? This can be resoved by looking at $$x$$. $$x$$ is the number of fish in each tank. So this value must be an integer. If we solve for $$x$$ from Eq.\ref{eq:rule} there must a pair of values for $$S$$ and $$T$$ for which $$x$$ is an integer.

$$
\begin{align}
x = \frac{44-S}{6+T} \label{eq:x}
\end{align}
$$

Lets look at the neumerator and denominator of Eq.\ref{eq:x} for each value of  $$S$$ and $$T$$.

$$
\begin{align}
numerator: &43, 41, 39, 38, 37 \nonumber \\
denominator: &7, 8, 9, 10, 11, 12, 13 \nonumber
\end{align}
$$

only 39/13 produces an integer. The unknows are now known. $$x=3, S=5, T=7$$. There are 7 tanks in sector 3 that the captain needs to know. 

-------------------------

The video solves it in a different way which reveals an important piece information to me. The best way to compare multiple pieces of partial information: a table.



