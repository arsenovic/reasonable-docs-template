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

# A spectrum

```{include} /_snippets/notebook.md
```

The spectrum of a sum of sines has a peak at each sine's frequency, as tall as its amplitude.

```{code-cell} ipython3
import matplotlib.pyplot as plt
import mypkg

signal = mypkg.sine(50) + mypkg.sine(120, amplitude=0.5)

fig, ax = plt.subplots(figsize=(6, 3))
signal.plot_spectrum(ax)
ax.set_xlim(0, 200);
```
