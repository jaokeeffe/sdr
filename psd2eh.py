#!/usr/bin/python

from azure.servicebus import ServiceBusService
from rtlsdr import RtlSdr
from matplotlib.mlab import psd
#from scipy import signal

sdr = RtlSdr()

# sdr
sdr.sample_rate = 2.048e6
sdr.center_freq = 105e6
sdr.freq_correction = 60
sdr.gain = 'auto'

# Azure
key_name = 'RootManageSharedAccessKey'
key_value = 'uoDYiA/o3Jjtp2Wb4f3HZnclv73VneyPigcZ0jwGMEU='
service_namespace = 'joksdrpsd'
evhub = 'sdr1'
sbs=ServiceBusService(service_namespace,shared_access_key_name=key_name,shared_access_key_value=key_value)
x = 1024 # FFT bins
i = 256  # Passes

while(True):
	samples = sdr.read_samples(i*x)
	sdr.close()
	power,freq = psd(samples, NFFT=x, Fs=sdr.sample_rate/1e6)
	
	for i in range(len(freq)):
		msg = '{"psd": "' + str(freq[i]) + ',' + str(power[i]) + '"}'
		sbs.send_event(evhub,msg)



