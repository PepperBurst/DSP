import numpy as np
from scipy import signal as sig
from scipy.io import wavfile as wvf
import matplotlib.pyplot as plt
#this is the file used for the filters
def s1(x):
    b = [1/2, -1/2]
    a = [1]
    y = sig.lfilter(b, a, x)
    return y

def s2(x):
    b = [1]
    a = [1, -1/2]
    y = sig.lfilter(b, a, x)
    return y

def musicFilter(path):
    # this is the audio reading capabilities of scipy
    # wvf.read will read the wav file and return sampling rate and data
    # we will do processing on the data only
    rate, data = wvf.read(path)
    # we will normalize the int16 data file to a float 32 data type
    data = data / ((2**16)/2)
    data = np.array(data, dtype=np.float32)
    # we are setting it's type to np.float32 because
    # there are issues wherein it ussed np.float64 instead and this will
    # show up problems in writing the wav file so
    # extra care is needed in the data types
    s1Data = np.array(s1(data), dtype=np.float32)
    s2Data = np.array(s2(data), dtype=np.float32)
    s1Data = np.float32(s1Data)
    s2Data = np.float32(s2Data)
    # we add a .wav file extension to save it as a wav file
    fileName = 's1 filtered.wav'
    print(s1Data.dtype)
    wvf.write(fileName, rate, s1Data)
    # we are using String.replace to replace parts of the string
    # instead of writing it all over again
    fileName = fileName.replace('1', '2', 1)
    wvf.write(fileName, rate, s2Data)
    # plt.subplot(311)
    # plt.plot(np.arange(0, len(data)), data)
    # plt.subplot(312)
    # plt.plot(np.arange(0, len(s1Data)), s1Data)
    # plt.subplot(313)
    # plt.plot(np.arange(0, len(s2Data)), s2Data)
    # plt.show()
    #s1 Filter is a High-Pass Filter
    #s2 Filter is a Low-Pass Filter

def fil351(x):
    # these are the coefficients of the filter
    b = [0.2, 0.4, 0.2]
    a = [1, 0, 0.8]
    y = sig.lfilter(b, a, x)
    return y

def fil352(x):
    b = [1, 1/2]
    a = [1, -1.8*np.cos(np.pi/16), 0.81]
    y = sig.lfilter(b, a, x)
    return y
