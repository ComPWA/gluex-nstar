# Reaction and Models

<!-- cspell:ignore Mathieu -->
<!-- This amplitude model is adapted from the [Lecture 11 in STRONG2020 HaSP School](https://indico.ific.uv.es/event/6803/contributions/21223/) by Vincent Mathieu. -->

## Reaction with Resonances and Decay

The (photo-production) reaction is $ \gamma p \to \eta \pi^0 p$, its decay is described by an amplitude model with three possible resonances: $a_2$, $\Delta^+$, and $N^*$.

```{image} https://github.com/ComPWA/compwa-org/assets/17490173/ec6bf191-bd5f-43b0-a6cb-da470b071630
:width: 100%
```

## Amplitude Models

The amplitude model is adapted from the [Lecture 11 in STRONG2020 HaSP School](https://indico.ific.uv.es/event/6803/contributions/21223/), only the Breit-Wigner and Spherical harmonics terms are kept for doing PWA eventually, as shown in equation {eq}`BW_SH_label`.

```{math}
:label: BW_SH_label
\begin{eqnarray}
A^{12} &=& \frac{\sum a_m Y_2^m (\Omega_1)}{s-m^2_{a_2}+im_{a_2} \Gamma_{a_2}} \\
A^{23} &=& \frac{\sum b_m Y_1^m (\Omega_2)}{s-m^2_{\Delta}+im_{\Delta} \Gamma_{\Delta}}  \\
\
A^{31} &=& \frac{c_0}{s-m^2_{N^*}+im_{N^*} \Gamma_{N^*}}
\end{eqnarray}
```

where s is the Mandelstam variable, m is the mass, $\Gamma$ is the width, $Y^m_l$ is the spherical harmonics, $\Omega_i$ is the decay angles (a pair of Euler angles), and $a_i$, $b_i$, and $c_i$ are coefficients

:::{note}
Mandelstam variables $s_{ij}=(p_i+p_j)^2$, $t_i=(p_a-p_i)^2$, and $u_i=(p_b-p_i)^2$.
:::

with intensity $I$ and amplitude $A$:

```{math}
:label: 123_label
\begin{eqnarray}
I &=& |A|^2 \nonumber \\
A &=& A^{12} + A^{23} + A^{31} \\
\end{eqnarray}
```

where $\quad 1 \equiv \eta ; \quad  2 \equiv \pi^0 ; \quad 3 \equiv p$

:::{note}
The choice of the amplitude model (equations (1) and (2)) for PWA in this tutorial consists of three resonances, and each of them are formed by two terms: Breit-Wigner with Spherical harmonics ($l = 2, 1, 0$).
:::

:::{important}
The spin of $\eta$ meson and $\pi^0$ meson are all 0. But the spin of proton is not 0, it is spin-$\frac{1}{2}$.

In this amplitude model **spin** of baryon is simplified (not realistic):
$\eta$, $\pi^0$ and $p$ are all treated as spin-0 particles.

This means that total intrinsic spin $s$ is ignored in this model,
the total angular momentum
$J$ of the system or any subsystems within this model will solely depend on the orbital angular momentum
$L$, characterized by quantum number $l$.
And this simplifies the use of spherical harmonics $Y_l^m(\theta,\phi)$,
since only the orbital angular momentum component is involved, and thus the combination of contribution is not considered (e.g. Clebsch-Gordan Coefficients).

In our case:

- $A^{12}$ amplitude represents a d-wave interaction, as indicated by $l=2$.
  - The possible $m$ values are $−2,−1,0,1,2$. Each of these values corresponds to different orientations of the d-wave. The wave type is solely determined by $l$ and all these $m$ values still describe d-wave characteristics.
- $A^{23}$ amplitude represents a p-wave interaction, as indicated by $l=1$.
  - The possible $m$ values are $−1,0,1$. Each of these values corresponds to different orientations of the p-wave. Similarly, these values are all p-wave orientations.
- $A^{31}$ amplitude represents a s-wave interaction, as indicated by $l=0$. - The only possible $m$ value is 0, which is consistent with the spherical symmetry of s-waves.

:::
