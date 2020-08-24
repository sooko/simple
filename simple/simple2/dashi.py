from kivy.lang import Builder
from kivy.config import Config
Config.set('graphics', 'height', 370)
Config.set('graphics', 'width', 770)
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.app import App

Builder.load_string("""
<RecImg@FloatLayout>:
    warna:1,1,1,1
    lebar:1
    tinggi:1
    source:""
    FloatLayout:
        pos_hint:root.pos_hint
        size_hint:None,None
        size:root.lebar*min(root.size),root.tinggi*min(root.size)
        canvas:
            Color:
                rgba:root.warna
            Rectangle:
                size:self.size
                pos:self.pos
                source:root.source
<CircImg@FloatLayout>:
    lebar:1
    tinggi:1
    warna:1,1,1,1
    source:""
    angle_start:0
    angle_end:360
    FloatLayout:
        pos_hint:root.pos_hint
        size_hint:None,None
        size:root.lebar*min(root.size),root.tinggi*min(root.size)
        canvas:
            Color:
                rgba:root.warna
            Ellipse:
                size:self.size
                pos:self.pos
                source:root.source
                angle_start:root.angle_start
                angle_end:root.amgle_end
<Kanan@FloatLayout>:
    RecImg:
        lebar:1/2
        tinggi:1
        source:"img/kanan.png"
        pos_hint:{"right":1,"center_y":.5}

<Kiri@FloatLayout>:
    RecImg:
        lebar:1/1.86
        tinggi:1
        source:"img/kiri.png"
        pos_hint:{"x":0,"center_y":.5}


<Tengah@FloatLayout>:
    RecImg:
        lebar:1.17/1
        tinggi:1
        source:"img/tengah.png"
        pos_hint:{"center_x":.5,"center_y":.5}




<Dash>:
    Kanan
    Kiri
    Tengah
    


""")


class Dash(FloatLayout):
    def __init__(self, **kwargs):
        super(Dash,self).__init__(**kwargs)

class M(App):
    def build(self):
        return Dash()


if __name__=="__main__":
    M().run()