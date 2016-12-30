import spotilib
from lyrics import getLyrics
from metaData import getArtistInfo

artist = spotilib.artist()
song = spotilib.song()

print(getArtistInfo(artist))
print(getLyrics(artist, song))
