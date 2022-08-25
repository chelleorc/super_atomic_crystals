#!/usr/bin/env bash
#SBATCH --time=24:00:00
#SBATCH --job-name=bands_re6_se8_cl2
#SBATCH --output=slurm.out
#SBATCH --partition=ccq
#SBATCH --constraint=skylake
#SBATCH --mail-type=all
#SBATCH --mail-user=landerson@flatironinstitute.org


source ~/qe_env.sh 

mpirun -np 40 pw.x -in bands.in < out/bands.out

bands.x < bands_pp.in > out/bands_pp.out
