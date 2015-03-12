"""

2015-03-04 You Dabin
"""

import os
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

def Draw_Graph_2D(array, init_lat, init_lon, init_hour, max_lat, max_lon, max_minutes):

	print(array)

	x = []
	y = []
	
	for lat in range(0, max_lat):
		for lon in range(0, max_lon):
			if array[lat][lon][max_minutes-1] == 1:
				x.append(lat * 1/max_lat + init_lat)
				y.append(lon * 1/max_lon + init_lon)

	plt.plot(x, y) # draw line
	plt.plot(x, y, 'ko') # draw dots
	plt.margins(0.2)
	plt.xlabel('latitude')
	plt.ylabel('longitude')

	plt.show()

if __name__ == '__main__':
	array = np.zeros((3, 3))
	Draw_Graph_2D(array, 100, 100, 100, 100, 100, 100)
	
