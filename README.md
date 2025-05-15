# DFT-FFT

A Python application that demonstrates and compares the Discrete Fourier Transform (DFT) and the Fast Fourier Transform (FFT) on audio signals. Load an audio file, visualize its waveform, compute both transforms, and explore the resulting spectra in an interactive GUI.

---

## Features

- **Audio I/O**  
  Load WAV (or other) audio files and inspect the raw waveform.  
- **Transform Algorithms**  
  - **Naïve DFT** (O(N²)) implementation  
  - **Cooley–Tukey FFT** (O(N log N)) implementation  
- **Spectral Visualization**  
  View amplitude and phase spectra of the loaded signal.  
- **Interactive GUI**  
  - Play/pause audio  
  - Choose between DFT and FFT  
  - Zoom and pan on time-domain and frequency-domain plots  

---

## Getting Started

### Prerequisites

- Python 3.6 or newer  
- [NumPy](https://numpy.org/)  
- [SciPy](https://scipy.org/)  
- [Matplotlib](https://matplotlib.org/)  
- [PyQt5](https://pypi.org/project/PyQt5/) (or PySide2/PySide6)

Install dependencies:

```bash
pip install numpy scipy matplotlib PyQt5
