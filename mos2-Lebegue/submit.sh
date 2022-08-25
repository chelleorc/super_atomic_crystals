#!/usr/bin/env bash
#SBATCH --time=24:00:00
#SBATCH --job-name=mos2_bands
#SBATCH --output=slurm.out
#SBATCH --partition=ccq
#SBATCH --constraint=skylake
#SBATCH --mail-type=all
#SBATCH --mail-user=landerson@flatironinstitute.org

source ~/qe_env.sh 


mpirun -np 20 pw.x -in pw_bands.in > out/pw_bands.out

