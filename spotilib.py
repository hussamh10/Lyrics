import win32gui
import win32api
import os

def getwindow(Title="SpotifyMainWindow"):
	window_id = win32gui.FindWindow(Title, None)
	return window_id
	
def song_info():
	try:
		song_info = win32gui.GetWindowText(getwindow())
	except:
		pass
	return song_info

def artist():
	try:
		temp = song_info()
		artist, song = temp.split("-",1)
		artist = artist.strip()
		return artist
	except:
		return "There is noting playing at this moment"
	
def song():
	try:
		temp = song_info()
		artist, song = temp.split("-",1)
		song = song.strip()
		return song
	except:
		return "There is noting playing at this moment"

