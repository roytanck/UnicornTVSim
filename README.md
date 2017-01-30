# UnicornTVSim
Simulate TV with a Raspberry PI and Unicorn HAT. Use the HAT's LEDs to replicate the hue en brightness from your favorite movie frame by frame.

Requirements:
* A Raspberry PI with the Unicorn HAT installed
* Python3
* ffmpeg

Instructions:
* Clone this repository into a folder on your machine
* Add an mp4 file of your favorite movie to the folder (i.e. movie.mp4)
* Create a folder to hold the frames (i.e. 'frames1px')
* Use ffmpeg to convert it to 1*1px images: `ffmpeg -i movie.mp4 -vf scale=1:1 frames1px/frame%06d.png`
* Use convert.py to create the output.txt file, which contains each frame's RGB values
* Use play.py to play back these values on the Unicorn HAT
