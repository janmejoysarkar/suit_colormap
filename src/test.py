#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon May 27 12:27:53 2024

@author: janmejoyarch
"""

import matplotlib.pyplot as plt
from astropy.io import fits
import glob
from colormap import filterColor
import os

if __name__=="__main__":
    PROJ= os.path.expanduser('~/Dropbox/Janmejoy_SUIT_Dropbox/SUIT_publicity/colormap_project')
    
    ftr_list= ["NB01", "NB02", "NB03", "NB04", "NB05", "NB06", "NB07", "NB08", "BB01", "BB02", "BB03"]
    vmx_list=[2.5e4, 5e4, 3.5e4, 4e4, 6e4, 5e4, 5e4, 1.5e4, 5e4, 3.5e4, 3.2e4]
   
    for ftr_name, vmx in zip(ftr_list, vmx_list):        
        file= glob.glob(f'/home/janmejoyarch/shared_folder/FITS_FOR_CHAIRMAN/*{ftr_name}.fits')[0]
        data=fits.open(file)[0].data
        plt.figure(ftr_name)
        plt.imshow(data, vmin=0, vmax= vmx, cmap= filterColor[ftr_name], origin='lower')
        plt.title(ftr_name)
        plt.colorbar()
        plt.savefig(f'{PROJ}/products/{ftr_name}.pdf')
        plt.show()