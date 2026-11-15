# Contributing

Bug reports, ideas and pull requests are welcome, on
[GitHub](https://github.com/arsenovic/reasonable-docs-template).

## Set up

You need [uv](https://docs.astral.sh/uv/) and [just](https://just.systems/). Clone the repository,
and the recipes install everything else the first time they run:

```sh
git clone https://github.com/arsenovic/reasonable-docs-template
cd reasonable-docs-template
just serve
```

## Work on the docs

| Recipe           | Does |
| ---------------- | ---- |
| `just serve`     | Serves the docs at <http://127.0.0.1:8000>, rebuilding and reloading on every change. |
| `just docs`      | Builds the docs, failing on any warning, as the CI does. |
| `just notebooks` | Opens the guides and examples as notebooks in JupyterLab. Saving writes the `.md` files. |
| `just looks`     | Serves the docs in every look of the theme, to compare them. |
| `just clean`     | Deletes the build, so the notebooks run again. |

Guides and examples are notebooks saved as Markdown: {ref}`running-the-examples` explains how to
open them. A new example goes in a folder under `docs/examples/`, and appears in that folder's
gallery.

## Pull requests

- Run `just docs` first: a broken reference, or a cell that raises, fails the build.
- Keep each pull request to one change, with a message that says what it does and why.
