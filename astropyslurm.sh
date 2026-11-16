#!/bin/bash
# ======================
# astropyslurm.sh
# ======================
#SBATCH --job-name=astropy_test
#SBATCH --output=astropytest.out
#SBATCH --partition=teach_cpu
#SBATCH --account=phys040684
#SBATCH --nodes=1
#SBATCH --ntasks-per-node=1
#SBATCH --cpus-per-task=1
#SBATCH --time=0:01:00
#SBATCH --mem=100M

source ~/initMamba.sh
mamba activate dipenv
rclone copy compremote:DIP_2026/EUC_SPE_WIDE-CAT-LIN-102159484_N_20241110T054343.637093Z_00.00.fits /user/home/oh23984/euc_data/

cd $SLURM_SUBMIT_DIR
# Now run your program with the usual command
python astropytest.py