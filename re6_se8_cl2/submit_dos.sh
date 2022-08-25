#!/usr/bin/env bash
#SBATCH --time=24:00:00
#SBATCH --job-name=pdos_re6_se8_cl2
#SBATCH --output=slurm.out
#SBATCH --partition=ccq
#SBATCH --constraint=skylake
#SBATCH --mail-type=all
#SBATCH --mail-user=landerson@flatironinstitute.org


source ~/qe_env.sh 

projwfc.x -in p_dos.in < /mnt/home/landerson1/ceph/projects/quantum_espresso/super_atomic_crystals/re6_se8_cl2/out/p_dos.out
