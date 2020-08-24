import kivy
kivy.require('1.0.6') # replace with your current kivy version !

from kivy.app import App
from kivy.uix.label import Label

from kivy.uix.boxlayout import BoxLayout
from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import ListProperty
from kivy.clock import Clock

Builder.load_string("""

<Ml>:
    orientation:"vertical"
    Button
        text:"{}".format(root.l[0])
    Button
        text:"{}".format(root.l[0])
    Button
        text:"{}".format(root.l[0])
    Button
        text:"{}".format(root.l[0])
    Button
        text:"{}".format(root.l[0])
    
        
""")
class Ml(BoxLayout):
    l=ListProperty([1,2,3,4,5,6])
    c=0
    def __init__(self, **kwargs):
        super(Ml,self).__init__(**kwargs)
        Clock.schedule_interval(self.timer,1)
    def timer(self,dt):
        self.c+=1
        self.l=[self.c,1,2,3,4,5]
class MyApp(App):
    def build(self):
        return Ml()

if __name__ == '__main__':
    MyApp().run()