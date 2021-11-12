import lmfit
from lmfit import Model

def gaussian_fit(spectra, sigma, wavelengths, z_best):
    """
    Fits a gaussian to a spectra with a best-fit redshift using lmfit
    
    Parameters
    --------------------
    
    spectra (1D Array):
        Spectral data for which we will find the best fit redshift
        
    wavelengths (1D Array):
        wavelengths correspodning to spectra
        
    sigma (1D Array):
        standard deviation values for the spectrum
        
    z_best(float):
        redshift associated with minimum chi-sq value
        
    Returns
    -------------------------
    fit_report:
        Gaussian fit to the spectrum
    
    """
    wave_max = int(input("Enter the maximum wavelength for the Gaussian Distribution: "))
    wave_min = int(input("Enter the minimum wavelength for the Gaussian Distribution: "))


    index_gauss = np.where((np.logical_and(wavelengths < wave_max, wavelengths > wave_min)))

    spectra_trim = spectra[index_gauss]
    sigma_trim = sigma[index_gauss]
    wave_trim = wavelengths[index_gauss]
    weights = 1 / (sigma_trim**2)

    gauss_model = Model(gaussian)

    #Enter guesses for amplitude, width

    amplitude = int(input("Enter guess for amplitude of fit: "))
    width = int(input("Enter guess for width of fit: "))

    params = gauss_model.make_params(centr = (1.0 + z_best) * 3728.0, amp = amplitude, width = width, contin = 60.0)

    fit_report = gauss_model.fit(spectra_trim, params, weights, x = wave_trim)
    
    return fit_report
