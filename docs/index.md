# mypkg *— sampled signals, and their spectra*

```{important}
**This is a template project.** mypkg is a stand-in package, and these docs show what
[reasonable-docs-template](https://github.com/arsenovic/reasonable-docs-template) sets up: guides, a
gallery of examples, an API reference and project pages. To start your own, copy the template and
follow its [README](https://github.com/arsenovic/reasonable-docs-template#readme).
```

**mypkg** is an open-source, BSD-licensed Python package for sampled signals. It makes sine waves
and chirps, adds them together, and plots them and their spectra as interactive figures.

## Getting started

::::{container} sp-side-by-side

:::{container}
Plot the spectrum of two sine waves, in **3 lines**.

```python
from mypkg import sine
signal = sine(5) + sine(12, amplitude=0.5)
signal.plot_spectrum()
```

Install it with pip, then read {doc}`guides/getting-started`.

```sh
python -m pip install "mypkg[plot]"
```
:::

```{image} _static/spectrum.svg
:alt: The spectrum of two sine waves, with peaks at 5 Hz and 12 Hz
```

::::

## [Some examples](examples/index.md)

```{gallery}
:links-only:

examples/basics/sine-waves
examples/basics/adding-signals
examples/spectra/chirp
```

## Features

{.sp-features}
- Signals
  - sine waves and chirps
  - adding signals together
- Analysis
  - magnitude spectra
- Plotting
  - interactive plots, with plotly
  - signals against time
  - spectra against frequency

## Questions or comments?

Ask, report a bug, or suggest a feature on
[GitHub](https://github.com/arsenovic/reasonable-docs-template/issues). To help, see
{doc}`project/contributing`.

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
