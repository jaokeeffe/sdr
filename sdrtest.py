from rtlsdr import RtlSdr
import numpy as np

sdr = RtlSdr()

sdr.sample_rate = 2.4e6
sdr.center_freq=105e6
sdr.gain=4

passes = 1000
fftbins = 1024
samples = sdr.read_samples(passes*fftbins)
sdr.close()

print(samples[0])