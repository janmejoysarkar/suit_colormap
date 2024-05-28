<!DOCTYPE html>
<html>
<head>
	<meta http-equiv="content-type" content="text/html; charset=utf-8"/>
	<meta name="generator" content="LibreOffice 7.6.7.2 (Linux)"/>
	<meta name="created" content="00:00:00"/>
	<meta name="changed" content="2024-05-28T11:24:12.964656520"/>
	<meta name="qrichtext" content="1"/>
	<meta name="created" content="00:00:00">
	<meta name="created" content="00:00:00">
	<meta name="created" content="00:00:00">
</head>
<body lang="en-US" text="#000000" link="#000080" vlink="#800000" dir="ltr"><pre class="western"><b>SUIT Colormap</b>
Maintained by- Janmejoy Sarkar, SUIT- Aditya-L1

This project maintatins the colormap for SUIT images.

Filter-names:
[&quot;NB01&quot;, &quot;NB02&quot;, &quot;NB03&quot;, &quot;NB04&quot;, &quot;NB05&quot;, &quot;NB06&quot;, &quot;NB07&quot;, &quot;NB08&quot;, &quot;BB01&quot;, &quot;BB02&quot;, &quot;BB03&quot;]</pre><p style="margin-bottom: 0in">
filterColor[&quot;BB01&quot;]</p>
<p style="margin-bottom: 0in"><img src="README_files/qt_img170316928122886.png" name="Image1" align="bottom" width="512" height="64" border="0"/>

</p>
<p style="margin-bottom: 0in">filterColor[&quot;BB02&quot;]</p>
<p style="margin-bottom: 0in"><img src="README_files/qt_img170372762697734.png" name="Image2" align="bottom" width="512" height="64" border="0"/>

</p>
<p style="margin-bottom: 0in">filterColor[&quot;BB03&quot;]</p>
<p style="margin-bottom: 0in"><img src="README_files/qt_img170428597272582.png" name="Image3" align="bottom" width="512" height="64" border="0"/>

</p>
<p style="margin-bottom: 0in">filterColor[&quot;NB01&quot;]</p>
<p style="margin-bottom: 0in"><img src="README_files/qt_img170523086553094.png" name="Image4" align="bottom" width="512" height="64" border="0"/>

</p>
<p style="margin-bottom: 0in">filterColor[&quot;NB02&quot;]</p>
<p style="margin-bottom: 0in"><img src="README_files/qt_img170656230539270.png" name="Image5" align="bottom" width="512" height="64" border="0"/>

</p>
<p style="margin-bottom: 0in">filterColor[&quot;NB03&quot;]</p>
<p style="margin-bottom: 0in"><img src="README_files/qt_img170922518511622.png" name="Image7" align="bottom" width="512" height="64" border="0"/>

</p>
<p style="margin-bottom: 0in">filterColor[&quot;NB04&quot;]</p>
<p style="margin-bottom: 0in"><img src="README_files/qt_img170789374525446.png" name="Image6" align="bottom" width="512" height="64" border="0"/>

</p>
<p style="margin-bottom: 0in">filterColor[&quot;NB05&quot;]</p>
<p style="margin-bottom: 0in"><img src="README_files/qt_img171055662497798.png" name="Image8" align="bottom" width="512" height="64" border="0"/>

</p>
<p style="margin-bottom: 0in">filterColor[&quot;NB06&quot;]</p>
<p style="margin-bottom: 0in"><img src="README_files/qt_img171188806483974.png" name="Image9" align="bottom" width="512" height="64" border="0"/>

</p>
<p style="margin-bottom: 0in">filterColor[&quot;NB07&quot;] 
</p>
<p style="margin-bottom: 0in"><img src="README_files/qt_img171283295764486.png" name="Image10" align="bottom" width="512" height="64" border="0"/>

</p>
<p style="margin-bottom: 0in">filterColor[&quot;NB08&quot;]</p>
<p style="margin-bottom: 0in"><img src="README_files/qt_img171416439750662.png" name="Image11" align="bottom" width="512" height="64" border="0"/>

</p>
<p><br/>
<br/>

</p>
<pre class="western"><b>Usage</b>:

from colormap import filterColor
from matplotlib.colors import PowerNorm

data= #image data as 2D numpy array
plt.imshow(data, vmin=0, vmax= vmx, cmap= filterColor[filter-name], norm=PowerNorm(0.6,vmin=0), origin='lower')
#Use powernorm for RoI images or if needed.</pre>

</body>
</html>
