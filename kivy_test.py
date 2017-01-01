import kivy
kivy.require('1.0.6') # replace with your current kivy version !

from metaData import getArtistInfo
from lyrics import getLyrics
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.widget import Widget
from kivy.uix.button import Button
from kivy.config import Config
from kivy.uix.image import AsyncImage
from kivy.core.window import Window
from kivy.uix.floatlayout import FloatLayout
from kivy.lang import Builder
import urllib
import spotilib

Config.set('graphics','resizable', 0)
Window.size = (500, 750)

class MyApp(App):

    def getArtistImage(self, img_url, artist):
        artist = artist.replace(' ', '_')
        img_src = 'c:\\Users\\hussamh10\\Desktop\\Lyrics\\' + artist + '.jpeg'
        urllib.urlretrieve(img_url, img_src)
        return img_src

    def addArtistImage(self, layout, img_url, artist):
        #img_src = self.getArtistImage(img_url, artist)
        img_src = 'c:\\Users\\hussamh10\\Desktop\\Lyrics\\' + artist + '.jpeg'
        img = AsyncImage(source = img_src, size_hint=(.4, .4), pos=(15, 480))
        layout.add_widget(img)

    def addSongInfo(self, layout, artist, song):
        song_lb = Label(text='[color=757575]' + song + '\n' + artist['name'] + '[/color]', markup = True, font_size = '15sp', halign='left', pos=(80, 300))
        layout.add_widget(song_lb)


    def build(self):
        layout = FloatLayout(size = (500, 300))

        song = spotilib.song()
        artist = spotilib.artist()
        artist_data = getArtistInfo(artist)             # name, image, genre


        self.addArtistImage(layout, artist_data['image'], artist)
        self.addSongInfo(layout, artist_data, song)
        #addLyrics(layout, artist, song)

        return layout

if __name__ == '__main__':
    MyApp().run()
