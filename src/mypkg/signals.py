"""Signals sampled at a fixed rate."""

from dataclasses import dataclass

import numpy as np


@dataclass
class Signal:
    """Samples of a signal, taken at a fixed rate.

    Parameters
    ----------
    samples : numpy.ndarray
        The signal's values.
    rate : float
        Samples per second.

    Examples
    --------
    >>> s = Signal(np.zeros(8), rate=4.0)
    >>> s.duration
    2.0
    """

    samples: np.ndarray
    rate: float

    def __repr__(self) -> str:
        return f"Signal({len(self.samples)} samples at {self.rate:g} Hz)"

    @property
    def duration(self) -> float:
        """Length of the signal, in seconds."""
        return len(self.samples) / self.rate

    @property
    def time(self) -> np.ndarray:
        """The time of each sample, in seconds."""
        return np.arange(len(self.samples)) / self.rate

    def __add__(self, other: "Signal") -> "Signal":
        """Add two signals sampled at the same rate."""
        if other.rate != self.rate:
            raise ValueError("signals must share a sample rate")
        return Signal(self.samples + other.samples, self.rate)

    def spectrum(self) -> tuple[np.ndarray, np.ndarray]:
        """The signal's magnitude spectrum.

        Returns
        -------
        freqs : numpy.ndarray
            Frequencies, in Hz, from 0 to half the sample rate.
        magnitude : numpy.ndarray
            The magnitude at each frequency, scaled so a unit sine peaks at 1.
        """
        magnitude = np.abs(np.fft.rfft(self.samples)) * 2 / len(self.samples)
        return np.fft.rfftfreq(len(self.samples), 1 / self.rate), magnitude

    def plot(self, fig=None, **kwargs):
        """Plot the signal against time, as an interactive plotly figure.

        Parameters
        ----------
        fig : plotly.graph_objects.Figure, optional
            A figure to add the signal to; by default, a new one.
        **kwargs
            Passed to :class:`plotly.graph_objects.Scatter`, such as ``name``.

        Returns
        -------
        plotly.graph_objects.Figure
        """
        fig = _figure(fig)
        fig.add_scatter(x=self.time, y=self.samples, mode="lines", **kwargs)
        fig.update_xaxes(title="time (s)")
        return fig

    def plot_spectrum(self, fig=None, **kwargs):
        """Plot the signal's magnitude spectrum, from :meth:`spectrum`.

        Parameters
        ----------
        fig : plotly.graph_objects.Figure, optional
            A figure to add the spectrum to; by default, a new one.
        **kwargs
            Passed to :class:`plotly.graph_objects.Scatter`, such as ``name``.

        Returns
        -------
        plotly.graph_objects.Figure
        """
        fig = _figure(fig)
        freqs, magnitude = self.spectrum()
        fig.add_scatter(x=freqs, y=magnitude, mode="lines", **kwargs)
        fig.update_xaxes(title="frequency (Hz)")
        return fig


def _figure(fig=None):
    """The figure to plot on: `fig`, or a new one sized for a page."""
    if fig is not None:
        return fig
    import plotly.graph_objects as go

    return go.Figure(layout={"height": 350, "margin": {"l": 50, "r": 20, "t": 20, "b": 50}})


def sine(freq: float, duration: float = 1.0, rate: float = 1000.0, amplitude: float = 1.0) -> Signal:
    """A sine wave.

    Parameters
    ----------
    freq : float
        Frequency, in Hz.
    duration : float
        Length, in seconds.
    rate : float
        Samples per second.
    amplitude : float
        Peak value.

    Returns
    -------
    Signal
    """
    t = np.arange(int(duration * rate)) / rate
    return Signal(amplitude * np.sin(2 * np.pi * freq * t), rate)


def chirp(start: float, stop: float, duration: float = 1.0, rate: float = 1000.0) -> Signal:
    """A sine wave whose frequency sweeps linearly from `start` to `stop`.

    Parameters
    ----------
    start, stop : float
        Frequencies at the beginning and end, in Hz.
    duration : float
        Length, in seconds.
    rate : float
        Samples per second.

    Returns
    -------
    Signal
    """
    t = np.arange(int(duration * rate)) / rate
    phase = 2 * np.pi * (start * t + (stop - start) * t**2 / (2 * duration))
    return Signal(np.sin(phase), rate)
