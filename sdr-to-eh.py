#!/usr/bin/python

from azure.servicebus import ServiceBusService
from rtlsdr import RtlSdr

sdr = RtlSdr()

# sdr
sdr.sample_rate = 2.4e6
sdr.center_freq = 105e6
#sdr.freq_correction = 60
#sdr.gain = 'auto'
sdr.gain = 4

# Azure
key_name = 'RootManageSharedAccessKey'
key_value = 'QIru9DStoatRrRFmQ6Sq6RfyBpe88TQyJUAemsrQzgk='
service_namespace = 'joksdr'

fft = 1024 
s = 10
i = 0
samples = sdr.read_samples(s * fft)
sdr.close()
del(sdr)

sbs=ServiceBusService(service_namespace,shared_access_key_name=key_name,shared_access_key_value=key_value)
while(i<(s*fft)):
    sbs.send_event('sdr','{"signalval": "' + str(samples[i]) + '"}')
    i = i + 1

