from lyrics import getLyrics
from metaData import getArtistInfo
from metaData import getSongInfo
import spotilib

artist = spotilib.artist()
song = spotilib.song()

print(getLyrics(artist, song))


