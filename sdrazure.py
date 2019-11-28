#!/usr/bin/python

from azure.servicebus import ServiceBusService
from rtlsdr import RtlSdr

sdr = RtlSdr()

# sdr
sdr.sample_rate = 2.048e6
sdr.center_freq = 70e6
sdr.freq_correction = 60
sdr.gain = 'auto'

# Azure
key_name = 'RootManageSharedAccessKey'
key_value = 'QIru9DStoatRrRFmQ6Sq6RfyBpe88TQyJUAemsrQzgk='
service_namespace = 'joksdr'

x = 512
i = 0
samples = sdr.read_samples(x)

sbs=ServiceBusService(service_namespace,shared_access_key_name=key_name,shared_access_key_value=key_value)
if(sbs.create_event_hub('sdrhub')):
    while(i<x):
        sbs.send_event('sdr','{"signalval": "' + str(samples[i]) + '"}')
        i = i + 1

    sbs.delete_event_hub('sdrhub')
else:
    print "Event Hub creation failed"

