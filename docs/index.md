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

## Guides

Start with {doc}`guides/getting-started`, then read {doc}`guides/concepts`.

## [Examples](examples/index.md)

Short notebooks, each showing one thing mypkg does, in a gallery.

## [API](api/index.md)

Every module, class and function, from their docstrings.

```{toctree}
:caption: Guides
:hidden:

Overview <self>
guides/getting-started
guides/concepts
```

```{toctree}
:caption: Examples
:hidden:

examples/index
examples/running
```

```{toctree}
:caption: API
:hidden:

api/generated/mypkg.signals
```

```{toctree}
:caption: Project
:hidden:

project/contributing
project/about
project/license
```
