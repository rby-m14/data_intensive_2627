import os
os.environ["MKL_NUM_THREADS"] = "1"
os.environ["NUMEXPR_NUM_THREADS"] = "1"
os.environ["OMP_NUM_THREADS"] = "1"

from astropy.io import fits

with fits.open('~/euc_data/EUC_SPE_WIDE-CAT-LIN-102159484_N_20241110T054343.637093Z_00.00.fits') as fits_file:
    fits_file.info()
    data = fits_file[0].data
    print(data)

