import matplotlib.pyplot as plt
import numpy as np
import scipy.signal as signal
from pyyeti import psd
frange = (1.0, np.inf)
rng = np.random.default_rng()
g = rng.normal(size=10000)
sr = 400
f, p = signal.welch(g, sr, nperseg=sr)
p3, f3, msv3, ms3 = psd.rescale(p, f, frange=frange)
p6, f6, msv6, ms6 = psd.rescale(
    p, f, n_oct=6, frange=frange)
p12, f12, msv12, ms12 = psd.rescale(
    p, f, n_oct=12)

print(f)
fig = plt.figure('Example', clear=True,
                 layout='constrained')
line = plt.semilogx(f, p, label='Linear')
line = plt.semilogx(f3, p3, label='1/3 Octave')
line = plt.semilogx(f6, p6, label='1/6 Octave')
line = plt.semilogx(f12, p12, label='1/12 Octave')
plt.legend(ncol=2, loc='best')
plt.xlim([1, 200])
plt.show()
msv1 = np.sum(p[1:]*(f[1]-f[0]))
abs(msv1/msv3 - 1) < .12
abs(msv1/msv6 - 1) < .06
abs(msv1/msv12 - 1) < .03