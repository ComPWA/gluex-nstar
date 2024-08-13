import os

author = "ComPWA"
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
html_logo = (
    "https://raw.githubusercontent.com/ComPWA/ComPWA/04e5199/doc/images/logo.svg"
)
html_favicon = "_static/favicon.ico"
html_theme = "sphinx_book_theme"
html_theme_options = {
    "announcement": "This repository is under active development.",
    "launch_buttons": {
        "binderhub_url": "https://mybinder.org",
        "colab_url": "https://colab.research.google.com",
        "deepnote_url": "https://deepnote.com",
        "notebook_interface": "jupyterlab",
    },
    "path_to_docs": "docs",
    "repository_branch": "main",
    "repository_url": "https://github.com/ComPWA/gluex-nstar",
    "show_navbar_depth": 2,
    "show_toc_level": 2,
    "use_download_button": False,
    "use_edit_page_button": True,
    "use_issues_button": True,
    "use_repository_button": True,
    "use_source_button": True,
}
html_title = "GlueX Symbolic N* Amplitudes"
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
