import qe_parser as qe
import matplotlib.pyplot as plt
from matplotlib import rcParamsDefault
import numpy as np

# set new figure defaults
plt.rcParams["figure.dpi"]=150
plt.rcParams["figure.facecolor"]="white"
plt.rcParams["figure.figsize"]=(8, 6)
plt.rcParams['font.size'] = 18


# load band structure data
data = np.loadtxt('MoS2.bands.dat.gnu')


# unit test
bands_out_file = qe.read_file("out/bands.out")
print(bands_out_file)

   # set minimum and maximum x chart limits
    # plt.xlim(min(k), max(k))    
    # plt.ylim(y_min, y_max)    

    # high_sym_points = []
    # # # text labels and ticks at each high symmetry point on x-axis
    # high_sym_points = high_symmetry(band_structure_data,"high-symmetry")
    # plt.xticks(ticks= high_sym_points, \
    #     labels=['$\Gamma$','M','K','$\Gamma$'])
    # plt.savefig(out_file_path)
    # plt.show()


# plt.ylabel("Energy (eV)")
# # plt.text(1.3, -0.3, 'Fermi energy', fontsize='medium')

# # save file as png
# plt.savefig('plots/band_structure.png')
# plt.show()