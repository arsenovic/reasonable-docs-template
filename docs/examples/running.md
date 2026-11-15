(running-the-examples)=
# Running the examples

Every example, and every guide, is a notebook, saved as a Markdown file (MyST, read by
[jupytext](https://jupytext.readthedocs.io/)) so it's easy to read and review as text.

## From a copy of the repository

With [uv](https://docs.astral.sh/uv/) and [just](https://just.systems/) installed:

```sh
git clone https://github.com/you/mypkg
cd mypkg
just notebooks
```

`just notebooks` installs the docs' dependencies, mypkg among them, and opens JupyterLab in `docs/`,
where each `.md` file opens as a notebook. Open one from `examples/` or `guides/`, and run its cells
with {kbd}`Shift+Enter`, or all of them from the **Run** menu. Saving writes the notebook back to its
`.md` file, outputs left out, so your changes show up in `git diff` as text.

## From a downloaded page

The **Download** link at the top of each notebook page saves its `.md` file. To run it without the
repository:

```sh
pip install mypkg matplotlib jupyterlab jupytext
jupyter lab
```

In JupyterLab, right-click the file and choose **Open With > Jupytext Notebook**.
