from rtlsdr import RtlSdr
import numpy as np
from pylab import psd

sdr = RtlSdr()

sdr.sample_rate = 2.4e6
sdr.center_freq=105e6
sdr.gain=4

passes = 1000
fftbins = 1024
samples = sdr.read_samples(passes*fftbins)
sdr.close()

print(samples[0])

spectra = psd(samples,NFFT=fftbins,Fs=sdr.sample_rate/1e6,Fc=sdr.center_freq/1e6)
print(spectra[0])
print(spectra[1])