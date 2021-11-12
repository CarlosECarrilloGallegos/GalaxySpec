from astropy.io import fits
import numpy as np
import matplotlib.pyplot as plt
from numpy import loadtxt
from numpy import exp

def best_redshift(spectra, wavelengths, sigma, eigen_fits, min_redshift, max_redshift, increment):
    """
    This function takes a spectrum and its associated sigma array as well as eignespectra and computes
    find the best fit redshift for the function.
    
    Parameters
    --------------------
    
    spectra (1D Array):
        Spectral data for which we will find the best fit redshift
        
    wavelengths (1D Array):
        wavelengths correspodning to spectra
        
    sigma (1D Array):
        standard deviation values for the spectrum
        
    eigen_fits (FITS file):
        FITS file containing wavelength and spectral data for 4 different eigenspectra used for fitting.
        
    min_redshift (int):
        Minimum redshift to test
    
    max_redshift (int):
        Maximum redshift to test
        
    increment (float):
        increment for redshift loop
        
    
    Returns
    ----------------------
    
    redshift_spectra.txt(txt file):
        file containing each redshift, its chi-sq, and best fit coefficients
        
    z_best(float):
        redshift associated with minimum chi-sq value
    
    """
    f = open('redshift_spectra.txt', 'w')
    dummy = 100000000.0
    z_best = 0.0
    model_best = np.empty([len(spectra)])
    spectraDIV = spectra / sigma

    #We must interpolate the eignespectra data to align it with the indicies of the observed
    #spectra
    for z in np.arange(min_redshift, max_redshift, increment):

        wavelengths_z = eigen_fits[1].data['Wave'] * (1.0 + z)

        flux1_intp = np.interp(wavelengths, wavelengths_z, eigen_fits[1].data['flux1']) / sigma
        flux2_intp = np.interp(wavelengths, wavelengths_z, eigen_fits[1].data['flux2']) / sigma
        flux3_intp = np.interp(wavelengths, wavelengths_z, eigen_fits[1].data['flux3']) / sigma
        flux4_intp = np.interp(wavelengths, wavelengths_z, eigen_fits[1].data['flux4']) / sigma

        A = np.vstack([flux1_intp, flux2_intp, flux3_intp, flux4_intp]).T
        Y = spectraDIV[:,np.newaxis]
        pinv = np.linalg.pinv(A)
        coeff = pinv.dot(Y)
        model = (coeff[0]*flux1_intp + coeff[1]*flux2_intp + coeff[2]*flux3_intp + coeff[3]*flux4_intp) * sigma
    
        chi_sq = np.sum(((spectra - model) / sigma)**2)

        if (chi_sq < dummy):
            dummy = chi_sq
            z_best = z
            model_best = model


        f.write(str("%1.4f" % z + " "))
        f.write(str("%1.2f" % chi_sq + " "))
        f.write(str("%1.4f" % coeff[0] + " "))
        f.write(str("%1.4f" % coeff[1] +  " "))
        f.write(str("%1.4f" % coeff[2] + " "))
        f.write(str("%1.4f" % coeff[3] + "\n "))

    f.close()
    
    return z_best

   