# ee-120-labs
Python virtual labs implemented via the Jupyter Notebook developed for <a href="https://www2.eecs.berkeley.edu/Courses/EE120/">*EE 120: Signals and Systems*</a> at UC Berkeley. 

## About

These labs were developed by the EE 120 course staff in the spring 2019, fall 2019, and spring 2020 semesters. The topics follow our course's content and are listed below. They're ideal for an entry-level upper division course with a focus in signal processing where the students have some prior programming exposure.

We presented these labs at the *2020 International Conference on Higher Education Advances*. The paper is available [here](http://headconf.org/wp-content/uploads/pdfs/11308.pdf).

## Usage

The relevant Jupyter Notebook (.ipynb) file that students complete for Lab N is at `labN/labN.ipynb`. For example, the file for Lab 3 is named `lab3.ipynb`, located in the `lab3` folder. The folder `labN` also contains all resources necessary for that lab to function as intended. Changing the directory structure provided in this repository may cause issues, since the labs expect certain fixed filepaths (e.g., when displaying images inside the notebook, loading data from provided files, or running test cases to provide students with sanity checks on their work).

The versions here are without solutions. If you're an educator at another institution and would like to use these in your course, contact Prof. Babak Ayazifar (ayazifar@berkeley.edu) about acquiring solutions.

## The Labs


| Lab                                                 | Topics        |
| ----------------------------------------------------|---------------|
| **Lab 0:** Scientific Python Tutorial               | <ul><li>Python, NumPy, SciPy, and Matplotlib basics</li><li>Rectangular and exponential signal generation</li></ul>|
| **Lab 1:** Intro to Python for Signals and Systems  | <ul><li>Basics of audio signals (amplitude, phase)</li><li>Convolution</li></ul> |
| **Lab 2:** Applications of LTI Filtering            | <ul><li>1D edge detector</li><li>Simple moving average for denoising</li><li>Exponential moving average of stock data</li></ul> |
| **Lab 3:** Practical Fourier Analysis               | <ul><li>DFT/FFT implementation and analysis</li><li>Virtual oscilloscope calibration via cross-correlation</li></ul> |
| **Lab 4:** Heart Rate Monitoring                    | <ul><li>Spatial averaging of video of human thumb</li><li>Extract heartbeat frequency via FFT</li></ul> |
| **Lab 5:** Deconvolution and Imaging                | <ul><li>1D deconvolution (echo cancellation)</li><li>2D convolution (image blurring and sharpening)</li><li>2D deconvolution (Hubble Space Telescope image deblurring)</li></ul>      |
| **Lab 6:** Control                                  | <ul><li>Satellite stabilization</li><li>Open-loop vs closed-loop control</li><li>Nonlinear control</li></ul>|
| **Lab 7:** Communication                            | <ul><li>Amplitude Modulation</li><li>On-Off Keying</li></ul>|
| **Lab 8:** Shazam                                   | <ul><li>Spectrograms and STFT</li><li>Audio Fingerprinting</li></ul>|
| **Lab 9:** Wavelets                                 | <ul><li>Haar Basis vs DFT Basis</li><li>Implementation via filter banks</li><li> Image/Video Compression via Wavelets</li></ul>|
