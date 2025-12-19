# Symbolic Amplitudes for Light Baryons

[![Ruff](https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/charliermarsh/ruff/main/assets/badge/v2.json)](https://github.com/astral-sh/ruff)
[![uv](https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/astral-sh/uv/main/assets/badge/v0.json)](https://github.com/astral-sh/uv)
[![code style: prettier](https://img.shields.io/badge/code_style-prettier-ff69b4.svg?style=flat-square)](https://github.com/prettier/prettier)
[![Binder](https://static.mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/ComPWA/gluex-nstar/stable?urlpath=lab)

## $N^*$ Resonances at GlueX

> [!NOTE]
> This repository is under active development.

We are doing amplitude analysis and Partial Wave Analysis (PWA) with
[CAS-assisted model building](https://compwa.github.io/symbolics),
a technique employed in the ComPWA project.

- **First demonstration example:**
  $\gamma\,p \to \eta\,\pi^0\,p$, with $N^*$ resonances in

  - the $p\,\eta$ subsystem, and
  - the $p\,\pi^0$ subsystem.

- **Main physics target:**
  $\gamma\,p \to K^+\,\pi^0\,\Lambda$, with resonance contributions in:
  - the $\Lambda K^+$ system ($N^*$),
  - the $\Lambda \pi^0$ system ($Y^*$),
  - the $K^+ \pi^0$ system ($K^*$).

Current long-term plan:
This research project focuses on developing and applying amplitude models
to analyze data from the GlueX experiment, specifically targeting
$N^*$ and $Y^*$ resonances.

---

> [!WARNING]
> **Scope and physical interpretation**
>
> The amplitude models in this repository are **symbolic, CAS-assisted prototypes**
> developed primarily in an **s-channel decay-amplitude mindset**.
>
> While reactions such as
> $p\,\gamma \to \eta\,\pi^0\,p$ and
> $p\,\gamma \to K^+\,\pi^0\,\Lambda$
> are used as demonstration channels, the current implementations:
>
> - model **sequential s-channel decay chains**,
> - **do not include a realistic treatment of photoproduction dynamics**, such as
>   t-channel (or u-channel) exchange mechanisms, Reggeized exchanges, or energy-dependent
>   production amplitudes,
> - are therefore **not physically realistic descriptions of GlueX photoproduction**,
>   which is dominated by t-channel processes at GlueX energies.
>
> This work should be understood as a **proof-of-concept and technical foundation**
> for automated amplitude construction and visualization, providing a reproducible
> basis for future extensions toward realistic production–decay hybrid models
> and multi-channel hadron-spectroscopy analyses.
