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

# Concepts

```{include} /_snippets/notebook.md
```

## Samples and rate

A {class}`~mypkg.signals.Signal` is two things: its samples, and the rate they were taken at. Everything
else follows from those, such as its duration:

```{code-cell} ipython3
import numpy as np
import mypkg

signal = mypkg.Signal(np.zeros(500), rate=1000.0)
signal.duration
```

## Adding signals

Signals taken at the same rate add sample by sample. Signals taken at different rates can't be added:

```{code-cell} ipython3
:tags: [raises-exception]

mypkg.sine(5, rate=1000.0) + mypkg.sine(5, rate=500.0)
```

## Spectra

A signal's spectrum shows how much of each frequency it holds. For a sine wave of amplitude $A$, the
spectrum peaks at its frequency with height $A$:

```{code-cell} ipython3
freqs, magnitude = mypkg.sine(50, amplitude=2.0).spectrum()
freqs[magnitude.argmax()], magnitude.max()
```
