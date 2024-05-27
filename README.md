SUIT Colormap
Maintained by- Janmejoy Sarkar, SUIT- Aditya-L1

This project maintatins the colormap for SUIT images.

Filter-names:
["NB01", "NB02", "NB03", "NB04", "NB05", "NB06", "NB07", "NB08", "BB01", "BB02", "BB03"]




Usage:

from colormap import filterColor
data= #image data as 2D numpy array
plt.imshow(data, vmin=0, vmax= vmx, cmap= filterColor[filter-name], origin='lower')

