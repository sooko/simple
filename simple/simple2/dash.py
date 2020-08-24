from kivy.config import Config
Config.set('graphics', 'height', 370)
Config.set('graphics', 'width', 770)
from kivy.app import App
from kivy.uix.floatlayout import FloatLayout
from kivy.lang import Builder
from kivy.clock import Clock
from kivy.properties import StringProperty,NumericProperty,ListProperty,DictProperty
from struct import unpack
Builder.load_string('''
#:import math math
<Tengah>:
    val:0
    svalue:"0"
    FloatLayout:
        size_hint:None,None
        size: .93*min(root.size), .93*min(root.size)
        pos_hint:{"center_x":.5,"top":.975}
        id:tengah_bulat
        canvas:
            Color:
                rgba:1,1,1,1
            Rectangle:
                size:self.size
                pos:self.pos     
                source:"asset/tengah_bulat1.png" 
        FloatLayout:
            size_hint:.9,.9
            pos_hint:{"center_x":.5,"center_y":.47}
            id:marker_text
            canvas:
                Color:
                    rgba:0,0,0,1
                Ellipse:
                    size:self.size
                    pos:self.pos    
            FloatLayout:
                size_hint:.85,.85
                pos_hint:{"center_x":.5,"center_y":.5}
                canvas:
                    Color:
                        rgba:0,1,1,.2
                    Ellipse:
                        size:self.size
                        pos:self.pos  
                        angle_start:250
                        angle_end:250+(12000/66.7)
            FloatLayout:
                size_hint:.85,.85
                pos_hint:{"center_x":.5,"center_y":.5}
                canvas:
                    Color:
                        rgba:0,1,1,.9
                    Ellipse:
                        size:self.size
                        pos:self.pos  
                        angle_start:250
                        angle_end:250+(root.rpm_val/66.7)
        Image:
            size_hint:.77,.77
            pos_hint:{"center_x":.51,"center_y":.41}
            source:"asset/isi_tengah.png"  
            canvas.before:
                PushMatrix
                Rotate:
                    angle: 30
                    origin: self.center
            canvas.after:
                PopMatrix
        FloatLayout
            size_hint:.42,.42
            pos_hint:{"center_x":.5,"center_y":.47}
            id:label_rpm
            canvas:
                Color:
                    rgba:0,0,0,1
                Ellipse:
                    size:self.size
                    pos:self.pos    
            Label:
                text:"RPM"
                font_name:"fonts/hemi.ttf"
                size_hint:1,.17
                font_size:self.height
                pos_hint:{"center_x":.5,"top":.95}
                color:1,1,0,.7
            Label:
                text:"{}".format(int(root.rpm_val))
                font_name:"fonts/bebas.ttf"
                size_hint:1,.5
                font_size:self.height
                pos_hint:{"center_x":.5,"center_y":.5}
                color:0,1,1,.8
        BoxLayout
            orientation:"vertical"
            size_hint:1,.2
            pos_hint:{"center_x":.5,"center_y":0.13}
            id:label_speed
            Label:
                text:"{}".format(int(root.vss_val))
                font_name:"fonts/bebas.ttf"
                font_size:self.height
                color:1,1,1,.5
            LineGw
            Label:
                text:"km/h"
                font_name:"fonts/hemi.ttf"
                color:1,1,0,.7
                size_hint:1,.4
                font_size:self.height/1.2

    
<Labelhemi@Label>:
    font_name:"fonts/hemi.ttf"
<Labelmodern@Label>:
    font_name:"fonts/modern.ttf"
<LineGw@Label>:
    size_hint:.3,None
    pos_hint:{"center_x":.5,"center_y":.5}
    height:"2sp"
    canvas:
        Color:
            rgba:1,1,1,1
        Rectangle:
            size:self.size
            pos:self.pos
            source:"asset/lw.png"
<TabelKanan@BoxLayout>:
    title_color:0,1,1,1
    value_color:0,1,1,1
    orientation:"vertical"
    pos_hint:{"right":1,"center_y":.53}
    size_hint:.6,.5
    title1:""
    title2:""
    title3:""
    value1:0
    value2:0
    value3:0
    BoxLayout
        orientation:"vertical"
        background_color:0,0,0,.5
        Labelmodern
            text:"{:.1f}".format(root.value1)
            font_size:self.height/1.5
            halign:"center"
            valign:"bottom"
            text_size:self.size
            color:root.value_color
        LineGw
            size_hint:1,None
        Labelmodern
            size_hint:1,.3
            text:root.title1
            color:root.title_color
            font_size:self.height
    BoxLayout
        orientation:"vertical"
        background_color:0,0,0,.5
        Labelmodern
            text:"{:.1f}".format(root.value2)
            font_size:self.height/1.5
            halign:"center"
            valign:"bottom"
            text_size:self.size
            color:root.value_color
        LineGw
            size_hint:1,None
        Labelmodern
            size_hint:1,.3
            text:root.title2
            color:root.title_color
            font_size:self.height
            markup:True
    BoxLayout
        orientation:"vertical"
        background_color:0,0,0,.5
        Labelmodern
            text:"{:.1f}".format(root.value3)
            font_size:self.height/1.5
            halign:"center"
            valign:"bottom"
            text_size:self.size
            color:root.value_color
        LineGw
            size_hint:1,None
        Labelmodern
            size_hint:1,.3
            text:root.title3
            color:root.title_color
            font_size:self.height
            markup:True
<TabelKiri@BoxLayout>:
    title_color:0,1,1,1
    value_color:0,1,1,1
    orientation:"vertical"
    pos_hint:{"x":0,"center_y":.53}
    size_hint:.6,.5
    title1:""
    title2:""
    title3:""
    value1:0
    value2:0
    value3:0
    BoxLayout
        orientation:"vertical"
        background_color:0,0,0,.5
        Labelmodern
            text:"{:.3f}".format(root.value1)
            font_size:self.height/1.5
            halign:"center"
            valign:"bottom"
            text_size:self.size
            color:root.value_color
        LineGw
            size_hint:1,None
        Labelmodern
            size_hint:1,.3
            text:root.title1
            color:root.title_color
            font_size:self.height
    BoxLayout
        orientation:"vertical"
        background_color:0,0,0,.5
        Labelmodern
            text:"{:.3f}".format(root.value2)
            font_size:self.height/1.5
            halign:"center"
            valign:"bottom"
            text_size:self.size
            color:root.value_color
        LineGw
            size_hint:1,None
        Labelmodern
            size_hint:1,.3
            text:root.title2
            color:root.title_color
            font_size:self.height
    BoxLayout
        orientation:"vertical"
        background_color:0,0,0,.5
        Labelmodern
            text:"{}".format(root.value3)
            font_size:self.height/1.5
            halign:"center"
            valign:"bottom"
            text_size:self.size
            color:root.value_color
        LineGw
            size_hint:1,None
        Labelmodern
            size_hint:1,.3
            text:root.title3
            color:root.title_color
            font_size:self.height
<BulatKanan@FloatLayout>:
    key:""
    svalue:""
    unit:""
    size_hint:.35,.35
    pos_hint:{"x":.15,"top":.995}
    id:root_bulat_kanan
    Image:
        source:"asset/bt.png"
        pos_hint:{"center_x":.5,"center_y":.5}
    FloatLayout
        size: .85*min(root_bulat_kanan.size), .85*min(root_bulat_kanan.size)
        pos_hint:{"center_x":.5,"center_y":.5}
        size_hint:None,None
        canvas:
            Color:
                rgba:1,1,1,.7
            Ellipse:
                size:self.size
                pos:self.pos   
                source:"asset/02.png"
    BoxLayout:
        pos_hint:{"center_x":.5,"center_y":.5}
        size_hint:1,.6
        orientation:"vertical"
        Labelhemi:
            size_hint:1,.3
        Labelhemi:
            text:root.svalue
            font_size:self.height/1.5
            color:1,1,1,.6
        LineGw                    
            size_hint:.8,None
        Labelhemi:
            size_hint:1,.5
            text:root.key
            font_size:self.height/1.7
            color:0,1,1,.6
            halign:"center"
            valign:"top"
            text_size:self.size 
<BulatKiri@FloatLayout>:
    key:""
    svalue:""
    value:0
    unit:""
    size_hint:.35,.35
    pos_hint:{"right":.85,"top":.995}
    id:root_bulat_kiri
    Image:
        source:"asset/bt.png"
        pos_hint:{"center_x":.5,"center_y":.5}
    FloatLayout
        size: .85*min(root.size), .85*min(root.size)
        pos_hint:{"center_x":.5,"center_y":.5}
        size_hint:None,None
        canvas:
            Color:
                rgba:1,1,1,.7
            Ellipse:
                size:self.size
                pos:self.pos    
                source:"asset/02.png"
    BoxLayout:
        pos_hint:{"center_x":.5,"center_y":.5}
        size_hint:1,.6
        orientation:"vertical"
        Labelhemi:
            size_hint:1,.3
        Labelhemi:
            text:root.svalue
            color:1,1,1,.6
            font_size:self.height/1.5
        LineGw                    
            size_hint:.8,None
        Labelhemi:
            size_hint:1,.5
            text:root.key
            font_size:self.height/1.7
            color:0,1,1,.6
            halign:"center"
            valign:"top"
            text_size:self.size
<ClockNumber>:
    text: "1"
    pos_hint: {"center_x": 0.5+0.46*math.sin(math.pi*(root.angle)), "center_y": 0.5+0.46*math.cos(math.pi*(root.angle))}
    font_size: self.height/18
    color:1,1,1,.6
    font_name:"fonts/hemi.ttf"
<Dash>:
    canvas:
        Color:
            rgba:1,1,1,1
        Rectangle:
            size:self.size
            pos:self.pos
            source:"asset/01.jpg"
#=============================KANAN===============================
    FloatLayout:
        size_hint:None,None
        size: 1/1.65*min(root.size), 1*min(root.size)
        pos_hint:{"right":1,"bottom":1}
        id:kanan
        canvas:
            Color:
                rgba:1,1,1,1
            Rectangle:
                size:self.size
                pos:self.pos     
                source:"asset/KANAN1.png"  
        BulatKanan:
        BoxLayout:
            size_hint:.6,.1
            pos_hint:{"x":0,"y":.115}
            Labelhemi
                text:"adv"
                font_size:self.height/2
                color:0,1,1,1
            
            Labelhemi
                text:"{}".format(int(root.adv_val))
                font_size:self.height/1.5
                size_hint:.5,1
#=============================KIRI===============================
    FloatLayout:
        size_hint:None,None
        size: 1/1.65*min(root.size), 1*min(root.size)
        pos_hint:{"left":1,"bottom":1}
        id:kiri
        canvas:
            Color:
                rgba:1,1,1,1
            Rectangle:
                size:self.size
                pos:self.pos     
                source:"asset/KIRI1.png"   
        BulatKiri
            
        BoxLayout:
            size_hint:.6,.1
            pos_hint:{"right":1,"y":.115}
            Labelhemi
                text:"{:.1f}".format(root.inj_val)
                font_size:self.height/1.5
                size_hint:.5,1
            Labelhemi
                text:"inj"
                font_size:self.height/2
                color:0,1,1,1
#=============================TENGAH===============================
    Tengah:
        on_parent:root.dict_dash[0]=self


''')
class Tengah(FloatLayout):
    rpm_val  =NumericProperty(0)
    vss_val  =NumericProperty(0)
    inj_val  =NumericProperty(0)
    adv_val  =NumericProperty(0)
    def __init__(self, **kwargs):
        super(Tengah,self).__init__(**kwargs)
        Clock.schedule_once(self.delay,1)
    def delay(self,dt):
        for i in range(13):
            self.ids["marker_text"].add_widget(ClockNumber(angle=1.41+i/12.2,text=(str(i))))
from kivy.uix.label import Label
class ClockNumber(Label):
    angle=NumericProperty(0)
class Dash(FloatLayout):
    rpm_val  =NumericProperty(0)
    vss_val  =NumericProperty(0)
    inj_val  =NumericProperty(0)
    adv_val  =NumericProperty(0)
    dict_dash=DictProperty({})
    def __init__(self,*args, **kwargs):
        super(Dash,self).__init__(*args,**kwargs)
class M(App):
    def build(self):
        return Dash()
if __name__=="__main__":
    M().run()
