# $p \gamma \to \eta \pi^0 p$ reaction and models

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
While the **spin** of the $\eta$ meson and the $\pi^0$ meson are both $0$, the spin of the proton is spin-$\frac{1}{2}$.
However, in order to simplify the amplitude model, we treat the proton as a spin-0 particle.
Overall, the $\eta$, $\pi^0$ and $p$ are therefore all treated as spin-0 particles.

The primary motivation for assuming proton to be spin-$0$ is to avoid the necessity of aligning the amplitudes (see e.g. [ComPWA/ampform#6](https://github.com/ComPWA/ampform/issues/6)).
This assumption enables the intensity $I$ to be written as a coherent sum of the amplitudes of the subsystems without the need for additional Wigner rotations.
In addition, the amplitude for each decay chain contains only one spherical harmonic, namely that of the resonance.

The spherical harmonics in Equation&nbsp;{eq}`BW_SH_label` are therefore relevant only to the resonances.
Here, $l$ represents the spin of the resonances and $m$ represents its spin projection in the decay chain.
The total angular momentum and coupled spin (for the two-body state of the two decay products of the resonance) are not considered.
According to {cite}`Richman:1984gh` and other classical references on helicity, this is known as the **helicity basis**.
In contrast, the **canonical basis** does not sum over $L$ and $S$, resulting in a more complex coherent sum of amplitudes.
The transformation between these bases is also discussed [here](https://ampform.rtfd.io/0.15.x/usage/helicity/formalism.html) on the AmpForm website.

In our case:

- $A^{12}$ represents a **d-wave** interaction, because we assume there is a $a_2$ resonance (spin&nbsp;2) in this subsystem. The possible $m$&nbsp;values are $−2,−1,0,1,2$. Each of these values corresponds to different orientations of the d-wave.
- $A^{23}$ represents a **p-wave** interaction, because we assume this subsystem has a (spin-1) $\Delta^+$ resonance. The possible $m$&nbsp;values are $−1,0,1$.
- $A^{31}$ represents an **s-wave** interaction, because we assume there is one spin-0 $N^*$ resonance in this subsystem. The only possible $m$ value is 0 and, since $Y_0^0=0$, the amplitude only consists of a Breit–Wigner.

:::
