import os

comments_config = {
    "hypothesis": True,
}
exclude_patterns = [
    "_build",
    ".DS_Store",
    ".pixi",
    ".virtual_documents",
    "**.ipynb_checkpoints",
    "Thumbs.db",
]
extensions = [
    "myst_nb",
    "sphinx_comments",
    "sphinx_copybutton",
]
html_theme = "sphinx_book_theme"
html_theme_options = {
    "collapse_navigation": False,
}
master_doc = "index"
myst_enable_extensions = [
    "amsmath",
    "colon_fence",
    "dollarmath",
    "html_image",
    "smartquotes",
]
nb_execution_mode = "cache" if os.environ.get("EXECUTE_NB") else "off"
nb_execution_show_tb = True
nb_execution_timeout = -1
nb_render_markdown_format = "myst"
nitpicky = True
project = "GlueX N-Star"
