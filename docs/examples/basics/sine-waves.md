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

# Sine waves

{func}`~mypkg.signals.sine` makes a sine wave of any frequency and amplitude.

```{code-cell} ipython3
import matplotlib.pyplot as plt
import mypkg

fig, ax = plt.subplots(figsize=(6, 3))
for freq in (1, 2, 4):
    mypkg.sine(freq).plot(ax, label=f"{freq} Hz")
ax.legend();
```
