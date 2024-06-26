comments_config = {
    "hypothesis": True,
}
exclude_patterns = [
    "**.ipynb_checkpoints",
    ".DS_Store",
    ".pixi",
    "Thumbs.db",
    "_build",
]
extensions = [
    "myst_nb",
    "sphinx_comments",
    "sphinx_copybutton",
]
html_theme = "sphinx_book_theme"
master_doc = "index"
myst_enable_extensions = [
    "amsmath",
    "colon_fence",
    "dollarmath",
    "html_image",
    "smartquotes",
]
nb_execution_show_tb = True
nb_execution_timeout = -1
nitpicky = True
project = "GlueX N-Star"
