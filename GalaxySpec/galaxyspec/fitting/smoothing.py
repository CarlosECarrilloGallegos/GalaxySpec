import numpy as np
from numpy import loadtxt
import scipy
from scipy import signal

def savgol_fit():
    
    """
    Applies a Savitzky-Golay to a spectrum.
    
    User inputs file, window length, and polynomial order
    
    A "Smoothed.txt" file is returned.
    
    """
    inputFileName = input("Enter name of file: ")

    spectra_file = loadtxt('inputFileName')
    spectra = np.array(spectra_file[:,1])
    wavelengths = np.array(spectra_file[:,0])
    sigma = np.sqrt(np.array(spectra_file[:,2]))

    window = int(input("Enter the window length for the savgol filter: "))
    polyorder = int(input("Enter the polynomial order for the savgol filter: "))

    spectra_sav = signal.savgol_filter(spectra, window, polyorder)
    sigma_sav = signal.savgol_filter(sigma, window, polyorder)/3

    f = open("Smoothed.txt", "w")
    i = 0

    for i in range(0,len(wavelengths)):
        f.write(str('%1.3f' % wavelengths[i]) + " ")
        f.write(str('%1.3f' % spectra_sav[i]) + " ")
        f.write(str('%1.5f' % sigma_sav[i]) + " ")
    
    
    f.close()
    
    return