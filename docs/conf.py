# Sphinx configuration: https://www.sphinx-doc.org/en/master/usage/configuration.html

import os

import mypkg
from plotly.offline import get_plotlyjs_version

# -- Project ------------------------------------------------------------------

project = "mypkg"
author = "The mypkg developers"
copyright = f"2026, {author}"
release = mypkg.__version__
html_title = project

# The repository, for the header's GitHub icon and link.
repository = "https://github.com/arsenovic/reasonable-docs-template"

# -- Extensions ---------------------------------------------------------------

extensions = [
    "myst_nb",                   # Markdown pages, and MyST (jupytext) notebooks, run during the build
    "sphinx.ext.autodoc",        # API pages from docstrings
    "sphinx.ext.autosummary",    # ... one per module, class and function
    "sphinx.ext.napoleon",       # NumPy-style docstrings
    "sphinx.ext.mathjax",        # $math$
    "sphinx.ext.viewcode",       # [source] links to highlighted code
    "sphinx.ext.intersphinx",    # links to Python's, NumPy's and plotly's docs
    "sphinx_codeautolink",       # names in code blocks and cells link to their API pages
    "sphinx_copybutton",         # a copy button on code blocks
    "shibuya_page.gallery",      # the examples' thumbnail gallery
]

exclude_patterns = ["_build", "**.ipynb_checkpoints", "jupyter_execute"]
# A reference that doesn't resolve is an error, so a renamed function can't leave a dead link.
nitpicky = True
templates_path = ["_templates"]

# -- MyST and notebooks -------------------------------------------------------

myst_enable_extensions = ["colon_fence", "dollarmath", "attrs_block", "attrs_inline"]
myst_heading_anchors = 3

# Notebooks run during the build, and again only when their code changes.
nb_execution_mode = "cache"
nb_execution_timeout = 120
# A cell that fails fails the build; tag a cell raises-exception when it's meant to.
nb_execution_raise_on_error = True
nb_merge_streams = True

# Plotly figures show as interactive HTML, which needs plotly.js on the page (setup, below), and
# carry a PNG too, which the gallery uses for their cards. The notebooks' kernel reads this setting.
os.environ["PLOTLY_RENDERER"] = "sphinx_gallery+png"

# -- API reference ------------------------------------------------------------

autosummary_generate = True
autodoc_typehints = "description"
autodoc_member_order = "bysource"
napoleon_google_docstring = False
napoleon_use_rtype = False
# Types such as "float, optional" link the type and leave "optional" as plain text.
napoleon_preprocess_types = True

intersphinx_mapping = {
    "python": ("https://docs.python.org/3", None),
    "numpy": ("https://numpy.org/doc/stable", None),
    "plotly": ("https://plotly.com/python-api-reference", None),
}

# Link names in code cells; a cell that isn't valid Python just goes unlinked.
codeautolink_concat_default = True
suppress_warnings = ["codeautolink.parse_block", "codeautolink.match_block"]

# Copy code without its prompts.
copybutton_prompt_text = r">>> |\.\.\. |\$ |In \[\d*\]: "
copybutton_prompt_is_regexp = True

# -- HTML ---------------------------------------------------------------------

html_theme = "shibuya-page"
html_static_path = ["_static"]
html_css_files = ["mypkg.css"]
html_favicon = "_static/logo.svg"

html_theme_options = {
    # shibuya-page's own options (see its README).
    "look": "rtd",
    "prune_page_headings": True,
    "external_links_new_tab": True,
    "download_notebooks": True,
    # Notebook pages link to this page, as Run, beside Download.
    "run_notebooks": "examples/running",
    # Shibuya's options: https://shibuya.lepture.com/customisation/
    "accent_color": "blue",
    "light_logo": "_static/logo.svg",
    "dark_logo": "_static/logo.svg",
    "github_url": repository,
    "nav_links": [
        {"title": "Guides", "url": "guides/getting-started"},
        {"title": "Examples", "url": "examples/index"},
        {"title": "API", "url": "api/index"},
        {"title": "GitHub", "url": repository, "external": True},
    ],
    # The sidebar shows three levels, so a section's pages under its headings (Examples > Basics >
    # Sine waves); prune_page_headings leaves out headings that hold no pages.
    "toctree_collapse": True,
    "toctree_maxdepth": 3,
    "toctree_titles_only": False,
    "show_ai_links": False,
}


# -- Plotly ---------------------------------------------------------------------


def add_plotlyjs(app, pagename, templatename, context, doctree):
    """Load plotly.js on the pages with a plotly figure."""
    if "plotly-graph-div" in context.get("body", ""):
        app.add_js_file(f"https://cdn.plot.ly/plotly-{get_plotlyjs_version()}.min.js")


def setup(app):
    app.connect("html-page-context", add_plotlyjs)
