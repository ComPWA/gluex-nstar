from qrules.particle import Particle, ParticleCollection, Spin

from gluex_nstar import create_pgamma, generate_markdown_table, load_particle_database


def test_create_pgamma() -> None:
    mass = 4.1

    spin_half, spin_three_half = create_pgamma(mass)

    assert spin_half.name == "pgamma1"
    assert spin_half.spin == 0.5
    assert spin_half.mass == mass
    assert spin_half.isospin == Spin(0.5, 0.5)
    assert spin_half.charge == 1
    assert spin_half.baryon_number == 1
    assert spin_half.parity == -1
    assert spin_half.pid == 99990
    assert spin_three_half.name == "pgamma2"
    assert spin_three_half.spin == 1.5
    assert spin_three_half.mass == mass
    assert spin_three_half.pid == 99991


def test_load_particle_database() -> None:
    particle_db = load_particle_database()

    additional_particles = {
        "N(1875)+",
        "N(1880)+",
        "N(1895)+",
        "N(1900)+",
        "N(2060)+",
    }
    assert additional_particles <= set(particle_db.names)
    assert particle_db["N(1875)+"].pid == 200002
    assert particle_db["N(2060)+"].spin == 2.5


def test_generate_markdown_table() -> None:
    particle = Particle(
        name="test",
        pid=1,
        latex="T",
        spin=0.5,
        mass=1.25,
        width=0.5,
        charge=1,
        isospin=Spin(0.5, 0.5),
        baryon_number=1,
        parity=-1,
    )
    particle_db = ParticleCollection([particle])

    table = generate_markdown_table(particle_db, ["test"])

    assert "| Particle | Name | PID |" in table
    assert (
        R"| $T$ | `test` | 1 | $\frac{1}{2}^{- } \; (\frac{1}{2}^{ })$ | $\frac{1}{2}$ | 1.25 | 0.5 | 1 | 0 | 1 |"
        in table
    )
