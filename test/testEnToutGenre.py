import os
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide"
from pygame import mixer
from pygame import USEREVENT
from pygame import event
from random import randint
import ctypes
import sys
import pygame
import time

absPath = os.path.abspath("") + "/Murloc.mp3"
stop = False

pygame.init()

mixer.init()
MUSIC_END = USEREVENT+1
mixer.music.set_endevent(MUSIC_END)


mixer.music.load(absPath)

mixer.music.play()

while stop == False:
	for event in pygame.event.get():
		if event.type == MUSIC_END:
		    print('music end event')
		    stop = True
