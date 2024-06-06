author = "ComPWA"
exclude_patterns = [
    "**.ipynb_checkpoints",
    ".DS_Store",
    ".pixi",
    "Thumbs.db",
    "_build",
]
extensions = [
    "myst_nb",
    "sphinx.ext.duration",
    "sphinx.ext.doctest",
    "sphinx.ext.autodoc",
    "sphinx.ext.autosummary",
    "sphinx.ext.intersphinx",
]
intersphinx_mapping = {
    "python": ("https://docs.python.org/3/", None),
    "sphinx": ("https://www.sphinx-doc.org/en/master/", None),
}
intersphinx_disabled_domains = ["std"]
templates_path = ["_templates"]
html_theme = "sphinx_rtd_theme"
master_doc = "index"
nitpicky = True
project = "GlueX N-Star"
release = "0.1"
version = "0.1.0"
