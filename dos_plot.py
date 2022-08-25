import matplotlib.pyplot as plt
from matplotlib import rcParamsDefault
import numpy as np


# load data
energy, dos, idos = np.loadtxt('/mnt/home/landerson1/ceph/projects/quantum_espresso/super_atomic_crystals/re6_se8_cl2/Re6Se8Cl2_dos.dat', unpack=True)

plt.rcParams['font.size'] = 18

# make plot
plt.figure(figsize = (12, 6))
plt.plot(energy-10.3516, dos, linewidth=0.75, color='red')
plt.xticks(np.arange(-2, 3, step=0.5))
plt.yticks([])
plt.xlabel('Energy (eV)')
plt.ylabel('DOS')
plt.axvline(x=0, linewidth=0.5, color='k', linestyle=(0, (8, 10)))
plt.xlim(-2.0, 3.0)
plt.ylim(-1.0, 35.0)

# get Fermi energy from non-scf output file
plt.fill_between(energy-10.3516, 0, dos, where=(energy < 11.3511), facecolor='red', alpha=0.25)
plt.text(10.99, 1.0, 'Fermi energy', fontsize= 'medium', rotation=90)
plt.title("DOS vs. Energy(eV)")
plt.savefig('plots/dos.png')
plt.show()