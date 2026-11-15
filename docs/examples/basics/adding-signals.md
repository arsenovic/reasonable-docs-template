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

# Adding signals

```{include} /_snippets/notebook.md
```

Signals sampled at the same rate add sample by sample, so a sum of sines is one line.

```{code-cell} ipython3
import matplotlib.pyplot as plt
import mypkg

parts = [mypkg.sine(3), mypkg.sine(7, amplitude=0.5), mypkg.sine(13, amplitude=0.25)]
total = sum(parts[1:], parts[0])

fig, ax = plt.subplots(figsize=(6, 3))
total.plot(ax, color="black");
```
