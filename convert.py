#!/usr/bin/python3

from PIL import Image

# open the ouput file
output_file = open("output.txt", "w")
# remove any existing content (http://stackoverflow.com/a/17126137)
output_file.seek(0)
output_file.truncate()

# loop through frames
#for i in range(11000,11050):
for i in range(1,183217):
	im = Image.open('frames1px/frame' + str( "{0:0>6}".format(i) ) + '.png')
	px = im.load()
	#print (px[0,0])
	values_str = str( px[0,0][0] ) + ',' + str( px[0,0][1] ) + ',' + str( px[0,0][2] )
	print ( values_str )
	output_file.write( values_str + "\n" )

output_file.close()
