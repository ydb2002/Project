#_*_ coding: utf-8 _*_

"""
1. gpx파일에서 필요한 데이터만을 모아서 txt파일로 변환합니다.

2015-03-02 유다빈
"""

from sys import argv
from os.path import exists
import os

def Change_Point(number):
	# init
	n = 3
	m = 1

	for i in range(0, 3):
		m = m * 10

	temp_num1 = round(float(number), n)
	temp_num2 = int(number)
	number = (temp_num1 - temp_num2) * m

	return int(number)

def Change_file(filename):
	# Open file
	in_file = open(filename, 'r')
	out_file = open(filename[:-3] + "txt", 'w')

	#Write file
	while 1:
		ward = in_file.read().split()
		if not ward : break

		for i in range(0, len(ward)):
			if ward[i].find('lat="') != -1: 
				lat = ward[i][len('lat="'):len(ward[i])-len('"')]
				lat = Change_Point(float(lat))
				out_file.write(str(lat)) 
				out_file.write("\t")
			elif ward[i].find('lon="') != -1: 
				lon = ward[i][len('lat="'):len(ward[i])-len('">')]
				lon = Change_Point(float(lon))
				out_file.write(str(lon)) 
				out_file.write("\t")
			elif ward[i].find('<time>') != -1: 
				time = ward[i][len('<time>'):len(ward[i])-len('</time>')]
				out_file.write(time)
				out_file.write("\n") 

	# Close file
	out_file.close()
	in_file.close()

if __name__ == '__main__':
	root = "/home/ydb2002/Desktop/Project/Step2"
	for (path, dirs, fnames) in os.walk(root):
		for fname in fnames:
			if fname[-3:] == "gpx":
				Change_file(fname)
	
