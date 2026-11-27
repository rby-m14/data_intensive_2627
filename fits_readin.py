import os
os.environ["MKL_NUM_THREADS"] = "1"
os.environ["NUMEXPR_NUM_THREADS"] = "1"
os.environ["OMP_NUM_THREADS"] = "1"

from pathlib import Path
from astropy.io import fits
import matplotlib.pyplot as plt
import numpy as np
import cv2

file = '/user/home/oh23984/euc_data/EUC_MER_BGSUB-MOSAIC-VIS_TILE102159484-116033_20241025T015934.885975Z_00.00.fits'



with fits.open(file, memmap=True) as hdu:
    print(hdu.info())

    total_rows = hdu[0].data.shape[0]

    arrays=[]
    

    for i in range (0, total_rows, 1000):
        start_row = i
        
        if (start_row+1000) > total_rows:

            padded_array = np.pad(hdu[0].data[start_row:total_rows, :], pad_width=((0,pad_width),(0,0)), mode='minimum')

            image_data = padded_array
            img_shaped = np.reshape(image_data, (100,10,192,100))
            img_mean = np.mean(img_shaped, axis=(1,3))

            arrays.append(img_mean)

        else:

            image_data = hdu[0].data[start_row:start_row+1000, :]
            img_shaped = np.reshape(image_data, (100,10,192,100))
            img_mean = np.mean(img_shaped, axis=(1,3))

            arrays.append(img_mean)

    print(arrays)
    del hdu[0].data


