# reasonable-docs-template

A starting point for a Python package's docs: guides, a gallery of examples, and an API reference,
built with [Sphinx](https://www.sphinx-doc.org/) and the
[shibuya-page](https://github.com/arsenovic/shibuya-page) theme.

- Guides and examples are notebooks, written as MyST Markdown (`.md`) so they diff and review like
  text. They run during the build, and again only when their code changes.
- Examples are a gallery: each card shows the plot its notebook draws.
- The API reference comes from docstrings, one page per module, class and function.
- Names in code link to their API pages, and a broken reference fails the build.

## Use it

1. Click **Use this template** on GitHub, or copy this folder.
2. Replace `src/mypkg` with your package, and rename `mypkg` in `pyproject.toml`, `docs/conf.py`
   and `docs/api/index.md`.
3. In `docs/conf.py`, set `project`, `author` and `repository`. Replace `docs/_static/logo.svg`.
   Choose a look with `just looks`, and set it as `look` in `docs/conf.py`.
4. Replace the pages in `docs/guides` and `docs/examples` with your own.

## Recipes

Needs [uv](https://docs.astral.sh/uv/) and [just](https://just.systems/).

| Recipe           | Does |
| ---------------- | ---- |
| `just docs`      | Builds the docs into `docs/_build/html`, failing on any warning. |
| `just serve`     | Serves the docs at http://127.0.0.1:8000, rebuilding and reloading on every change. |
| `just looks`     | Serves the docs in every look, with a menu in the corner to switch, so you can choose one for `conf.py`. |
| `just notebooks` | Opens the guides and examples as notebooks in JupyterLab. Saving writes the `.md` files. |
| `just clean`     | Deletes the built docs, the generated API pages, and the notebooks' cached outputs. |

## Layout

```
docs/
  conf.py           Sphinx settings, commented
  index.md          the home page; its hidden toctrees make the sidebar's Guides, Examples and API
                    captions, listing the pages themselves
  guides/           read in order; add each to the Guides toctree in index.md
  examples/         index.md is the gallery, a section per folder; running.md explains running them
  api/index.md      the API tab's table of modules; autosummary writes api/generated/, and each
                    module goes in the API toctree in index.md
  _templates/       autosummary's page templates for modules and classes
  _static/          the logo, and mypkg.css for your own styles
src/mypkg/          the package being documented
.jupyter/           makes `just notebooks` open .md files as notebooks
```

## Write a notebook

A notebook is a Markdown file that starts with a jupytext header, with code in `code-cell` blocks:

````markdown
---
jupytext:
  text_representation:
    extension: .md
    format_name: myst
kernelspec:
  display_name: Python 3
  language: python
  name: python3
---

# A title

Some text.

```{code-cell} ipython3
import mypkg
mypkg.sine(5).plot()
```
````

Each notebook page gets **Run** and **Download** links at the top right: Run opens
`examples/running.md`, which explains how readers can run the notebooks (the `run_notebooks` option
in `docs/conf.py`), and Download saves the page's `.md` file.

Edit a notebook as text, or in JupyterLab with `just notebooks`. A cell that raises fails the build, unless
it's tagged `raises-exception`.

The build caches each notebook's outputs, and re-runs a notebook only when its code changes, not when
your package does. After changing the package, `just clean` makes the next build re-run them all.

A new example goes in a section folder under `docs/examples/`, and appears in that section's gallery.
Its card shows the notebook's last plot. To choose another, tag a cell `thumbnail`, or set
`thumbnail: path/to/image.png` in the front matter.

## Plots

mypkg plots with [plotly](https://plotly.com/python/), so plots in the docs are interactive: they
zoom, pan, and show values on hover. `docs/conf.py` sets the notebooks' kernel to draw each plotly
figure twice, as HTML for the page and as a PNG for the gallery's card, and loads plotly.js on the
pages that have a plot. The PNGs come from [kaleido](https://github.com/plotly/Kaleido), which
needs Chrome; `uv run --group docs plotly_get_chrome` installs one if you don't have it.

## Publish

[.github/workflows/docs.yml](.github/workflows/docs.yml) builds the docs on every push and pull
request, and publishes them on GitHub Pages from `main`. Turn Pages on first: **Settings > Pages >
Source: GitHub Actions**.
