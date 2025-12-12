import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import matplotlib.mlab as mlab
import scipy.signal
from scipy.signal import welch


# Load CSV data
acceldata = pd.read_csv('accelzdata.csv')
data = acceldata.values.flatten()  # Convert to 1D array

# Define your custom time series
sample_rate = 1000  # samples per second (adjust as needed)

(f, S)= scipy.signal.welch(data, sample_rate, nperseg=4096)

plt.semilogy(f, S)
plt.xlim([0, 100])
plt.xlabel('frequency [Hz]')
plt.ylabel('PSD [G^2/Hz]')
plt.show()



