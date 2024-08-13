import os

ORGANIZATION = "ComPWA"
REPO_NAME = "gluex-nstar"

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
    "https://github.com/user-attachments/assets/5650480b-8bed-4fb2-9f2b-c43b12e16ac3"
)
html_favicon = "_static/favicon.ico"
html_theme = "sphinx_book_theme"
html_theme_options = {
    "announcement": "⚠️ This repository is under active development ⚠️",
    "icon_links": [
        {
            "name": "Common Partial Wave Analysis",
            "url": "https://compwa.github.io",
            "icon": "_static/favicon.ico",
            "type": "local",
        },
        {
            "name": "GitHub",
            "url": f"https://github.com/{ORGANIZATION}/{REPO_NAME}",
            "icon": "fa-brands fa-github",
        },
        {
            "name": "Launch on Binder",
            "url": f"https://mybinder.org/v2/gh/{ORGANIZATION}/{REPO_NAME}/main?filepath=docs",
            "icon": "https://mybinder.readthedocs.io/en/latest/_static/favicon.png",
            "type": "url",
        },
        {
            "name": "Launch on Colaboratory",
            "url": f"https://colab.research.google.com/github/{ORGANIZATION}/{REPO_NAME}/blob/main",
            "icon": "https://avatars.githubusercontent.com/u/33467679?s=100",
            "type": "url",
        },
    ],
    "launch_buttons": {
        "binderhub_url": "https://mybinder.org",
        "colab_url": "https://colab.research.google.com",
        "deepnote_url": "https://deepnote.com",
        "notebook_interface": "jupyterlab",
    },
    "logo": {"text": "Symbolic Amplitudes<br>for Light Baryons"},
    "path_to_docs": "docs",
    "repository_branch": "main",
    "repository_url": f"https://github.com/{ORGANIZATION}/{REPO_NAME}",
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
