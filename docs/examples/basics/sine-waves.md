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

{func}`~mypkg.signals.sine` makes a sine wave of any frequency and amplitude. Each plot is
interactive: hover over a line to read its values, drag to zoom in, and double-click to zoom back out.

```{code-cell} ipython3
import mypkg

fig = mypkg.sine(1).plot(name="1 Hz")
for freq in (2, 4):
    mypkg.sine(freq).plot(fig, name=f"{freq} Hz")
fig
```
