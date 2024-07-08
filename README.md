
![Logo](https://suit.iucaa.in/sites/default/files/top_banner_compressed_2_1.png)


# SUIT Colormap
- Colormap for 11 science bandpasses of the SUIT payload of Aditya-L1.

Created by Janmejoy Sarkar @ [SUIT](https://suit.iucaa.in)LAB\
Initiated in May 2024.

## Screenshots

- BB01 ![BB01](./README_files/qt_img170316928122886.png)
- BB02 ![BB02](./README_files/qt_img170372762697734.png)
- BB03 ![BB03](./README_files/qt_img170428597272582.png)
- NB01 ![NB01](./README_files/qt_img170523086553094.png)
- NB02 ![NB02](./README_files/qt_img170656230539270.png)
- NB03 ![NB03](./README_files/qt_img170922518511622.png)
- NB04 ![NB04](./README_files/qt_img170789374525446.png)
- NB05 ![NB05](./README_files/qt_img171055662497798.png)
- NB06 ![NB06](./README_files/qt_img171188806483974.png)
- NB07 ![NB07](./README_files/qt_img171283295764486.png)
- NB08 ![NB08](./README_files/qt_img171416439750662.png)

## Authors

- [@janmejoysarkar](https://github.com/janmejoysarkar)


## Acknowledgements

 - [IUCAA, Pune](https://www.iucaa.in)
 - [ISRO, Aditya-L1](https://www.isro.gov.in/Aditya_L1.html)


## Usage/Examples

```python
from colormap import filterColor
from matplotlib.colors import PowerNorm

data= #image data as 2D numpy array
plt.imshow(data, cmap= filterColor[filter-name], norm=PowerNorm(0.6,vmin=0), origin='lower')
#Use powernorm for RoI images or if needed.
