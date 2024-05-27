#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri May 24 18:13:03 2024

@author: janmejoyarch
"""

from matplotlib.colors import LinearSegmentedColormap
import matplotlib.pyplot as plt
from astropy.io import fits
import glob

def make_cmap(col_ls, pos_ls=None):
    if (pos_ls != None): 
       cmap= LinearSegmentedColormap.from_list("CustomGradient1", list(zip(pos_ls, col_ls)))
    else:
        cmap= LinearSegmentedColormap.from_list("CustomGradient1", col_ls)
    return(cmap)

filterColor = {
    'BB01': make_cmap(['#000000','#35095f','#e8acf3','#ffffff'], [0, 0.26, 0.7, 1]),
    'BB02': make_cmap(['#000000','#562210','#be8b12','#ffffff']),
    'BB03': make_cmap(['#000000','#6d0000','#d39552','#ffffff']),
    'NB01': make_cmap(['#000000','#ffffff']),
    'NB02': make_cmap(['#000000','#3e600c','#a4d15e','#ffffff']),
    'NB03': make_cmap(['#000000','#674201','#c1a50a','#ffffff']),
    'NB04': make_cmap(['#000000','#672000','#ffc600','#ffffff'], [0,0.34,0.68,1]), 
    'NB05': make_cmap(['#000000','#452263','#ab74d9','#ffffff'], [0,0.24,0.57,1]),
    'NB06': make_cmap(['#000000','#005393','#68b0d6','#ffffff'], [0,0.38,0.66,1]),
    'NB07': make_cmap(['#000000', '#aa4639', '#ffffff']),
    'NB08': make_cmap(['#000000','#331385','#d2adff','#ffffff'])
}

if __name__=="__main__":
    ftr_list= ["NB01", "NB02", "NB03", "NB04", "NB05", "NB06", "NB07", "NB08", "BB01", "BB02", "BB03"]
    vmx_list=[2.5e4, 5e4, 3e4, 3.5e4, 6e4, 5e4, 5e4, 1.5e4, 7e4, 3.5e4, 3.2e4]
    for ftr_name, vmx in zip(ftr_list, vmx_list):        
        file= glob.glob(f'/home/janmejoyarch/shared_folder/FITS_FOR_CHAIRMAN/*{ftr_name}.fits')[0]
        data=fits.open(file)[0].data
        plt.figure(ftr_name)
        plt.imshow(data, vmin=0, vmax= vmx, cmap= filterColor[ftr_name])
        plt.title(ftr_name)
        plt.colorbar()
        plt.show()