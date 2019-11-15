---
title: Why $$0!=1$$?
categories:
  - notes
---

It is one of those topics that makes sense when I learn it. But as time passes by suddenly it stops to make sense. And I find myself asking the question that should not be asked after all these time working with it. The question is why $$0!=1\$$? Sure what else would it be. When working with factorials, it is sufficient to know that the factorial of a number is the multiplication of all the whole numbers from leading up to that number.

$$
\begin{equation}\label{eq:factorial}
n! = n \times (n-1) \times (n-2) \times \cdots 3 \times 2 \times 1 
\end{equation}
$$

After working with only this definition long enough, it is only natural to get shaky on the actual concept of why we use factorial. And that is when I think most of us find ourselves asking how is $$0!=1\$$ then! It does not fit the definition above.

To answer the question we have to get back to original problem where factorial is used. Permutation. The number of ways a group of objects can be arranged. If one object can be arranged $$m$$ times and for each of those arrangement another object can be arranged $$n$$ times, together they can be arranged $$m\times n$$ times. How many times can $$n$$ objects be rearranged? Well each of those arrangements can  be thought of as $$n$$ objects holding $$n$$ boxes. Starting off, in the first box we have $$n$$ objects available to us. We can place any one of them in the first box. So the first box can be filled $$n$$ ways. After using up one object in the first box we have $$(n-1)$$ objects available for the next box. So we can fill the next box $$(n-1)$$ ways. Together we can have $$n\times(n-1)$$ ways to fill the two boxes. This way for the next box we have $$(n-2)$$ objects available which can fill the box $$(n-2)$$ ways. So together with three boxes we have $$n \times (n-1) \times (n-2)$$ ways to fill them. This way get to the very last box where only one object is available to us which can use only one way. Which is, as it is. This is how we get the definition of factorial in Eq.\ref{eq:factorial}. Lets apply this arrangement concept. For three objects there are six ways to arrange them. For two objects there are two ways to arrange them. For only one object we cannot create any extra arrangments. There is only one arrangement which is *they way it already is*. So how many arrangement can we create with zero objects? In other words,  how many arrangments are there for nothing?

$$
\begin{align}
3! &= 3\times 2\times 1 \nonumber \\ 
2! &= 2\times 1 \nonumber \\
1! &= 1 \nonumber \\
0! &= ? \nonumber
\end{align}
$$

We are presented with nothing. And we cannot create any extra arrangement other than the way it already is. So *the way it already is* is one arrangement. And we cannot add any more arrangement. So $$0!=1$$. Simple. But easy to forget.
