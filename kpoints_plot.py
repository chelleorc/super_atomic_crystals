from email import header
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.ticker as mtick
import pandas as pd
import seaborn as sb


# list of headers for each data column
# col = ['energy cutoff (Ry)', 'total energy (Ry)', 'wall time (s)', 'kpoints']

# open file as csv which is tab separated, and ignores blank lines and comments
data = pd.read_csv('data/kpoints.csv', 
                    sep=',',skip_blank_lines=True,header=0,names=["K Points (n x n x 1)","Energy Cutoff(Ry)","Charge Density(Ry)","Total Energy Difference(Ry)","Wall Time"])

charge_density = data["Charge Density(Ry)"]
total_energy = data["Total Energy Difference(Ry)"]-min(data["Total Energy Difference(Ry)"])
energy_cutoff = data["Energy Cutoff(Ry)"]
wall_time = data["Wall Time"]
print(min(data["Total Energy Difference(Ry)"]))
# conversion factor for eV
eV = 13.6056980659

# data["Wall Time"] = pd.to_datetime(data["Wall Time"], format="%H:%M:%S", errors='coerce')
# print dataframe of csv file
print(total_energy)

# total_energy = data["Total Energy"]
sb.set_context("notebook", font_scale=1.0, rc={"lineswidth": 2.5})
sb.set_style("whitegrid")

# plot total energy data
fig = sb.lineplot(data=data, x="K Points (n x n x 1)", y=total_energy).figure
#data.plot.scatter(x = 3, y = 1, figsize=(20,10),s=300)
# plt.gca().yaxis.set_major_formatter(mtick.FormatStrFormatter('%.6f'))
# plt.xlim(min("K Points"),max("K Points"))
# plt.ylim(min(total_energy), max(total_energy))

plt.title("Convergence Test for Kinetic Energy Cutoff")
plt.tight_layout()
plt.show()

fig.savefig("plots/etot_kpoints.png")

