# List the recipes.
default:
    @just --list

# Build the docs into docs/_build/html, failing on any warning. Notebooks run only when their code changed.
docs:
    uv run --group docs sphinx-build -W --keep-going -b html docs docs/_build/html

# Build the docs, serve them at http://127.0.0.1:8000, and rebuild and reload on every change.
serve:
    uv run --group docs sphinx-autobuild docs docs/_build/html --watch src --ignore "*/jupyter_execute/*"

# Serve the docs in every shibuya-page look at http://127.0.0.1:8000, with a menu to switch, to choose one for conf.py.
looks:
    uv run --group docs python -m shibuya_page.looks docs docs/_build/looks --serve

# Open the guides and examples as notebooks in JupyterLab. Saving writes the .md files.
notebooks:
    JUPYTER_CONFIG_PATH="{{justfile_directory()}}/.jupyter" uv run --group docs jupyter lab --notebook-dir=docs

# Delete the built docs, the generated API pages and the notebooks' cached outputs, so they re-run.
clean:
    rm -rf docs/_build docs/api/generated
