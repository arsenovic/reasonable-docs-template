# mypkg *— sampled signals, and their spectra*

mypkg makes signals, adds them up, and plots them and their spectra. It's a stand-in: replace it with
your own package, and these pages with your own.

```python
import mypkg

signal = mypkg.sine(5) + mypkg.sine(12, amplitude=0.5)
signal.plot_spectrum()
```

## Features

{.sp-features}
- Signals
  - sine waves and chirps
  - adding signals together
- Analysis
  - magnitude spectra
- Plotting
  - signals against time
  - spectra against frequency

## [Guides](guides/index.md)

Start with {doc}`guides/getting-started`, then read {doc}`guides/concepts`.

## [Examples](examples/index.md)

Short notebooks, each showing one thing mypkg does.

## [API](api/index.md)

Every module, class and function, from their docstrings.

```{toctree}
:hidden:

guides/index
examples/index
api/index
```
