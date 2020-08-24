from kivy.lang import Builder
from kivy.uix.floatlayout import FloatLayout
from kivy.app import App
from css import *
from kivy.config import Config
Config.set('graphics', 'height', 370)
Config.set('graphics', 'width', 770)
Builder.load_string('''
<Dash>:
    pop:pop
    pos_hint:{"center_x":.5,"center_y":.5}
    Kotak:
        source:"img/KIRI.png"
        size_hint:None,None
        size:1.2*(329/536)*min(root.size),1*min(root.size)
        pos_hint:{"x":0,"center_y":.5}
        BV:
            padding:10,0,0,0
            size_hint:.6,.5
            pos_hint:{"x":0,"center_y":.51}
            ItemBig
                value:0
                svalue:"0"
                key:"o2"
                unit:"volt"
                on_parent:root.G[3]=self
            ItemBig
                value:0
                svalue:"0"
                key:"stf"
                unit:"lamda"
                on_parent:root.G[4]=self
            ItemBig
                value:0
                svalue:"0"
                key:"afr"
                unit:" : 1"
                on_parent:root.G[5]=self
        BH:
            id:inj
            size_hint:.5,.075
            pos_hint:{"center_x":.6,"y":.12}
            Label:
                font_name:"fonts/hemi.ttf"
                font_size:min(self.size)
                text:"{:.1f}".format(root.inj)
            Label:
                text:"INJ"
                font_name:"fonts/hemi.ttf"
                font_size:min(self.size)/1.5
                color:0,1,1,1
    Kotak
        source:"img/KANAN.png"
        size_hint:None,None
        size:1.2*(329/536)*min(root.size),1*min(root.size)
        pos_hint:{"right":1,"center_y":.5}
        BV:
            padding:0,0,10,0
            size_hint:.6,.5
            pos_hint:{"right":1,"center_y":.51}
            ItemBig
                value:0
                svalue:"0"
                key:"battery"
                unit:"volt"
                on_parent:root.G[0]=self
            ItemBig
                value:0
                svalue:"0"
                key:"iat"
                unit:"[sup]o [/sup]c"
                on_parent:root.G[1]=self
            ItemBig
                value:0
                svalue:"0"
                key:"map"
                unit:"kpa"
                on_parent:root.G[2]=self
        Image:
            source:"img/batt.png"
            pos_hint:{"right":.88,"top":.825}
            size_hint:.1,.15
            color:1,1,1,.1
            on_parent:root.I[4]=self
        BH:
            id:adv
            size_hint:.5,.07
            pos_hint:{"center_x":.4,"y":.12}
            Label:
                text:"ADV"
                font_name:"fonts/hemi.ttf"
                font_size:min(self.size)/1.5
                color:0,1,1,1
            Label:
                text:"{}".format(root.adv)
                font_name:"fonts/hemi.ttf"
                font_size:min(self.size)
    Kotak:
        id:bl
        size_hint:None,None
        source:"img/tengah.png"
        size:1.17*min(root.size),min(root.size)
        pos_hint:{"center_x":.5,"center_y":.5}
        Bulat:
            size_hint:.9*1/1.18, .9*1
            pos_hint:{"center_x":.5,"center_y":.5425}
            source:"img/ongko.png"
            Kotak:
                warna:1,0,0,1
                size_hint:.04,.8
                color:1,0,0,.5
                source:"img/arrow.png"
                pos_hint:{"center_x":.5,"center_y":.5}
                canvas.before:
                    PushMatrix
                    Rotate:
                        angle: 108-root.angle_rpm*(180/root.max_rpm)
                        origin: self.center
                canvas.after:
                    PopMatrix
        Bulat:
            size_hint:.34*1/1.18, .34*1
            pos_hint:{"center_x":.5,"center_y":.5425}
            warna:0,0,0,1
            LabelBatmfa:
                text:"rpm"
                pos_hint:{"center_x":.5,"center_y":.85425}
                font_size:min(self.size)/7
                color:0,1,1,1
            LabelFish:
                text:"{:.0f}".format(root.rpm)
                pos_hint:{"center_x":.5,"center_y":.5425}
                font_size:min(self.size)/2
        Bulat:
            size_hint:.24,.1
            pos_hint:{"center_x":.5,"center_y":.27}
            warna:0,0,0,1
            LabelBatmfa:
                size_hint:1,.5
                text:"speed"
                pos_hint:{"center_x":.5,"top":1}
                font_size:min(self.size)/1.2
                color:1,1,1,.7
            LabelLcd:
                text:"{}".format(root.vss)
                pos_hint:{"center_x":.5,"center_y":.1}
                font_size:min(self.size)
        LineBulat
            max:100
            value:root.tps
            tebal:min(self.size)/30
            angle_start:220
            angle_end:220+ self.value*(160/self.max)
            size_hint:.8,.8
            warna:0,1,1,1
            size_hint:.3*1/1.18 ,.3*1
            pos_hint:{"center_x":.76,"center_y":.375}
            Label:
                text:"{:.0f}".format(self.parent.value)
                pos_hint:{"center_x":.5,"center_y":.55}
                font_name:"fonts/fish.ttf"
                font_size:min(self.size)/4
                color:0,1,1,1
            Label:
                text:"tps"
                pos_hint:{"center_x":.5,"center_y":.79}
                font_name:"fonts/hemi.ttf"
                font_size:min(self.size)/7
                color:0,0,0,1
        BH:
            pos_hint:{"center_x":.5,"y":0.01}
            size_hint:.5,.15
            spacing:self.width/22
            BtnModern:
                on_press:root.show_info_model()
        BH:
            pos_hint:{"center_x":.5,"y":0.01}
            size_hint:1,.06
            spacing:self.width/22
            LabelModern:
                text:"{}  .".format(root.model)
                halign:"right"
                valign:"middle"
                text_size:self.size
                font_size:min(self.size)/1.2
                markup:True
            LabelModern
                text:"  {:.0f}[sup]  O [/sup]c".format(root.temp)
                font_size:min(self.size)/1.2
                halign:"left"
                valign:"middle"
                text_size:self.size
                markup:True
    BoxLayout:
        size_hint:.15,.07
        pos_hint:{"center_x":.205,"y":.8}
        BtnImg
            source:"img/mil.png"
            color:1,1,1,.3
            on_parent:root.I[0]=self
            on_press:
                root.show_eror()
        Image
            source:"img/fan.png"
            color:1,1,1,.1
            on_parent:root.I[1]=self
    BoxLayout:
        size_hint:.15,.07
        pos_hint:{"center_x":.795,"y":.8}
        LabelBatmfa
            text:"N"
            color:0,1,0,1
            on_parent:root.I[2]=self
            font_size:self.height
        Image
            source:"img/jagang.png"
            color:1,1,1,.1
            on_parent:root.I[3]=self
    Pop:
        id:pop
        konten:root.data_eror
        on_hapus:root.cc()
    PopInfo:
        id:popinfo
        tittle:"info"
        message1:"anda terhubung dengan "
        message2:root.model
        message3:root.years
        message4:root.pn

''')
from kivy.animation import Animation
from kivy.properties import NumericProperty,StringProperty,ListProperty,DictProperty
from kivy.clock import Clock
class Dash(FloatLayout):
    clock=Clock
    tg=NumericProperty(0)
    I=DictProperty({})
    angle_rpm=NumericProperty(0)
    temp=NumericProperty(0)
    tps=NumericProperty(0)
    vss=NumericProperty(0)
    rpm=NumericProperty(0)
    inj=NumericProperty(0)
    adv=NumericProperty(0)
    max_rpm=NumericProperty(12000)
    G=DictProperty({})
    data_eror=StringProperty("")
    model=StringProperty("auto")
    years=StringProperty("")
    pn=StringProperty("")
    def __init__(self, **kwargs):
        self.register_event_type("on_hapus_dtc")
        super(Dash,self).__init__(**kwargs)
        self.anim = Animation(angle_rpm=self.rpm, duration=.3) 
        self.clock.schedule_interval(self.timer,.3)
        self.anim.start(self)
    def timer(self,dt):
        self.anim.start(self)
        self.anim = Animation(angle_rpm=self.rpm, duration=.7) 
    def show_eror(self):
        self.pop.pos_hint={"center_x":.5,"center_y":.5}
    def show_info_model(self):
        self.ids["popinfo"].pos_hint={"center_x":.5,"center_y":.5}
    def cc(self):
        self.dispatch("on_hapus_dtc")

    def on_hapus_dtc(self):
        pass