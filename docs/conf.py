# outline for a myst_nb project with sphinx
# build with: sphinx-build -nW --keep-going -b html . ./_build/html

# load extensions
extensions = ["myst_nb"]

# specify project details
master_doc = "index"
project = "GlueX N-Star"

# basic build settings
exclude_patterns = [
    ".pixi",
    "_build",
    "Thumbs.db",
    ".DS_Store",
    "**.ipynb_checkpoints",
]
nitpicky = True
