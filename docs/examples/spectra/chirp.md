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

# A chirp

A chirp sweeps through a range of frequencies, so its spectrum is spread across that range.

This page has two plots. The gallery shows the one in the cell tagged `thumbnail`, rather than the
last.

```{code-cell} ipython3
---
tags: [thumbnail]
---
import mypkg

signal = mypkg.chirp(start=1, stop=20, duration=2.0)

signal.plot()
```

```{code-cell} ipython3
signal.plot_spectrum().update_xaxes(range=[0, 40])
```
