from calendar import c
import matplotlib.pyplot as plt
from matplotlib import rcParamsDefault
import numpy as np 
import pandas as pd


########################################################################################
'''
This code block to set Fermi energy
'''
scf_fermi_energy = 10.35
nscf_fermi_energy = 11.3511

plt.rcParams['font.size'] = 18
plt.figure(figsize = (12, 6))
########################################################################################

########################################################################################
'''
#### Atomic PDOS ####
Use this code block to plot each atomic pdos vs energy 
'''
# load data
# Re_energy, Re_pdos = np.loadtxt('/mnt/home/landerson1/ceph/projects/quantum_espresso/super_atomic_crystals/re6_se8_cl2/data/atom_Re_tot.dat', unpack=True)
# Se_energy, Se_pdos = np.loadtxt('/mnt/home/landerson1/ceph/projects/quantum_espresso/super_atomic_crystals/re6_se8_cl2/data/atom_Se_tot.dat', unpack=True)
# Cl_energy, Cl_pdos = np.loadtxt('/mnt/home/landerson1/ceph/projects/quantum_espresso/super_atomic_crystals/re6_se8_cl2/data/atom_Cl_tot.dat', unpack=True)

# # make plot and rename label to atom of interest
# plt.plot(Re_energy-scf_fermi_energy, Re_pdos, label='Se-s',linewidth=0.75, color='green')
# plt.plot(Se_energy-scf_fermi_energy, Se_pdos, label='Se-p', linewidth=0.75, color='purple')
# plt.plot(Cl_energy-scf_fermi_energy, Cl_pdos, label='Se-d', linewidth=0.75, color='red')

# # Set Fermi energy line (get from nscf.out)
# plt.fill_between(Re_energy-scf_fermi_energy, 0, Re_pdos, where=(Re_energy < nscf_fermi_energy), facecolor='green', alpha=0.25)
# plt.fill_between(Se_energy-scf_fermi_energy, 0, Se_pdos, where=(Se_energy < nscf_fermi_energy), facecolor='purple', alpha=0.25)
# plt.fill_between(Cl_energy-scf_fermi_energy, 0, Cl_pdos, where=(Cl_energy < nscf_fermi_energy), facecolor='red', alpha=0.25)


########################################################################################

########################################################################################
'''
#### Orbital PDOS ####
Use this codeblock to plot s, p, d orbital energy contribution for Re, Se, or Cl
'''
# load data by editing filename 
tot_energy, tot_pdos = np.loadtxt('/mnt/home/landerson1/ceph/projects/quantum_espresso/super_atomic_crystals/re6_se8_cl2/data/atom_Se_tot.dat', unpack=True)
s_energy, s_pdos = np.loadtxt('/mnt/home/landerson1/ceph/projects/quantum_espresso/super_atomic_crystals/re6_se8_cl2/data/atom_Se_s.dat', unpack=True)
p_energy, p_pdos = np.loadtxt('/mnt/home/landerson1/ceph/projects/quantum_espresso/super_atomic_crystals/re6_se8_cl2/data/atom_Se_p.dat', unpack=True)
d_energy, d_pdos = np.loadtxt('/mnt/home/landerson1/ceph/projects/quantum_espresso/super_atomic_crystals/re6_se8_cl2/data/atom_Se_d.dat', unpack=True)

# plot data and rename label to atom of interest
plt.plot(tot_energy-scf_fermi_energy, tot_pdos, label='Se-tot',linewidth=0.75, color='black')
plt.plot(s_energy-scf_fermi_energy, s_pdos, label='Se-s',linewidth=0.75, color='green')
plt.plot(p_energy-scf_fermi_energy, p_pdos, label='Se-p', linewidth=0.75, color='purple')
plt.plot(d_energy-scf_fermi_energy, d_pdos, label='Se-d', linewidth=0.75, color='red')

# Fill in energy below the Fermi energy for improved visualization
# plt.fill_between(tot_energy-scf_fermi_energy, 0, tot_pdos, where=(tot_energy < nscf_fermi_energy), facecolor='black', alpha=0.25)
# plt.fill_between(s_energy-scf_fermi_energy, 0, s_pdos, where=(s_energy < nscf_fermi_energy), facecolor='green', alpha=0.25)
# plt.fill_between(p_energy-scf_fermi_energy, 0, p_pdos, where=(p_energy < nscf_fermi_energy), facecolor='purple', alpha=0.25)
# plt.fill_between(d_energy-scf_fermi_energy, 0, d_pdos, where=(d_energy < nscf_fermi_energy), facecolor='red', alpha=0.25)

########################################################################################

########################################################################################
'''
Set plot parameters
'''
plt.title("PDOS vs. Energy(eV)")
plt.xlabel('Energy (eV)')
plt.ylabel('PDOS')

plt.axvline(x=0, linewidth=0.5, color='k', linestyle=(0, (8, 10)))
plt.text(-0.15, 5.0, 'Fermi energy', fontsize= 'medium', rotation=90)

plt.xlim(-2.0, 3.0)
plt.ylim(-1.0, 10.0)
plt.yticks([])
plt.legend(loc=1)


# Save figure by renaming to atom of interest
# plt.savefig('plots/test_Re_Se_Cl_pdos.png')
plt.savefig('plots/Se_pdos.png')
plt.show()