from kivy.lang import Builder
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label

Builder.load_string("""
<Graph>:
    # x_text
    GraphTabel
        size_hint:.9,.9
        pos_hint:{"top":1,"right":1}
    Label:
        size_hint:1,.05
        text:"rpm"
        font_size:self.height/1.2
        valign:"bottom"
        text_size:self.size
        halign:"center"
<Xlabel>:
    orientation:"vertical"
    Xline:
        pos_hint:{"center_x":.5,"center_y":.5}
        size_hint:None,.25
    Label
        font_size:self.height/2.2
        text:root.text
        halign:"right"
        valign:"middle"
        text_size:self.size
<Ylabel>:
    Label
        font_size:self.height/2.2
        text:root.text
    # Xline
    #     warna:0,1,1,.2
    Yline:
        pos_hint:{"center_x":.5,"center_y":.5}
        size_hint:.2,None
<Yline>:
    size_hint:1,None
    height:"1sp"
    warna:1,1,1,1
    canvas:
        Color:
            rgba:root.warna
        Rectangle:
            size:self.size
            pos:self.pos
<Xline>:
    size_hint:None,1
    width:"1sp"
    warna:1,1,1,1
    canvas:
        Color:
            rgba:root.warna
        Rectangle:
            size:self.size
            pos:self.pos

<Yline>:
<GraphTabel>:
    g:g
    xline:xline
    yline:yline
    xlabel:xlabel
    ylabel:ylabel
    FloatLayout:
        pos_hint:{"center_x":.5,"center_y":.5}
        Label:
            text:root.x_title
            size_hint:1,.05
            font_size:self.height/1.8
            halign:"center"
            valign:"bottom"
            text_size:self.size
            pos_hint:{"center_x":.5,"y":0}
        Label:
            halign:"left"
            valign:"middle"
            text:root.y_title
            size_hint:.05,1
            pos_hint:{"x":0,"center_y":.5}
            canvas.before:
                PushMatrix
                Rotate:
                    angle:90
                    origin: self.center
                    axis: 0, 0, 1
            canvas.after:
                PopMatrix
        FloatLayout:
            size_hint:.9,.9
            pos_hint:{"right":1,"top":1}
            id:g
            BoxLayout:
                orientation:"vertical"
                size_hint:.1,1
                id:ylabel
                pos_hint:{"x":-.07,"y":0}
            BoxLayout:
                size_hint:1,.12
                id:xlabel
                pos_hint:{"x":0,"y":-.08}
            Yline:
                pos:g.pos[0],  (g.pos[1]+g.size[1]/root.ygrid*root.tps/10)+root.add_y
                id:yline
            Xline:
                pos:(g.pos[0]+g.size[0]/root.xgrid*root.rpm/1000)+root.add_x  , g.pos[1]
                id:xline
            BoxLayout
                orientation:"vertical"
                size_hint:1,.15
                pos:xline.pos[0],yline.pos[1]
                Label:
                    text:" rpm: {}".format(root.rpm)
                    font_size:self.height/1.5
                    halign:"left"
                    valign:"middle"
                    text_size:self.size
                Label:
                    text:" tps: {}".format(root.tps)
                    font_size:self.height/1.5
                    halign:"left"
                    valign:"middle"
                    text_size:self.size
                Label:
                    text:" inj: {}".format(root.inj)
                    font_size:self.height/1.5
                    halign:"left"
                    valign:"middle"
                    text_size:self.size
                

""")
from kivy.uix.floatlayout import FloatLayout
from kivy.properties import NumericProperty,ListProperty,StringProperty
class Xlabel(BoxLayout):
    # pass
    text=StringProperty("")
class Ylabel(BoxLayout):
    text=StringProperty("")
class Xline(Label):
    pass
class Yline(Label):
    pass
from kivy.clock import Clock
class GraphTabel(FloatLayout):
    xgrid=NumericProperty(13)
    c=NumericProperty(0)
    ygrid=NumericProperty(11)
    add_x=NumericProperty(0)
    add_y=NumericProperty(0)
    rpm=NumericProperty(0)
    tps=NumericProperty(0)
    inj=NumericProperty(0)
    x_title=StringProperty("rpm x 1000")
    y_title=StringProperty("tps")
    def __init__(self, **kwargs):
        super(GraphTabel,self).__init__(**kwargs)
        Clock.schedule_once(self.delay,.5)
    def delay(self,dt):
        for i in range(self.xgrid):
            self.xlabel.add_widget(Xlabel(text=str(i)))
        for i in range(self.ygrid):
            self.ylabel.add_widget(Ylabel(text=str(i)))
        self.ylabel.children.reverse()
        Clock.schedule_once(self.delay2,.5)
    def delay2(self,dt):
        self.add_x=self.xlabel.children[0].size[0]/2
        self.add_y=self.ylabel.children[0].size[1]/2
    def timer(self,dt):
        self.rpm+=10
        self.tps+=.1
        print(self.rpm)
class Graph(FloatLayout):
    def __init__(self, **kwargs):
        super(Graph,self).__init__(**kwargs)

from kivy.app import App
class My(App):
    def build(self):
        return GraphTabel()

if __name__=="__main__":
    My().run()
