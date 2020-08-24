from kivy.uix.floatlayout import FloatLayout
from kivy.properties import NumericProperty,DictProperty
from kivy.lang import Builder
from kivy.clock import Clock
from css import *
Builder.load_file("tabel.kv")
class Tabel(FloatLayout):
    D=DictProperty({})
    def __init__(self, **kwargs):
        super(Tabel,self).__init__(**kwargs)
        Clock.schedule_once(self.delay,1)
    def delay(self,dt):
        self.ids["bv"].size_hint=1,len(self.ids["bv"].children)*.085
    def resize(self,data):
        pass
    