#_*_ coding: utf-8 _*_

"""
1. gpx파일에서 필요한 데이터만을 모아서 txt파일로 변환합니다.

2015-03-02 유다빈
"""

from sys import argv
from os.path import exists
import os

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
				out_file.write(lat) 
				out_file.write("\t")
			elif ward[i].find('lon="') != -1: 
				lon = ward[i][len('lat="'):len(ward[i])-len('">')]
				out_file.write(lon) 
				out_file.write("\t")
			elif ward[i].find('<time>') != -1: 
				date = ward[i][len('<time>'):len(ward[i])-len('</time>')]
				out_file.write(date)
				out_file.write("\n") 

	# Close file
	out_file.close()
	in_file.close()

if __name__ == '__main__':
	root = "/home/ydb2002/Desktop/Project/Step1"
	for (path, dirs, fnames) in os.walk(root):
		for fname in fnames:
			if fname[-3:] == "gpx":
				Change_file(fname)
	
