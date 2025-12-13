
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import matplotlib.mlab as mlab
from scipy import signal
from pyyeti import psd
import endaq as endaq
from endaq import *


# Load CSV data from the raw csv file
acceldata = pd.read_csv('RAWDATA - Waveform.csv', usecols=['FrontAxle_Left Front (Max) (G)'])
data = acceldata.values.flatten()  # Convert to 1D array
sample_rate = 2000 
bin_width = 1  # desired bin width in Hz

# define the number frequencies to split the psd data into, then run the psd function
# nfreq = 102
nperseg = sample_rate / bin_width
f, s= signal.welch(data, sample_rate, nperseg=int(nperseg))
fdata = pd.DataFrame(f)

#get the already processed psd data, flatten it into arrays
psd_processed = pd.read_csv('PSD - Power Spectral Density_Front_Axle.csv', usecols=['FrontAxle_Left Front (G²/Hz)']).values.flatten()
freqs = pd.read_csv('PSD - Power Spectral Density_Front_Axle.csv', usecols=['Frequency (Hz)']).values.flatten()

#convert the psd to octave format 
s_octave, f_octave, msv, ms = psd.rescale(s, f, n_oct=12)
# endaq_oct = endaq.calc.psd.to_octave(fdata, fstart=1, octave_bins=12)
# octarray = endaq_oct.values.flatten()
# print(octarray)
#plot the psd data
plt.loglog(f, s, label='Python Manipulated PSD')
plt.loglog(freqs, psd_processed, label='Already Processed PSD')
plt.loglog(f_octave, s_octave, label='Pysci Octave PSD')
# plt.loglog(octarray, s_octave, label='Endaq Octave PSD')
plt.legend()
plt.xlim([0, 1000])
plt.xlabel('frequency [Hz]')
plt.ylabel('PSD [G^2/Hz]')
plt.show()



