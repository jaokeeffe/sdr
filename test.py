#!/usr/bin/python

from rtlsdr import RtlSdr

sdr = RtlSdr()

sdr.sample_rate = 2.048e6 # Hz
sdr.center_freq = 1420.4e6    # Hz
sdr.freq_correction = 60  # PPM
sdr.gain = 'auto'

fft=1024
sa=1000
samples = sdr.read_samples(sa*fft)
sdr.close()
length =  len(samples)
#print "Samples is ", length

for sample in samples:
	print(sample)


