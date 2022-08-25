'''
This program will plot band structures of any .dat.gnu output 
'''

from asyncore import read
from pickle import HIGHEST_PROTOCOL
import matplotlib.pyplot as plt
from matplotlib import rcParamsDefault
import numpy as np
import subprocess as sp




high_symmetry_points = []
'''
Opens file
'''
def read_file(file_path):
    # open file 
    file = open(file_path,'r')
    return file.readlines()

'''
Extracts high symmetry points from band structure data
'''
def high_symmetry(file_path,keyword):
    band_structure_data = read_file(file_path)
    for line_number, line in enumerate(band_structure_data):
        if keyword in line:
            line_split = list(line.split(" "))
            high_symmetry_points.append(float(line_split[-1]))
    return high_symmetry_points

# unit test
# bands_out_file = high_symmetry("out/bands.out","high-symmetry")
# print(bands_out_file)


'''
Restructure band structure data to make them readable for plotting
'''
def plot_bands(band_structure_data):
# find the unique array elements of the first column and initialize k
    k = np.unique(band_structure_data[:, 0])

    # # Reshape band_structure_data into a list of lists
    bands = np.reshape(band_structure_data[:, 1], (-1, len(k)))

    # # # Iterate through band structure data where x = k and y = bands
    for band in range(len(bands)):
        # print(k, bands[band, :])
        plt.plot(k, bands[band, :], linewidth=1, alpha=0.5, color='k')
    plt.xlim(min(k), max(k))

    

# unit test for reshape_bands
# bands_out_file = np.loadtxt('MoS2.bands.dat.gnu')
# plot_bands(bands_out_file)
# plt.ylim(-7.0, 5.0)
# # save file as png
# plt.savefig('plots/testband_structure.png')
# plt.show()

'''
Plot kpath based on high symmetry points
'''
def kpath(high_symmetry_points, label):
    for hs in range(len(high_symmetry_points)):
        plt.axhline(hs, linestyle=(0, (5, 5)), linewidth=0.75, color='k', alpha=0.5)
    # text labels and ticks at each high symmetry point on x-axis
    plt.xticks(ticks=high_symmetry_points, \
           labels=label)

'''
Main Test Program
'''
# Open file with raw bands data
bands_structure_data = np.loadtxt('MoS2.bands.dat.gnu')
high_sym_points = []
labels=['$\Gamma$','M','K','$\Gamma$']
plt.ylim(-7.0, 5.0)

# Find the high symmetry points from bands.out file
high_sym_points = high_symmetry("out/bands.out","high-symmetry")
print(high_sym_points)
# Plot bands
plot_bands(bands_structure_data)
# Plot high symmetry points
kpath(high_sym_points, labels)

# save file as png
plt.savefig('plots/testband_structure.png')
plt.show()
