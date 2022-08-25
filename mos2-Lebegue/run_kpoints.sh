#!/bin/sh
# reminder: from now on, what follows the character # is a comment
####################################################################
#
# define the following variables according to your needs
#
outdir=out/
pseudo_dir=./pseudo
# the following is not actually used:
# espresso_dir=top_directory_of_espresso_package
####################################################################

# make directory for processed data
mkdir -p data 

# remove files to prevent overwrite
rm -f $processed_output $raw_output

# set up input and output files
input=pwscf.in
raw_output=data/pwscf.out
processed_output=data/ecut_etot_kpoints_wall-time.csv

# modify input file for each set of kpoints and send output to si_kpoints.out 
for k_points in 10 15 20 25 30 35 40 45; do

echo "kpoints: ${k_points}"
# self-consistent calculation
cat > $input << EOF
&CONTROL
  calculation = 'scf'
  outdir = './out/'
  prefix = 'MoS2'
  pseudo_dir = './pseudo/'
/
&SYSTEM
  ecutrho =   4.0000000000d+02
  ecutwfc =  $ecutwfc
  ibrav = 4
  nat = 6
  ntyp = 2
  a = 3.1600000
  c = 20.000000
  occupations = 'fixed'
  smearing = 'gauss'
/
&ELECTRONS
  conv_thr =   1.0000000000d-09
/
ATOMIC_SPECIES
Mo     95.96 Mo.pbe-spn-kjpaw_psl.1.0.0.UPF
S      32.065 S.pbe-n-kjpaw_psl.1.0.0.UPF
ATOMIC_POSITIONS crystal
Mo           0.0000000000       0.0000000000       0.2500000000 
Mo           0.0000000000       0.0000000000       0.7500000000 
S            0.3333333300       0.6666666700       0.3620090000 
S            0.6666666700       0.3333333300       0.6379910000 
S            0.6666666600       0.3333333300       0.8620090000 
S            0.3333333400       0.6666666700       0.1379910000 
K_POINTS automatic
$k_points $k_points $k_points 0 0 0
EOF

   # If pw.x is not found, specify the correct value for $espresso_dir,
   # use $espresso_dir/bin/pw.x instead of pw.x

  mpirun -np 20 pw.x -in $input > $raw_output

   # grep -e 'lattice parameter' -e ! $raw_output | \
      # awk '/lattice/{alat=$(NF-1)}/!/{print alat, $(NF-1)}' >> $processed_output
   # set each grep to variable
   cutoff="$(grep -e 'kinetic-energy cutoff' ${raw_output} | awk '{print $(NF-1)}')"
   total_energy="$(grep ! ${raw_output} | awk '{print $(NF-1)}')"
   wall_time="$(grep 'PWSCF.*WALL' ${raw_output} | awk '{printf $(NF-1)}' | head -c -1)" 

   # write energy cutoff, total energy, wall time and kpoints to csv file
   echo "${cutoff}, ${total_energy}, ${wall_time}, ${k_points}" >> $processed_output
done
