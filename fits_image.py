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
    image_data = hdu[0].data
    print(type(image_data))
    print(image_data.shape)
    print(f'Minimum {np.min(image_data):.2f}, Maximum {np.max(image_data):.2f}, Mean {np.mean(image_data):.2f}')
    del hdu[0].data
    # print(len(image_data[0]))
    # print(len(image_data[1]))
    width = int(len(image_data[0])/100)
    height = int(len(image_data[1])/100)
    # print(width)
    image_slice = image_data[0:width, 0:height]
    res = cv2.resize(image_slice, dsize=(100, 100))
    print(res.shape)


plt.imshow(image_slice, cmap='gray')
plt.colorbar()
plt.savefig('testeuclidimg.png')
 


