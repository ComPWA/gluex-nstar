"""Particle definitions and presentation helpers."""

from collections.abc import Iterable
from fractions import Fraction
from importlib.resources import as_file, files
from textwrap import dedent

import qrules.io
from qrules.particle import (
    Particle,
    ParticleCollection,
    Spin,
    create_particle,
    load_pdg,
)


def create_pgamma(mass: float) -> tuple[Particle, Particle]:
    """Create the spin-1/2 and spin-3/2 virtual p-gamma states."""
    spin_half = Particle(
        name="pgamma1",
        latex=r"p\gamma (s1/2)",
        spin=0.5,
        mass=mass,
        charge=1,
        isospin=Spin(1 / 2, +1 / 2),
        baryon_number=1,
        parity=-1,
        pid=99990,
    )
    spin_three_half = create_particle(
        template_particle=spin_half,
        name="pgamma2",
        latex=R"p\gamma (s3/2)",
        spin=1.5,
        pid=spin_half.pid + 1,
    )
    return spin_half, spin_three_half


def load_particle_database() -> ParticleCollection:
    """Load the PDG database and the additional N-star definitions."""
    particle_db = load_pdg()
    resource = files("gluex_nstar").joinpath("additional-particles.yml")
    with as_file(resource) as path:
        additional_particles = qrules.io.load(path)
    particle_db.update(additional_particles)
    return particle_db


def generate_markdown_table(
    particle_db: ParticleCollection,
    particles: Iterable[str],
) -> str:
    """Render selected particle definitions as a Markdown table."""
    src = dedent(r"""
    | Particle | Name | PID | $J^{PC} (I^G)$ | $I_3$ | $M$ | $\Gamma$ | $Q$ | $S$ | $B$ |
    | :------- |------|-----|----------------|-------|-----|----------|-----|-----|-----|
    """)
    for name in particles:
        particle = particle_db[name]
        src += (
            f"| ${particle.latex}$ | `{particle.name}` | {particle.pid} | "
            f"{_jpc_ig(particle)} | {_i_3(particle)} | {particle.mass:.3g} | "
            f"{particle.width:g} | {particle.charge} | {particle.strangeness} | "
            f"{particle.baryon_number} |\n"
        )
    return src


def _jpc_ig(particle: Particle) -> str:
    spin = _format_fraction(particle.spin)
    parity = _format_parity(particle.parity)
    c_parity = _format_parity(particle.c_parity)
    if particle.isospin is None:
        return f"${spin}^{{{parity}{c_parity}}}$"
    isospin = _format_fraction(particle.isospin.magnitude)
    g_parity = _format_parity(particle.g_parity)
    return rf"${spin}^{{{parity}{c_parity}}} \; ({isospin}^{{{g_parity}}})$"


def _i_3(particle: Particle) -> str:
    if particle.isospin is None:
        return "N/A"
    return f"${_format_fraction(particle.isospin.projection)}$"


def _format_fraction(value: float) -> str:
    fraction = Fraction(value)
    if fraction.denominator == 1:
        return str(fraction.numerator)
    return rf"\frac{{{fraction.numerator}}}{{{fraction.denominator}}}"


def _format_parity(parity: int | None) -> str:
    if parity is None:
        return " "
    if parity == -1:
        return "-"
    if parity == 1:
        return "+"
    raise NotImplementedError
