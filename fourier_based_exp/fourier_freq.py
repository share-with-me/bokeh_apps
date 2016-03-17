import numpy as np
import scipy
import scipy.signal
import pandas as pd 
import matplotlib.pyplot as plt
from bokeh.plotting import figure, show, gridplot, hplot, vplot
import bokeh.charts
from bokeh.io import output_file
import bokeh.charts.utils
import bokeh.models
import bokeh.palettes
import bokeh.plotting
#Now some technicalities with respect to fourier transform. A signal can be thought of composed of sum of sine waves of different frquencies.
#A signal can be represented by the magnitude that ech frequency contributes to total signal.
#These magnitudes are called as Fourier Coefficients.
#We now plot Fourier Coefficients versus frequency. We will use fast fourier transform FFT implemented in numpy and scipy.

data = pd.read_csv('data.csv' , comment = '#' , names = ['t(ms)', 'V(microV)'])


#Conversion to seconds
data['t(ms)']/=1000
#Renaming the column name now
data = data.rename(columns = {'t(ms)':'t(s)'})

plot = bokeh.charts.Line(data.loc[5000:25000,:],x = 't(s)', y =  'V(microV)', color = "blue")
#1. Determine the frequencies asscoiates through fourier coeffiecients
sampling_freq = 25000
# Determine frequencies
f = np.fft.fftfreq(len(data)) * sampling_freq

# Compute power spectral density
psd = np.abs(np.fft.fft(data['V(microV)'].values))**2 / (len(data)/10000)

# Make plot
plt.plot(f, psd)
plt.xlabel('freq (Hz)')
plt.ylabel('PSD')
plt.margins(0.02)

# Compute Nyquist frequency
nyquist_freq = sampling_freq / 2

# Design a butterworth filter
b, a = scipy.signal.butter(3, 100 / nyquist_freq, btype='high')

# Get frequency response curve
w, h = scipy.signal.freqz(b, a, worN=2000)

# Make plot
plt.semilogx((nyquist_freq / np.pi) * w, abs(h))
plt.xlabel('freq. (Hz)')
plt.ylabel('response')
plt.margins(0.02)

