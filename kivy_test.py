import kivy
kivy.require('1.0.6') # replace with your current kivy version !

from metaData import getArtistInfo
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.widget import Widget
from kivy.uix.button import Button
from kivy.config import Config
from kivy.uix.image import AsyncImage
from kivy.core.window import Window
from kivy.uix.floatlayout import FloatLayout
import urllib

Config.set('graphics','position','custom')
Window.size = (500, 750)

class MyApp(App):

    def build(self):
        layout = FloatLayout(size = (500, 300))
        self.painter = Label(text="asdfdf")
        image = getArtistInfo('Katy Perry')['image']
        img = urllib.urlretrieve(image, 'ok.jpeg')
        aimg = AsyncImage(source = 'c:\\Users\\hussamh10\\Desktop\\Lyrics\\ok.jpeg', size_hint=(.4, .4), pos=(15, 480))
        clearbtn = Button(
            text='Hello world',
            size_hint=(.5, .25),
            pos=(0, 200))
        layout.add_widget(self.painter)
        layout.add_widget(aimg)
        layout.add_widget(clearbtn)
        return layout

if __name__ == '__main__':
    MyApp().run()
