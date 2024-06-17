project = "GlueX-Nstar"
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
    "sphinx.ext.napoleon",
    "sphinx.ext.viewcode",
]
html_theme = "sphinx_book_theme"
master_doc = "index"
myst_enable_extensions = [
    "colon_fence",
    "deflist",
    "dollarmath",
    "html_admonition",
    "html_image",
    "linkify",
    "substitution",
    "tasklist",
]

nb_execution_mode = "auto"
nitpicky = True
version = "0.1.0"
