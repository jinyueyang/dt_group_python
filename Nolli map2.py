# -*- coding: utf-8 -*-
"""
Created on Thu Jul 27 15:32:11 2017

@author: yangjinyue
"""

import osmnx as ox
from IPython.display import Image
ox.config(log_file=True, log_console=True, use_cache=True)

img_folder = 'images'
extension= 'png'
size = 600

point = (35.691502,139.703481)
dist = 2000
gdf = ox.buildings_from_point(point=point, distance=dist, retain_invalid=True)
gdf_proj = ox.project_gdf(gdf)
bbox = ox.bbox_from_point(point=point, distance=dist, project_utm=True)
fig, ax = ox.plot_buildings(gdf_proj, bgcolor='#333333', color='w', figsize=(8,8), bbox=bbox,
                            save=True, show=False, close=True, filename='paris_bldgs', dpi=150)
Image('{}/{}.{}'.format(img_folder, 'paris_bldgs', extension), height=size, width=size)