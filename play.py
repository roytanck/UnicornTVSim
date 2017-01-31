#!/usr/bin/python3

from PIL import Image
import datetime, time, threading
import unicornhat as unicorn

input_file = open("output.txt", "r")

# start up the unicorn hat
unicorn.set_layout(unicorn.HAT)
unicorn.rotation(90)
unicorn.brightness(1)
unicorn.off()

# read the file's content instead of using readline in aech iteration
contents = input_file.read()
lines = contents.split('\n')
index = 0

# keep track of the script's timing
starttime = time.time()

# use threading to get a reasonably precise timing (http://stackoverflow.com/a/8600301)
def processline():
	next_call = time.time()
	while True:
		#print ( datetime.datetime.now() )
		global index
		line = lines[index]
		# for testing: every 250 frames, report the framerate
		if index%250 == 0 and index != 0:
			global starttime
			time_passed = time.time() - starttime
			starttime = time.time()
			print( 250/time_passed )
		index = (index + 1) % len(lines)
		# line = input_file.readline()
		values = line.rstrip('\r\n').split(',')
		# print ( 'R:' + str(values[0]) + ' G:' + str(values[1]) + ' B:' + str(values[2]) )
		for y in range(8):
			for x in range(8):
				unicorn.set_pixel(x,y,int(values[0]),int(values[1]),int(values[2]))
		unicorn.show()

		next_call = next_call+0.04
		time.sleep(next_call - time.time())

timerThread = threading.Thread(target=processline)
#timerThread.daemon = True
timerThread.start()
