"""
To change location data to array

2015-03-04
"""

import os
from sys import argv
import numpy as np
import matplotlib.pyplot as plt
#from Draw_2D import Draw_Graph_2D

def Draw_Graph_2D(array, init_lat, init_lon, init_hour, max_lat, max_lon, max_minutes):

	x = []
	y = []
	
	for lat in range(0, max_lat):
		for lon in range(0, max_lon):
			if array[lat][lon][max_minutes-1] == 1:
				x.append(float(lat*max_lat) + init_lat)
				y.append(float(lon*max_lon) + init_lon)

	#plt.plot(x, y) # draw line
	plt.plot(x, y, 'ko') # draw dots
	plt.margins(0.2)
	plt.xlabel('latitude')
	plt.ylabel('longitude')

	plt.show()

def Change_data(filename):
	
	#define init
	init_lat = 37
	init_lon = 126
	init_hour = 14

	#define limit
	max_lat = 1000
	max_lon = 1000
	max_minutes = 60

	#define coodinate
	x = max_lat
	y = max_lon
	z = max_minutes
	xy = max_lat * max_lon
	xyz = xy * z 

	#make array
	array = np.zeros((x,y,z))

	#mapping
	in_file = open(filename, 'r')
	
	while 1:
		ward = in_file.read().split()
		if not ward : break
	
		for i in range(0, len(ward)/3):
			lat = int(ward[3*i])
			lon = int(ward[3*i+1])
			#time = ward[3*i+2]
			array[lat][lon][z-1] = 1
	
	#print(array)
	Draw_Graph_2D(array, init_lat, init_lon, init_hour, max_lat, max_lon, max_minutes)

if __name__ == '__main__' :
	script, filename = argv
	Change_data(filename)

