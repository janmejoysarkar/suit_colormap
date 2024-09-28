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
    save=input("Save? [y/n] ")
    project_path= os.path.expanduser('~/Dropbox/Janmejoy_SUIT_Dropbox/SUIT_publicity/colormap_project')
    
    vmx_dict={"NB01":25000.0,
    "NB02":17000.0,
    "NB03":9000.0,
    "NB04":10000.0,
    "NB05":15000.0,
    "NB06":50000.0,
    "NB07":50000.0,
    "NB08":12000.0,
    "BB01":50000.0,
    "BB02":10000.0,
    "BB03":32000.0}
    
    ftr_name='BB03'
    file= glob.glob(f'{project_path}/data/*1.0*{ftr_name}.fits')[0]
    data=fits.open(file)[0].data
    print(os.path.basename(file))
    plt.figure(ftr_name)
    plt.imshow(data, vmin=0, vmax= vmx_dict[ftr_name], cmap= filterColor[ftr_name], origin='lower')
    plt.title(ftr_name)
    plt.colorbar()
    if save=='y': plt.savefig(f'{project_path}/products/{os.path.basename(file)[:-5]}.png', dpi=600)
    plt.show()
'''
    for ftr_name, vmx in zip(ftr_list, vmx_list):        
        file= glob.glob(f'/data1/janmejoy/SUIT_publicity/2023-12-06/*{ftr_name}.fits')[0]
        data=fits.open(file)[0].data
        plt.figure(ftr_name)
        plt.imshow(data, vmin=0, vmax= vmx, cmap= filterColor[ftr_name], origin='lower')
        plt.title(ftr_name)
        plt.colorbar()
        if save==True: plt.savefig(f'{PROJ}/products/{ftr_name}.pdf')
        plt.show()
'''
