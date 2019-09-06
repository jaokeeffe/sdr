import pandas as pd
import numpy as np

filename = 'd:\\temp\\sdr.csv'

dfSDR = pd.read_csv(filename)
dfSDR.info()

dfSDR['signalval'] = dfSDR['signalval'].apply(complex)
dfSDR.info()
