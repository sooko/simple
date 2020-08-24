from kivy.lang import Builder
from kivy.uix.floatlayout import FloatLayout
from kivy.app import App
from kivy.properties import StringProperty,NumericProperty,ListProperty,DictProperty
from kivy.config import Config
Config.set('graphics', 'height', 370)
Config.set('graphics', 'width', 770)
from css import LabelCavian
from jajal import *
from tg import GraphTabel
# from tabel import tabel

Builder.load_string("""
<Chart>:
    background_color:0,0,0,0
    x_ticks_minor:2
    y_ticks_minor:2
    x_ticks_major:2
    y_ticks_major:20
    y_grid_label:True
    x_grid_label:True
    x_grid:False
    y_grid:False
    ylabel:"tps"
    xlabel:"rpm x 1000"
    xmin:0
    xmax:12
    ymin:0
    ymax:100
    border_color:0,0,0,0
    tick_color:0,1,1,1
    color:0,1,1,1
<LineCircle@FloatLayout>:
    angle_end:0
    angle_start:360
    tebal:1.5
    warna:0,1,1,1
    pos_hint:{"center_x":.5,"center_y":.5}
    canvas:
        Color:
            rgba:root.warna
        Line:
            width:root.tebal
            circle:
                (self.center_x, self.center_y, min(self.width, self.height)
                / 2,root.angle_start,root.angle_end)
<Dial@FloatLayout>:
    pos_hint:{"center_x":.5,"center_y":.5}
    LineCircle:
        pos_hint:{"center_x":.5,"center_y":.5}
        angle_start:220
        angle_end:220+50
        LineCircle: 
            pos_hint:{"center_x":.5,"center_y":.5}
            size_hint:.9,.9
            LineCircle
                tebal:1
                size_hint:.9,.9
                Label:
                    text:"14000"
                    font_name:"fonts/fish.ttf"
                    font_size:self.height/3
                    color:0,1,1,1
                    pos_hint:{"center_x":.5,"center_y":.5}
                Label:
                    text:"RPM"
                    font_name:"fonts/batmfa.ttf"
                    font_size:self.height/8
                    color:0,1,1,1
                    pos_hint:{"center_x":.5,"center_y":.8}
        
<LineVer@Label>:
    size_hint:1,None
    pos_hint:{"center_x":.5,"center_y":.5}
    height:"1sp"
    canvas:
        Color
            rgba:0,1,1,1
        Rectangle:
            size:self.size
            pos:self.pos
<LineHor@Label>:
    size_hint:None,1
    width:"1sp"
    canvas:
        Color
            rgba:0,1,1,1
        Rectangle:
            size:self.size
            pos:self.pos

<Dash>:
    size_hint:.99,.99
    pos_hint:{"center_x":.5,"center_y":.5}
    canvas:
        Color:
            rgba: 0,1,1,1
        Line:
            width: 1
            rectangle: (self.x, self.y, self.width, self.height)
    BoxLayout:
        pos_hint:{"center_x":.5,"center_y":.5}
        orientation:"vertical"
        Label:
            text:"sooko.io"
            font_name:"fonts/hemi.ttf"
            font_size:self.height/1.2
            halign:"left"
            valign:"top"
            text_size:self.size
            color:0,1,1,1
            size_hint:1,.1
        BoxLayout
            pos_hint:{"center_x":.5,"center_y":.5}
            padding:2
            BoxLayout:
                size_hint:.2,1
                orientation:"vertical"
                BoxLayout:
                    orientation:"vertical"
                    Label
                        size_hint:1,.091
                        text:" DATA LOGER"
                        font_size:self.height/1.8
                        font_name:"fonts/cn.ttf"
                        color:0,1,1,1
                        halign:"left"
                        text_size:self.size
                        valign:"middle"
                    ScrollView:
                        size_hint:.9,1
                        pos_hint:{"right":1}
                        Label:
                            id:lbl
                            size_hint:1,1.5
                            pos_hint:{"right":1}
                            text:root.dataloger
                            text_size:self.size
                            halign:"left"
                            valign:"top"
                            font_name:"fonts/consola.ttf"
                            font_size:self.height/27
                            color:0,1,1,1
                            readonly:True
                            foreground_color:0,1,1,1
                            background_color:0,0,0,0
            
            BoxLayout:
                orientation:"vertical"
                BoxLayout:
                    FloatLayout
                        size_hint:.8,1
                        Dial
                            size_hint:1,.8
                            pos_hint:{"center_x":.5,"top":1}
                    BoxLayout:
                        orientation:"vertical"
                        FloatLayout:
                            id:gr
                            GraphTabel:
                                pos_hint:{"center_x":.5,"center_y":.5}
                                id:chart
                        Label
                            size_hint:1,.4

""")
from kivy.clock import Clock
class Dash(FloatLayout):
    model=StringProperty("")
    pn=StringProperty("")
    years=StringProperty("")
    rpm=NumericProperty(0)
    ect=NumericProperty(0)
    vss=NumericProperty(0)
    tps=NumericProperty(100)
    inj=NumericProperty(0)
    adv=NumericProperty(0)
    bat=NumericProperty(0)
    o2=NumericProperty(0)
    bas=NumericProperty(0)
    dataloger=StringProperty("rpm :0\ntps :0\nect :0\n")
    def __init__(self, **kwargs):
        super(Dash,self).__init__(**kwargs)
    #     self.ids["chart"].add_plot(self.plot_x)
    #     self.ids["chart"].add_plot(self.plot_y)
    #     # Clock.schedule_interval(self.timer,1)
    # def timer(self,dt):
    #     print(self.ids["chart"].size)
    #     print(self.ids["chart"].pos)
       
        
class M(App):
    def build(self):
        return Dash()
if __name__=="__main__":
    M().run()