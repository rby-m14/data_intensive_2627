import os
os.environ["MKL_NUM_THREADS"] = "1"
os.environ["NUMEXPR_NUM_THREADS"] = "1"
os.environ["OMP_NUM_THREADS"] = "1"

from pathlib import Path
from astropy.io import fits


folder_path = Path('/user/home/oh23984/euc_data')

fits_files = []

for file in os.listdir(folder_path):
    fits_files.append(file)
    f = os.path.join(folder_path, file)
    with fits.open(f) as hdu:
        print(hdu.info())


 


## this caused out of memory error
    # data = fits_file[0].data
    # print(type(data))
    # print(data.shape)

