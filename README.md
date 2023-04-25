# Cherenkov Radiation Spectrum in Water
This code calculates and plots the Cherenkov radiation spectrum in water using the Frank-Tamm formula. The Cherenkov radiation is electromagnetic radiation emitted when a charged particle moves through a medium faster than the speed of light in that medium.

# Dependencies
This code requires the following Python packages:

- NumPy
- Matplotlib
- SciPy

# Usage 
To use this code, simply import the required packages and call the `frank_tamm()` function with the desired wavelength range and speeds. The `frank_tamm()` function returns the Cherenkov radiation intensity for the given wavelength and speed.

# Explanation
The code first imports the required packages: NumPy, Matplotlib, and SciPy. NumPy is used to create the wavelength range, Matplotlib is used to plot the Cherenkov radiation spectrum, and SciPy is used to import physical constants.

Then, it defines the refractive index of water (`n_water`) and converts the product of the Planck constant (`h`) and the speed of light (`c`) to electronvolts times nanometers (`hc`). It then defines the frank_tamm function, which takes a wavelength in nanometers and a particle speed as a fraction of the speed of light, and returns the Cherenkov radiation intensity using the Frank-Tamm formula.

The code then plots the Cherenkov radiation spectrum for each speed using a for loop. It calculates the beta factor for each speed, calls the `frank_tamm` function with the wavelength range and beta factor, and plots the intensity as a function of wavelength.
 # Result
 
