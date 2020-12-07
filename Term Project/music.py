from pico2d import *
import game_object

def mp3(music_name, repeat):
	bgm = load_music(music_name)
	bgm.set_volume(64)

	if repeat:
		bgm.repeat_play()
	else:
		bgm.play()

	return bgm

def wav(se_name, repeat):
	se = load_wav(se_name)
	se.set_volume(128)

	if repeat:
		se.repeat_play()
	else:
		se.play()

	return se