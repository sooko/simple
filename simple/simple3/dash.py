from kivy.lang import Builder
from kivy.uix.floatlayout import FloatLayout
from kivy.app import App
from kivy.config import Config
Config.set('graphics', 'height', 370)
Config.set('graphics', 'width', 770)
from css import *
Builder.load_string("""
#:import math math
<PopEror>:
    pos_hint:{"center_x":.5,"center_y":5}
    Button:
        background_color:0,0,0,.9
        pos_hint:{"center_x":.5,"center_y":.5}
        on_press:
            root.pos_hint={"center_x":.5,"center_y":5}
    FloatLayout:
        size_hint:.9,.9
        pos_hint:{"center_x":.5,"center_y":.5}
        Button
            pos_hint:{"center_x":.5,"center_y":.5}
            background_color:0,0,0,1
            canvas:
                Color:
                    rgba:0,1,1,1
                Rectangle:
                    source:"img/frame.png"
                    size:self.size
                    pos:self.pos
                    
        BV:
            pos_hint:{"center_x":.5,"center_y":.5}
            padding:20
            Label:
                size_hint:1,.1
                text:"DTC"
                font_size:self.height/1.5
                font_name:"fonts/batmfa.ttf"
                color:0,1,1,1
            Label:
                text:root.text_eror
                halign:"left"
                valign:"top"
                text_size:self.size
            BoxLayout:
                spacing:self.width/5
                size_hint:1,.2
                BtnMono:
                    font_name:"fonts/cavian.ttf"
                    text:"Clear Dtc"
                    font_size:self.height/3
                    on_press:root.clear()
                BtnMono:
                    font_name:"fonts/cavian.ttf"
                    text:"Exit"
                    font_size:self.height/3
                    on_release:root.pos_hint={"center_x":.5,"center_y":5}
                
<ItemBig@FloatLayout>:
    key:"rpm"
    svalue:"100"
    value:0
    unit:"kph"
    max:100
    pgvalue:0
    BoxLayout
        pos_hint:{"right":1,"center_y":.5}
        orientation:"vertical"
        size_hint:1,.9
        Label
            size_hint:1,.4
            text:root.key
            font_size:self.height/1.1
            font_name:"fonts/batmfa.ttf"
            halign:"left"
            valign:"middle"
            text_size:self.size
            color:1,1,1,.7
        BoxLayout
            Label
                color:0,1,1,1
                text:root.svalue
                font_size:self.height*1.2
                font_name:"fonts/lcd_b.ttf"
            Label:
                text:root.unit
                font_name:"fonts/consola.ttf"
                font_size:self.height/2.5
                halign:"center"
                valign:"bottom"
                text_size:self.size
                color:1,1,1,.7
                markup:True
        ProgressBar
            size_hint:1,.3
            pos_hint:{"right":1}
            value:root.value
            max:root.max

<ItemBig2@FloatLayout>:
    key:"rpm"
    svalue:"100"
    value:0
    unit:"kph"
    max:100
    pgvalue:0
    BoxLayout
        pos_hint:{"right":1,"center_y":.5}
        orientation:"vertical"
        size_hint:.8,.9
        Label
            size_hint:1,.4
            text:root.key
            font_size:self.height/1.1
            font_name:"fonts/batmfa.ttf"
            halign:"left"
            valign:"middle"
            text_size:self.size
            color:1,1,1,.7
        BoxLayout
            Label
                color:0,1,1,1
                text:root.svalue
                font_size:self.height*1.2
                font_name:"fonts/lcd_b.ttf"
            Label:
                text:root.unit
                font_name:"fonts/consola.ttf"
                font_size:self.height/2.5
                halign:"center"
                valign:"bottom"
                text_size:self.size
                color:1,1,1,.7
                markup:True
        ProgressBar
            size_hint:1,.3
            pos_hint:{"right":1}
            value:root.value
            max:root.max

<Cir@FloatLayout>:
    tebal:1
    warna:1,1,1,1
    angle_start:0
    angle_end:360
    canvas:
        Color:
            rgba: root.warna
        Line:
            width: root.tebal
            circle:
                (self.center_x, self.center_y, min(self.width, self.height)
                / 2,root.angle_start,root.angle_end)
            cap:"none"
<Ell@FloatLayout>
    # size_hint:None,None
    pos_hint:{"center_x":.5,"center_y":.5}
    warna:1,1,1,1
    angle_start:0
    angle_end:360
    source:""
    canvas.before:
        Color:
            rgba:root.warna
        Ellipse:
            size:self.size
            pos:self.pos
            angle_start:root.angle_start
            angle_end:root.angle_end
            source:root.source
<Rec@FloatLayout>
    pos_hint:{"center_x":.5,"center_y":.5}
    warna:1,1,1,1
    angle_start:0
    angle_end:360
    source:""
    canvas:
        Color:
            rgba:root.warna
        Rectangle:
            size:self.size
            pos:self.pos
            source:root.source
<Dash>:
    FloatLayout:
        id:rpm
        size_hint:None,None
        size:1.17*min(root.size),min(root.size)
        pos_hint:{"center_x":.5,"center_y":.5}
        value:0
        max:12000
        key:"rpm"
        on_parent:root.D[0]=self
        canvas:
            Color:
                rgba:1,1,1,1
            Ellipse:
                size:self.size
                pos:self.pos
                source:"img/tengah.png"
        Rec:
            size_hint:.02*1/1.18, .65*1
            pos_hint:{"center_x":.5,"center_y":.5425}
            source:"img/arrow.png"
            warna:1,0,0,1
            canvas.before:
                PushMatrix
                Rotate:
                    angle:108-rpm.value*(180/rpm.max)
                    origin: self.center
            canvas.after:
                PopMatrix
        BV
            size_hint:.25,.15
            pos_hint:{"center_x":.5,"center_y":.24}
            canvas:
                Color:
                    rgba:0,0,0,1
                Ellipse:
                    size:self.size
                    pos:self.pos
        BV
            id:speed
            key:"speed"
            value:0
            svalue:"{}".format(self.value)
            size_hint:.25,.13
            pos_hint:{"center_x":.5,"center_y":.24}
            on_parent:root.D[2]=self
            Label
                font_name:"fonts/batmfa.ttf"
                size_hint:1,.6
                text:"Speed"
                color:1,1,1,.7
                font_size:self.height/1.3
            Label:
                font_name:"fonts/lcd_b.ttf"
                text:speed.svalue
                font_size:self.height*1.1
                color:0,1,1,1
            
        Ell:
            size_hint:.91*1/1.18, .91*1
            pos_hint:{"center_x":.5,"center_y":.5425}
            source:"img/ongko.png"
        Ell:
            size_hint:.34*1/1.18, .34*1
            pos_hint:{"center_x":.5,"center_y":.5425}
            warna:0,0,0,1
            Label:
                pos_hint:{"center_x":.5,"center_y":.5}
                text:"{}".format(rpm.value)
                font_name:"fonts/fish.ttf"
                font_size:self.height/2
            Label:
                pos_hint:{"center_x":.5,"center_y":.85}
                color:0,1,1,1
                text:rpm.key
                font_name:"fonts/batmfa.ttf"
                font_size:self.height/6
                
        Rec:
            unit:""
            id:tp
            max:100
            key:"tps"
            svalue:"0"
            value:0
            size_hint:.3*1/1.18 ,.3*1
            pos_hint:{"center_x":.76,"center_y":.375}
            warna:0,0,0,0
            on_parent:root.D[1]=self
            Label:
                text:"{:.0f}".format(tp.value)
                pos_hint:{"center_x":.5,"center_y":.55}
                font_name:"fonts/fish.ttf"
                font_size:self.height/4
                color:0,1,1,1
            Label:
                text:"tps"
                pos_hint:{"center_x":.5,"center_y":.79}
                font_name:"fonts/hemi.ttf"
                font_size:self.height/7
                color:0,0,0,1
            Cir
                pos_hint:{"center_x":.5,"center_y":.5}
                tebal:min(self.size)/30
                angle_start:220
                angle_end:220+tp.value*(160/tp.max)
                size_hint:.8,.8
                warna:0,1,1,1
        
    Rec:
        source:"img/KANAN.png"        
        size_hint:None,None
        size:1/1.4*min(root.size),min(root.size)
        pos_hint:{"right":1}
        
        BV:
            padding:0,0,15,0
            size_hint:.6,.5
            pos_hint:{"right":1,"center_y":.52}
            ItemBig
                key:"o2"
                svalue:"0"
                unit:"volt"
                max:1.5
                value:0
                on_parent:root.G[3]=self
            ItemBig
                key:"stf"
                svalue:"0"
                unit:"lamda"
                max:2
                value:0
                on_parent:root.G[4]=self
            ItemBig
                key:"afr"
                svalue:"0"
                unit:" : 1"
                max:30
                value:0
                on_parent:root.G[5]=self
        BH:
            id:adv
            key:"ADV"
            value:0
            svalue:"{:.0f}".format(self.value)
            size_hint:.5,.07
            pos_hint:{"center_x":.4,"y":.12}
            on_parent:root.D[5]=self
            Label:
                text:adv.key
                font_name:"fonts/hemi.ttf"
                font_size:self.height/1.5
                color:0,1,1,1
            Label:
                text:"{}".format(adv.svalue)
                font_name:"fonts/hemi.ttf"
                font_size:self.height
    Rec:
        source:"img/KIRI.png"        
        size_hint:None,None
        size:1/1.4*min(root.size),min(root.size)
        pos_hint:{"x":0}
        on_parent:root.D[4]=self
        BV:
            padding:15,0,0,0
            size_hint:.6,.5
            pos_hint:{"x":0,"center_y":.52}
            ItemBig
                key:"battery"
                svalue:"0"
                unit:"volt"
                max:16
                value:0
                on_parent:root.G[0]=self
            ItemBig
                key:"iat"
                svalue:"0"
                unit:"[sup]O[/sup] c"
                max:60
                value:0
                on_parent:root.G[1]=self
            ItemBig
                key:"map"
                svalue:"0"
                unit:"kpa"
                max:120
                value:0
                on_parent:root.G[2]=self
        BH:
            id:inj
            key:"INJ"
            value:0
            svalue:"{:.1f}".format(self.value)
            unit:""
            size_hint:.5,.07
            pos_hint:{"center_x":.6,"y":.12}
            Label:
                text:"{}".format(inj.svalue)
                font_name:"fonts/hemi.ttf"
                font_size:self.height
            Label:
                text:inj.key
                font_name:"fonts/hemi.ttf"
                font_size:self.height/1.5
                color:0,1,1,1
    BH:
        id:temp
        spacing:20
        size_hint:.4,.08
        pos_hint:{"center_x":.5}
        LabelHemi:
            svalue:"supra"
            text:"{}    .".format(self.svalue)
            markup:True
            halign:"right"
            valign:"middle"
            text_size:self.size
            font_size:self.height/1.5
            on_parent:root.D["model"]=self
        LabelHemi:
            value:68
            key:""
            unit:""
            svalue:"{:.0f}".format(self.value)
            text:"  {} [sup]O[/sup] c".format(self.svalue)
            markup:True
            halign:"left"
            valign:"middle"
            text_size:self.size
            font_size:self.height/1.5
            on_parent:root.D[3]=self
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
            color:1,1,1,.3
            on_parent:root.I[1]=self
    BoxLayout:
        size_hint:.15,.07
        pos_hint:{"center_x":.795,"y":.8}
        Image
            source:"img/batt.png"
            color:1,1,1,.3
            on_parent:root.I[2]=self
        Image
            source:"img/jagang.png"
            color:1,1,1,.3
            on_parent:root.I[3]=self
    PopEror:
        id:poperor
    
""")
from kivy.clock import Clock
from kivy.properties import NumericProperty,StringProperty,ListProperty,DictProperty
class PopEror(FloatLayout):
    text_eror=StringProperty("")
    def __init__(self, **kwargs):
        self.register_event_type("on_clear_dtc")
        super(PopEror,self).__init__(**kwargs)
    def clear(self):
        self.dispatch("on_clear_dtc")
    def on_clear_dtc(self):
        print("cok")
class Tengah(FloatLayout):
    pass
class ClockNumber(Label):
    angle=NumericProperty(0)
class Dash(FloatLayout):
    rpm=NumericProperty(0)
    vss=NumericProperty(0)
    D=DictProperty({})
    G=DictProperty({})
    I=DictProperty({})
    def __init__(self, **kwargs):
        super(Dash,self).__init__(**kwargs)
        Clock.schedule_once(self.delay,1)
    def delay(self,dt):
        # self.D[0].value=11000
        # self.D[3].svalue="100"
        # self.I[0].on_press=print("ok")
    # def show_pop_eror(self):
        # print("ok")
        # self.I[0].color=[1,1,0,1]
        pass
    def show_eror(self):
        self.ids["poperor"].pos_hint={"center_x":.5,"center_y":.5}
# class M(App):
#     def build(self):
#         return Dash()
# if __name__=="__main__":
#     M().run()
# readme
# D[0]=rpm
# D[1]=tps
# D[2]=speed
# D[3]=temp
# D[4]=inj
# D[5]=adv


 
