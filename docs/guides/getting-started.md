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
pip install "mypkg[plot]"
```

## Make a signal

A signal is a set of samples taken at a fixed rate. {func}`~mypkg.signals.sine` makes a sine wave:

```{code-cell} ipython3
import mypkg

signal = mypkg.sine(freq=3, duration=1.0)
signal
```

## Plot it

{meth}`~mypkg.signals.Signal.plot` draws it with [plotly](https://plotly.com/python/), so you can
zoom in and hover over it to read its values:

```{code-cell} ipython3
signal.plot()
```

Next, {doc}`concepts` explains what a {class}`~mypkg.signals.Signal` holds.
