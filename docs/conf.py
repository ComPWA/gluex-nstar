import os

from sphinx_api_relink.helpers import get_branch_name

BRANCH = get_branch_name()
ORGANIZATION = "ComPWA"
REPO_NAME = "gluex-nstar"
REPO_TITLE = "GlueX N-Star Documentation"

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
    "sphinx_api_relink",
    "sphinx_comments",
    "sphinx_copybutton",
]
html_logo = (
    "https://raw.githubusercontent.com/ComPWA/ComPWA/04e5199/doc/images/logo.svg"
)
html_theme = "sphinx_book_theme"
html_theme_options = {
    "path_to_docs": "docs",
    "repository_branch": BRANCH,
    "repository_url": f"https://github.com/{ORGANIZATION}/{REPO_NAME}",
    "show_navbar_depth": 2,
    "show_toc_level": 2,
    "use_download_button": True,
    "use_edit_page_button": True,
    "use_issues_button": True,
    "use_repository_button": True,
    "use_source_button": True,
}
html_title = REPO_TITLE
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
