import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import matplotlib.mlab as mlab
import scipy.signal
from scipy.signal import welch


# Load CSV data from the raw csv file
acceldata = pd.read_csv('RAWDATA - Waveform.csv', usecols=['FrontAxle_Left Front (Max) (G)'])
data = acceldata.values.flatten()  # Convert to 1D array
sample_rate = 2000  # samples per second 

# define the number frequencies to split the psd data into, then run the psd function
nfreq = 102
nperseg = nfreq * 2
(f, S)= scipy.signal.welch(data, sample_rate, nperseg=nperseg)

#get the already processed psd data, flatten it into arrays
psd = pd.read_csv('PSD - Power Spectral Density_Front_Axle.csv', usecols=['FrontAxle_Left Front (G²/Hz)']).values.flatten()
freqs = pd.read_csv('PSD - Power Spectral Density_Front_Axle.csv', usecols=['Frequency (Hz)']).values.flatten()

#plot the psd data
print(len(freqs)), print(len(f))
plt.loglog(f, S, label='Python Manipulated PSD')
plt.loglog(freqs, psd, label='Already Processed PSD')
plt.legend()
plt.xlim([0, 1000])
plt.xlabel('frequency [Hz]')
plt.ylabel('PSD [G^2/Hz]')
plt.show()



