# pγ → ηπ⁰p

## Amplitude Analysis 101 / PWA101 (v2.0)

### CAS-assisted Amplitude Models building for photoproduction reaction

This document is a follow-up of PWA101 (v1.0), see **[TR&#8209;033](https://compwa.github.io/report/033)**.

Now the focus is the use of symbolic expressions (computations), with the use of [ComPWA packages](https://compwa.github.io/), or CAS(Computer Algebra System)-assisted model building in general (the python package SymPy in this case) to illustrate the general process in PWA.
Address to the issue ✅&nbsp;[ComPWA/gluex-nstar#1](https://github.com/ComPWA/gluex-nstar/issues/1), this document is PWA101(v2.0), which shows PWA methodologies and full workflow in the context of hadron physics with symbolic expressions via `sympy` and [ComPWA](https://compwa.github.io/).

In the following, an attempt to manually formulate the amplitude model via Sympy is shown.
Later on, attempts of automated amplitude model formualtion are done via e.g. `ampform` and `ampform-dpd`.

```{toctree}
reaction-model
manual
pgamma-state
automated
```
