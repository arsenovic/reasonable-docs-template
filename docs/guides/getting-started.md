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

# Getting started

## Install

```sh
pip install mypkg
```

## Make a signal

```{note}
Every page under Guides and Examples is a notebook: the Download link at the top gets it, and
`just notebooks` opens it in JupyterLab.
```

A signal is a set of samples taken at a fixed rate. {func}`~mypkg.signals.sine` makes a sine wave:

```{code-cell} ipython3
import mypkg

signal = mypkg.sine(freq=3, duration=1.0)
signal
```

## Plot it

```{code-cell} ipython3
signal.plot();
```

Next, {doc}`concepts` explains what a {class}`~mypkg.signals.Signal` holds.
