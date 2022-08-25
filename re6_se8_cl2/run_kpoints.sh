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
processed_output=data/kpoints.csv

# modify input file for each set of kpoints and send output to si_kpoints.out 
for k_points in 1 2 3 4 5 6 7 9; do

echo "kpoints: ${k_points}"
# self-consistent calculation
cat > $input << EOF
&control
	prefix	=	'Re6Se8Cl2'
	calculation	=	'scf'
	wf_collect	=	.false.
	outdir	=	'./out'
	wfcdir	=	'./wfc'
  pseudo_dir   =    './pseudo'	
	max_seconds	=	42000
/

&system
	ibrav	=	14
	celldm(1)	=	12.468413
	celldm(2)	=	1.006365565
	celldm(3)	=	1.338966353
  celldm(4)    =    0.2290644793
	celldm(5)	=	0.3370952584
  celldm(6)    =    0.0634872582
	nat	=	16
	ntyp	=	3
	ecutwfc	=	50
	ecutrho	=	200
	nbnd	=	260
	! occupations	=	'smearing'
	! smearing	=	'gaussian'
	! degauss	=	0.001
	lspinorb	=	.True.
	noncolin	=	.True.
/

&electrons
	diagonalization='cg'
	mixing_mode = 'plain'
	mixing_beta = 0.7
	electron_maxstep	=	100
	conv_thr	=	1e-06
/

ATOMIC_SPECIES
	Se   78.96  Se.rel-pbe-dn-kjpaw_psl.1.0.0.UPF
    Cl   35.453 Cl.rel-pbe-n-kjpaw_psl.1.0.0.UPF
    Re   186.207 Re.rel-pbe-spn-kjpaw_psl.1.0.0.UPF

ATOMIC_POSITIONS {angstrom}
Se      0.9832662828    4.3009863649    1.5592122665
Se      9.0143567172    4.1639266351    6.5525157335
Cl      2.5077453349    2.2885865293    3.9756169856
Cl      7.4898776651    6.1763264707    4.1361110144
Se      1.7537090282    0.8687108002    0.8925065745
Se      8.2439139718    7.5962021998    7.2192214255
Re      3.0634232334    2.8651772698    1.7696409569
Re      6.9341997666    5.5997357302    6.3420870431
Re      3.0289459833    5.0791626815    0.2939615152
Re      6.9686770167    3.3857513185    7.8177664848
Se      4.2568340669    4.9644097366    2.5050777593
Se      5.7407889331    3.5005042634    5.6066492407
Se      5.2121166140    1.5652459357    1.9190487180
Se      4.7855073860    6.8996680643    6.1926792820
Re      5.2401418271    3.6878209348    0.5561869056
Re      4.7574811729    4.7770930652    7.5555410944

K_POINTS {automatic}
$k_points $k_points 1 0 0 0

EOF

   # If pw.x is not found, specify the correct value for $espresso_dir,
   # use $espresso_dir/bin/pw.x instead of pw.x

  mpirun -np 40 pw.x -in $input > $raw_output

   # grep -e 'lattice parameter' -e ! $raw_output | \
      # awk '/lattice/{alat=$(NF-1)}/!/{print alat, $(NF-1)}' >> $processed_output
   # set each grep to variable
   cutoff="$(grep -e 'kinetic-energy cutoff' ${raw_output} | awk '{print $(NF-1)}')"
   total_energy="$(grep ! ${raw_output} | awk '{print $(NF-1)}')"
   charge_cutoff="$(grep -e 'charge density cutoff' ${raw_output} | tail -1 | awk '{print $(NF-1)}')"
   wall_time="$(grep 'PWSCF.*WALL' ${raw_output} | awk '{printf $(NF-1)}' | head -c -1)" 

   # write energy cutoff, total energy, wall time and kpoints to csv file
   echo "${k_points}, ${cutoff}, ${charge_cutoff}, ${total_energy}, ${wall_time}" >> $processed_output
done
