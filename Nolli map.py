# -*- coding: utf-8 -*-
"""
Created on Thu Jul 13 14:26:54 2017

@author: yangjinyue
"""

import osmnx as ox
from IPython.display import Image
ox.config(log_file=True, log_console=True, use_cache=True)

img_folder = 'images'
extension= 'png'
size = 800

place = 'chongqing'
point= (42.911968,129.51879)
fig, ax = ox.plot_figure_ground(point=point, dist=2000, filename=place, network_type='all', dpi=150)
Image('{}/{}.{}'.format(img_folder, place, extension), height=size,width=size)
