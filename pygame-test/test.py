#!/usr/bin/python3

import pygame
from flask import Flask

app = Flask(__name__)

@app.route("/play")
def play():
	pygame.mixer.music.load('./musics/02.ogg')
	pygame.mixer.music.play(0)
	return "playing"
@app.route("/stop")
def stop():
	pygame.mixer.music.stop()
	return "stoped"

if __name__ == "__main__":
	pygame.init()
	app.run()



