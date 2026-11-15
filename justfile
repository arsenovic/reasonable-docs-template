# List the recipes.
default:
    @just --list

# Build the docs into docs/_build/html, failing on any warning; `just docs scipy` overrides conf.py's look.
docs look="":
    uv run --group docs sphinx-build -W --keep-going -b html {{ if look != "" { "-D html_theme_options.look=" + look } else { "" } }} docs docs/_build/html

# Serve the docs at http://127.0.0.1:8000, rebuilding on every change; `just serve scipy` overrides the look.
serve look="":
    uv run --group docs sphinx-autobuild docs docs/_build/html --watch src --ignore "*/jupyter_execute/*" {{ if look != "" { "-D html_theme_options.look=" + look } else { "" } }}

# Open the guides and examples as notebooks in JupyterLab. Saving writes the .md files.
notebooks:
    JUPYTER_CONFIG_PATH="{{justfile_directory()}}/.jupyter" uv run --group docs jupyter lab --notebook-dir=docs

# Delete the built docs, the generated API pages and the notebooks' cached outputs, so they re-run.
clean:
    rm -rf docs/_build docs/api/generated
