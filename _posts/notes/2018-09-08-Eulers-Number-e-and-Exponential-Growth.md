---
title: Eulers Number $$e$$ and Exponential Growth
categories:
  - notes
---

One of the most important number in mathematics the constant $$e$$ that we use as base of natural logarithm, solution to differential equations and even in complex number. But unlike other mathematical constant like $$\pi$$, this constant does not come from geometry but from phenomenon of grouwth or decay.

The history of this number goes back as far as Bernoulli who wanted to know the total sum of money after 1 year of 100% interest compouned infinite times. We we have 1 unit of money at the start of a year and interest is 100% compouned n times a year, in the first cycle we would have $$(1+1/n)$$. In the second cycle $$(1+1/n)^2$$. After n cycles i.e. at the end of the year money would be $$(1+1/n)^n$$. Bernoulli wanted to know what this value becomes as $$n\to\infty$$ i.e. the limit $$\lim_{n\to\infty}(1+\frac{1}{n})^n$$. He was not able to find the limit which later Euler figured out.

<center>
<img width="50%" src="{{site.url}}{{site.baseurl}}/assets/site-images/notes/eulers-number/exps.png" />
</center>

But in formal mathematics the number $$e$$ finds its roots in differential calculus, from the rate of exponential/logarithmic growth/decay. Any exponential function $$y = b^x$$ represents expontial growth. Just like wanting to know velocity of something we have the need to know the rate of change of $$y = b^x$$. Differentiating this function leads to an interesting function.

$$
\begin{align}
\frac{dy}{dx} &= \lim_{h\to0}\frac{b^{x+h} - b^x}{h} = b^x[\lim_{h\to0}\frac{b^h - 1}{h}] = cb^x = cy
\end{align}
$$

The differential of $$y=b^x$$ is itself multiplied by a factor $$c = \lim_{h\to0}(b^h - 1)/h$$ which requires evaulatuion of a limit. But we know that this limit is finite because the slopes of the graphs in the figure is surely finite. Similarly there is the inverse function $$x = \log_b y$$ which has the differential

$$
\begin{align}
\frac{dy}{dx} &= cy \nonumber \\
\frac{dx}{dy} &= \frac{1}{cy}
\end{align}
$$

The rate of change of $$x = \log_b y$$ is $$1/cy$$. At $$x = 0$$, $$y = 1$$ regardless of any value of $$b$$. But the slope is $$1/c$$ which depends on $$b$$. So, depending on the value of $$b$$ slope at $$y = 1$$ will change. For the right choice of $$b$$ the slope will equal 1[^1].

$$
\begin{align}
\frac{1}{cy} &= \lim_{h\to0}\frac{\log_b(y+h) - \log_by}{h} = \lim_{h\to0}\log_b(1+\frac{h}{y})^{1/h} = \log_b\lim_{h\to0}(1+\frac{h}{y})^{1/h}
\end{align}
$$

At $$y = 1$$ this becomes
$$
\begin{align}
\frac{1}{c} &= \log_b\lim_{h\to0}(1+h)^{1/h} = \log_b e
\end{align}
$$

Here the limit $$\lim_{h\to0}(1+h)^{1/h}$$ is assigned a label $$e$$. We can clearly see that for $$b = e$$ the multiplying constant $$c$$ becomes 1. With a change of variable $$n=1/h$$, $$e = \lim_{n\to\infty}(1+\frac{1}{n})^n$$ which is same as the Bernoulli limit. Hence, the multiplying constant $$c$$ becomes $$c=1/\log_b e = \log_e b = \ln{b}$$.

# Why $$e$$ is natural choice for base?
Now when $$b = e$$, the derivative of $$y = \log_b x = \ln{x}$$ and $$y = b^x = e^x$$ is

$$
\begin{equation}
\frac{d}{dx}\ln{x} = \frac{1}{cx} = \frac{1}{\ln{b} x} = \frac{1}{\ln{e} x} = \frac{1}{x}
\qquad\text{and}\qquad
\frac{d}{dx} e^x = ce^x = e^x\ln{e} = e^x \nonumber
\end{equation}
$$

By the choice of $$e$$ as the base derivative of $$y = \log_b x$$ becomes a function of just the variable and derivative of $$e^x$$ is itself. This simplifies a lot of calculation in differential equations and thus serves as a natural choice of base.

# $$e$$ in complex number
What would be the result if we had raised the power of $$e$$ to a complex number? There is a very cool way to get the result. Lets suppose a point on the complex plane $$z = r\cos\theta + ir\sin\theta$$

$$
\begin{align}
z &= r\cos\theta + ir\sin\theta \nonumber \\
dz &= (-r\sin\theta + ir\cos\theta)d\theta \nonumber \\
dz &= i(r\cos\theta+ir\sin\theta)d\theta \nonumber \\
dz &= izd\theta \nonumber \\
\frac{dz}{z} &= id\theta \nonumber \\
\int \frac{dz}{z} &= \int id\theta \nonumber \\
\ln{|z|} &= i\theta + c \nonumber \\
z &= \pm e^{i\theta+c} \nonumber \\
z &= \pm e^c e^{i\theta} = Ce^{i\theta} \nonumber
\end{align}
$$

At $$\theta = 0$$, $$z = r\cos0 + ir\sin0 = r$$ and $$z = Ce^{i0} = C$$. Hence,

$$
\begin{align}
z = re^{i\theta} = r(\cos\theta + i\sin\theta)
\end{align}
$$

This is an equation used extensively in physics and engineering. For a number $$r$$ in the real number line, multiplying by $$e^{i\theta}$$ corresponds to a rotation of $$r$$ in the complex plane by an angle $$\theta$$.

----------------------

[^1]: Gilber Strang, Calculus, Wellesley-Cambridge Press, pp-236 
