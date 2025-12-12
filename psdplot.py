import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import matplotlib.mlab as mlab
import scipy.signal
from scipy.signal import welch


# Load CSV data
acceldata = pd.read_csv('RAWDATA - Waveform.csv', usecols=['FrontAxle_Left Front (Max) (G)'])
data = acceldata.values.flatten()  # Convert to 1D array
nfreq = 101 # number of frequency points
sample_rate = 2000  # samples per second (adjust as needed)

(f, S)= scipy.signal.welch(data, sample_rate, nperseg=len(data)/nfreq)

plt.loglog(f, S)
plt.xlim([0, 1000])
plt.xlabel('frequency [Hz]')
plt.ylabel('PSD [G^2/Hz]')
plt.show()



