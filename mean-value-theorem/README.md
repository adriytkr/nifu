# Mean Value Theorem

If $f$ is continuous on $[a,b]$ and differentiable on $(a,b)$, then
\[
f'(c)=\frac{f(b)-f(a)}{b-a}
\]
for some $c$ on $(a,b)$

The Mean Value Theorem (MVT) is pretty straightforward, although its proof is technically demanding.

It basically states that there exists at least one tangent line that is parallel to a secant line.

![MVT Visualization](./mvt-intro.gif)

The full proof lies at the end of the document for it requires the preliminary theorems to a rigorous proof.

- [Mean Value Theorem](#mean-value-theorem)
  - [Fermat's Theorem](#fermats-theorem)
    - [Proof](#proof)
  - [Extreme Value Theorem](#extreme-value-theorem)
    - [Proof](#proof-1)
  - [Rolle's Theorem](#rolles-theorem)
    - [Proof](#proof-2)
  - [Formal Proof of Mean Value Theorem](#formal-proof-of-mean-value-theorem)

## Fermat's Theorem

If $f$ has a local minimum or maximum at $c$ and $f$ is differentiable at $c$, then $f'(c)=0$

### Proof

Let $f$ be differentiable at $c$. Without loss of generality, assume f has a local max at $c$. Then $f(c) \ge f(x)$ for all $x$ near $c$.

Since $f$ is differentiable at $c$, the limit

\[
\lim_{h \to 0}\frac{f(c+h)-f(c)}{h}
\]

exists. Thus, the right-hand and left-hand limits both exist and equal $f'(c)$. We consider each separately.

For the right-hand side, we have $h>0$ and $f(c+h)-f(c) \le 0$. Hence, we obtain the following inequality

\[
\begin{equation}
\lim_{h \to 0^+}\frac{f(c+h)-f(c)}{h} \le 0
\end{equation}
\]

Similarly for the left-hand side limit, we obtain

\[
\begin{equation}
\lim_{h \to 0^-}\frac{f(c+h)-f(c)}{h} \ge 0
\end{equation}
\]

Since the left-hand side and right-hand side are equal, the only possible value is $0$. Thus, we obtain

\[
\lim_{h \to 0}\frac{f(c+h)-f(c)}{h} = 0
\]

Therefore, $f'(c)=0$.

## Extreme Value Theorem

If $f$ is continuous on $[a,b]$, then $f$ attains a maximum value at $x_{max}$ and a minimum value at $x_{min}$ where $x_{max}$ and $x_{min}$ lie on $[a,b]$.

### Proof

Under construction

## Rolle's Theorem

If $f$ is continuous on [a,b], differentiable on $(a,b)$ and $f(a)=f(b)$, then $f'(c)=0$ for some $c$ on $(a,b)$.

### Proof

We can divide the proof into two cases

**Case 1: $f$ is constant**

Then $f'(x)=0$ for all $x$. Hence, there exists at least one $c$ on (a,b) such that $f'(c)=0$.

**Case 2: $f$ is not constant**

Since $f$ is continuous on $[a,b]$, we can apply the Extreme Value Theorem. Since $f(a)=f(b)$ and $f$ is not constant, the maximum and minimum cannot both occur only at the endpoints. Hence, at least one of them must occur at some point on $(a,b)$.

Without loss of generality, assume $f$ attains a minimum at some point $c$ on (a,b). Then, by the Fermat's Theorem, $f'(c)=0$.

## Formal Proof of Mean Value Theorem

Let $f$ be continuous on $[a,b]$ and differentiable on $(a,b)$, and $L$ be the line that passes through the points $(a,f(a))$ and $(b,f(b))$. Then,

\[
L(x)=\frac{f(b)-f(a)}{b-a}(x-a)+f(a)
\]

Let $h(x)=f(x)-L(x)$. Then,

\[
h'(x)=f'(x)-\frac{f(b)-f(a)}{b-a}
\]

Notice that $h(a)=h(b)$. Hence, we can apply Rolle's Theorem to $h$. Thus, $h'(c)=0$ for some $c$ on $(a,b)$ and we obtain

\[
\begin{align*}
h'(c)&=0\\
&=f'(c)-\frac{f(b)-f(a)}{b-a}
\end{align*}
\]

Therefore,

\[
f'(c)=\frac{f(b)-f(a)}{b-a}
\]

for some $c$ on $(a,b)$.
