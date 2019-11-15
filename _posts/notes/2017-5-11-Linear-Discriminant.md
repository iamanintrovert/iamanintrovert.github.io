---
title: Linear Discriminant Analysis
categories:
   - notes
tags:
  - research
  - algorithm 
---

For class label $$C \in \{ 1,2, \cdots K \}$$ and feature vector $$X \in \mathbb{R}^p$$ the classification problem can be described as the probability of a class being $$C=j$$ given a feature set $$X=x$$. Mathematically 

$$
\begin{equation}\label{eq:LDA_1}
f(x) = P(C=j \mid X=x)
\end{equation}
$$

If this function is evaluated across all of the class labels then the label with the highest probability gives the class that $$X=x$$ belongs to. Hence the Eq.\ref{eq:LDA_1} can written as

$$
\begin{equation}\label{eq:LDA_2}
f(x) = \operatorname*{arg\,max}_{j=1,2,\cdots K} P(C=j \mid X=x)
\end{equation}
$$

From the property of conditional probability we can rewrite

$$
\begin{eqnarray} 
P(C=j \mid X=x)P(X=x) = P(X=x \mid C=j)P(C=j) \nonumber \\
P(C=j \mid X=x) = \frac{P(X=x \mid C=j)P(C=j)}{P(X=x)} \label{eq:LDA_3}
\end{eqnarray}
$$

Using Eq.\ref{eq:LDA_3} in EQ.\ref{eq:LDA_2} can rewritten as

$$
\begin{align}
f(x) &= \operatorname*{arg\,max}_{j=1,2,\cdots K} \frac{P(X=x \mid C=j)P(C=j)}{P(X=x)} \nonumber \\
f(x) &= \operatorname*{arg\,max}_{j=1,2,\cdots K} P(X=x \mid C=j)P(C=j) \nonumber \\
f(x) &= \operatorname*{arg\,max}_{j=1,2,\cdots K} P(X=x \mid C=j)\cdot \pi_j \label{eq:LDA_4}
\end{align}
$$

Because $$P(X=x)$$ does not depend on $$j$$ and is constant, removing that term from equation does not influence the function. Here $$\pi_j=P(C=j)$$ is the prior probability of class $$j$$. Rearranging Eq.\ref{eq:LDA_2} into Eq.\ref{eq:LDA_4} allows for us to estimate the conditional class density $$P(X=x \mid C=j)$$ from the sample data which is the training data. Linear Discriminant Analysis approximates this rule by modeling conditional class densities as multivariate normals.
$$
\begin{equation}
h_j(x) = P(X=x \mid C=j) = N(\mu_j, \Sigma)
\end{equation}
$$

i.e. each class $$j$$ has its own mean $$\mu_j \in \mathbb{R}^p$$, but shares a common covariance matrix $$\Sigma \in \mathbb{R}^{p\times p}$$. Hence the multivariate normal density 

$$
\begin{equation}
h_j(x) = \frac{1}{(2\pi^{p/2})det(\Sigma)^{1/2}}e^{-\frac{1}{2} (x_i - \mu_j)^T\Sigma^{-1} (x_i - \mu_j)}
\end{equation}
$$

We want to find $$j$$ so that $$P(X=x \mid C=j)\cdot \pi_j = h_j(x)\cdot \pi_j$$ is largest. Since $$\log{.}$$ is a monotonic function, we can consider maximizing $$\log{[h_j(x)\cdot \pi_j]}$$ over $$j=1,2,\cdots K$$. We can define the rule

$$
\begin{align}
f^{LDA}(x) &= \operatorname*{arg\,max}_{j=1,2,\cdots K} \log{[\frac{1}{(2\pi^{p/2})det(\Sigma)^{1/2}}e^{-\frac{1}{2} (x_i - \mu_j)^T\Sigma^{-1} (x_i - \mu_j)}\cdot \pi_j]} \nonumber \\
&= \operatorname*{arg\,max}_{j=1,2,\cdots K} [x^T\Sigma^{-1}\mu_j - \frac{1}{2}\mu_j^T\Sigma^{-1}\mu_j + \log{\pi_j}] \nonumber \\
&= \operatorname*{arg\,max}_{j=1,2,\cdots K} \delta_j(x)
\end{align}
$$

We call $$\delta_j(x), j=1,2,\cdots K$$ the discriminant functions [^1]. When we replace $$\pi_j, \mu_j, \Sigma$$ with their sample estimates, based on the labeled observations $$y_i \in {1,2, \cdots K}$$, $$x_i \in \mathbb{R}^p$$, $$i = 1,2, \cdots n$$,

$$
\begin{align}
\hat{\pi_j} &= \frac{n_j}{n} \nonumber \\
\hat{\mu_j} &= \frac{1}{n_j}\sum_{y_i=j} x_i \nonumber \\
\hat{\Sigma} &= \frac{1}{n-K}\sum^{k}_{j=1}\sum_{y_i=j}(x_i-\hat{\mu_j})(x_i-\hat{\mu_j})^T \nonumber
\end{align}
$$

The rule can then be written as

$$
\begin{equation}\label{eq:LDA_5}
\hat{f}^{LDA}(x) = \operatorname*{arg\,max}_{j=1,2,\cdots K} \hat{\delta_j}(x)
\end{equation}
$$

where $$\hat{\delta_j}(x)$$ is the estimated discriminant function of class j,

$$
\begin{align}
\hat{\delta_j}(x) &= x^T\hat{\Sigma}^{-1}\hat{\mu_j} - \frac{1}{2}\hat{\mu_j}^T\hat{\Sigma}^{-1}\hat{\mu_j} + \log{\hat{\pi_j}} \nonumber \\
&= a_j + b_j^Tx \label{eq:LDA_6}
\end{align}
$$

where $$a_j = - \frac{1}{2}\hat{\mu_j}^T\hat{\Sigma}^{-1}\hat{\mu_j} + \log{\hat{\pi_j}}$$ and $$b_j = \hat{\Sigma}^{-1}\hat{\mu_j}$$. For a Given $$X=x$$ we use Eq.\ref{eq:LDA_5} to find the output class. Eq.\ref{eq:LDA_6} is just a set of equations of lines. It can be written in expanded from as follows.

$$
\begin{align}
\hat{\delta_1} &= b_{11}*i_1 + b_{12}*i_2 + ... + w_{1n}*i_n + a_{1} \nonumber\\
\hat{\delta_2} &= b_{21}*i_1 + b_{22}*i_2 + ... + b_{2n}*i_n + a_{2}\\
\vdots \nonumber\\
\hat{\delta_m} &= b_{m1}*i_1 + b_{m2}*i_2 + ... + b_{mn}*i_n + a_{m} \nonumber
\end{align}
$$

The decision boundary between two class can also be found from these equations. The boundary exists where the values of the equations for two classes become equal. The decision boundary between classes $$j,k$$ is the set of all $$X \in \mathbb{R}^p$$ such that $$\hat{\delta}_j(x)=\hat{\delta}_k(x)$$, i.e.

$$
\begin{eqnarray}
a_j + b_j^Tx = a_k + b_k^Tx \nonumber\\
(a_j - a_k) + (b_j^T - b_k^T)x = 0 \label{eq:LDA_boundary}
\end{eqnarray}
$$

This is the equation of the line that defines the decision boundary of class $$j$$ and $$k$$.

<div class="divider"></div>
### training code
```matlab
function ob = lindisTrain(meas, species)
% take in data as samples in each row

x = meas'; % same dimension values along same row
y = species';

%% data preparation
Y = grp2idx(y);
cls = unique(Y);
% http://www.stat.cmu.edu/~ryantibs/datamining/lectures/20-clas1-marked.pdf
%% estimate unknown qunaties from sample estimates
sigma = 0;
for i = 1:length(cls)
    prior(1, i) = sum(Y == i)/length(Y);
    mu(:, i) = sum(x(:, Y == i), 2)/sum(Y == i);
    XminMu = x(:, Y == i) - repmat(mu(:, i), 1, sum(Y == i));
    sigma = sigma + XminMu * XminMu';
end
sigma = sigma / ( length(Y) - length(cls) );
%% estimated discriminant
A = (inv(sigma)*mu);
B = diag(-(0.5)*mu'*inv(sigma)*mu)' + log(prior);

ob = struct('A', [], 'B', [], 'sigma', [], 'mu', [], 'Classname', []);
ob.A = A;
ob.B = B;
ob.sigma = sigma;
ob.mu = mu;
ob.Classname = unique(species);
```

### classification code
```matlab
function cls = lindisClassification(ob, meas)
% features in one row
x = meas';
Y = x'*ob.A + ob.B;
[~, argmax] = max(Y);
cls = ob.Classname(argmax);
```

------------------------------------------

[^1]: Notes taken from online lecture notes of Dr. Ryan Tibshirani of CMU. [http://www.stat.cmu.edu/~ryantibs/datamining/](http://www.stat.cmu.edu/~ryantibs/datamining/)
