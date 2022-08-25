import matplotlib.pyplot as plt
from matplotlib import rcParamsDefault
import numpy as np
import subprocess as sp
# set new figure defaults
plt.rcParams["figure.dpi"]=150
plt.rcParams["figure.facecolor"]="white"
plt.rcParams["figure.figsize"]=(8, 6)
plt.rcParams['font.size'] = 18

# load band structure data
data = np.loadtxt('Re6Se8Cl2.bands.dat.gnu')

# find the unique array elements of the first column and initialize k
k = np.unique(data[:, 0])


# Reshape data into a list of lists
bands = np.reshape(data[:, 1], (-1, len(k)))

# Iterate through band structure data where x = k and y = bands[bands, :]
for band in range(len(bands)):
    plt.plot(k, bands[band, :], linewidth=1, alpha=0.5, color='k')

# set minimum and maximum x chart limits
plt.xlim(min(k), max(k))
plt.ylim(-7.0, 5.0)


'''
If system is a metal, set Fermi energy level by using bash command:
    grep 'Fermi energy' bands_x_calc_file.out
'''
# plt.axhline(0.0000, linestyle=(0, (5, 5)), linewidth=0.75, color='k', alpha=0.5)

plt.axvline(0.0000, linewidth=0.75, color='k', alpha=0.5) #G
plt.axvline(0.5774, linewidth=0.75, color='k', alpha=0.5) #M
plt.axvline(0.9107, linewidth=0.75, color='k', alpha=0.5) #K
plt.axvline(1.2440, linewidth=0.75, color='k', alpha=0.5) #Q
plt.axvline(1.5773, linewidth=0.75, color='k', alpha=0.5) #G


# text labels and ticks at each high symmetry point on x-axis
plt.xticks(ticks= [0.0000,0.5774,0.9107, 1.2440,1.5773], \
           labels=['$\Gamma$','M','K','Q','$\Gamma$'])
plt.ylabel("Energy (eV)")


# save file as png
plt.savefig('plots/band_structure.png')
plt.show()