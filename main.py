import os
import random
import spotilib
from lyrics import getLyrics

def generateMessage():
    file = open('C:\\Users\\hussamh10\\Desktop\\Lyrics\\funnies', 'r')
    messages = file.readlines()
    message = "Please wait, " + random.choice(messages)
    return message

def main():
    os.system('cls')
    print generateMessage()

    artist = spotilib.artist()
    song = spotilib.song()

    lyrics = getLyrics(artist, song)
    os.system('cls')
    print(lyrics)

main()
