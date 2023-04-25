import numpy as np
import matplotlib.pyplot as plt
from scipy.constants import c, eV, h, pi
import math

# Constants
n_water = 1.33  # Refractive index of water
hc = h * c / eV  # Convert hc to eV * nm

def frank_tamm(wavelength, beta):
    """
    Calculate Cherenkov radiation intensity using the Frank-Tamm formula.
    :param wavelength: Wavelength in nm
    :param beta: Particle speed as a fraction of the speed of light
    :return: Cherenkov radiation intensity
    """
    k = 2 * pi / wavelength
    intensity = (2 * math.pi * (1 / 137)) * (1 / wavelength**2) * (1 - 1 / (beta**2 * n_water**2))
    return intensity * (intensity > 0)

# Wavelength range
wavelengths = np.linspace(200, 800, 1000)

# Speeds as fractions of the speed of light
speeds = [0.75 * c, 0.80 * c, 0.90 * c, 0.99 * c]

# Plot Cherenkov radiation spectrum
plt.figure()

for speed in speeds:
    beta = speed / c
    intensity = frank_tamm(wavelengths, beta)
    plt.plot(wavelengths, intensity, label=f"{beta:.2f}c")

plt.xlabel("Wavelength (nm)")
plt.ylabel("Cherenkov Spectrum (Intensity)")
plt.title("Cherenkov Radiation Spectrum in Water")
plt.legend()
plt.grid()
plt.savefig('foo.png')
plt.show()
