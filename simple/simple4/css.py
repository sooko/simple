from kivy.uix.behaviors.touchripple import  TouchRippleButtonBehavior
from kivy.lang import Builder
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.image import Image
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.floatlayout import FloatLayout
Builder.load_string('''
<PopInfo>:
    tittle:"info"
    message1:"-"
    message2:"-"
    message3:"-"
    message4:""
    message5:""
    message6:""
    pos_hint:{"center_x":.5,"center_y":5}
    Button:
        background_color:0,0,0,0
        pos_hint:{"center_x":.5,"center_y":.5}
        on_press:root.pos_hint={"center_x":.5,"center_y":5}
    Kotak:
        source:"img/frame.png"
        size_hint:.6,.6
        pos_hint:{"center_x":.5,"center_y":.5}
        BV:
            padding:20
            pos_hint:{"center_x":.5,"center_y":.5}
            BtnBatmfa:
                text:root.tittle
                size_hint:1,.2
                font_size:self.height/1.2
                
            BV:
                BtnConsola:
                    text:root.message1
                    font_size:self.height/1.5
                BtnConsola:
                    text:root.message2
                    font_size:self.height/1.5
                BtnConsola:
                    text:root.message3
                    font_size:self.height/1.5
                BtnConsola:
                    text:root.message4
                    font_size:self.height/1.5
                BtnConsola:
                    text:root.message5
                    font_size:self.height/1.5
                BtnConsola:
                    text:root.message6
                    font_size:self.height/1.5
        
                
               
            
    
                
<Pop>:
    pos_hint:{"center_x":.5,"center_y":5}
    tittle:"DATA KERUSAKAN"
    konten:""
    Button:
        pos_hint:{"center_x":.5,"center_y":.5}
        background_color:0,0,0,.9
        on_press:root.pos_hint={"center_x":.5,"center_y":5}
    Button
        background_color:0,0,0,.9
        pos_hint:{"center_x":.5,"center_y":.5}
        size_hint:.9,.9
    Kotak
        size_hint:.9,.9
        pos_hint:{"center_x":.5,"center_y":.5}
        source:"img/frame.png"
        warna:.81,.81,.81,1
        BV:
            padding:min(root.size)/35
            pos_hint:{"center_x":.5,"center_y":.5}
            LabelBatmfo
                size_hint:1,.12
                text:root.tittle
                font_size:self.height/1.5
                color:1,1,1,1
            Kotak
                source:"img/linegd.png"
                size_hint:.8,None
                height:"1sp"
                pos_hint:{"center_x":.5,"center_y":.5}
            LabelBatmfa
                size_hint:.8,.02
                pos_hint:{"center_x":.5,"center_y":.5}
            
            LabelConsola:
                size_hint:.8,1
                pos_hint:{"center_x":.5,"center_y":.5}
                text:root.konten
                halign:"left"
                valign:"top"
                text_size:self.size
                font_size:min(self.size)/20
                color:1,1,1,1
        BtnCavian:
            size_hint:.3,.1
            pos_hint:{"right":.98,"y":.04}
            on_press:root.cc()
            text:"Clear DTC"
            font_size:self.height/1.2


<ItemBig>:
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
<Kotak>:
    warna:1,1,1,1
    source:""
    canvas:
        Color:
            rgba:self.warna
        Rectangle:
            size:self.size
            pos:self.pos
            source:self.source
<Bulat>:
    warna:1,1,1,1
    angle_start:0
    angle_end:360
    source:""
    canvas:
        Color:
            rgba:root.warna
        Ellipse:
            size:self.size
            pos:self.pos
            angle_start:root.angle_start
            angle_end:root.angle_end
            source:self.source
<LineBulat>:
    tebal:1
    angle_start:0
    angle_end:360
    warna:1,1,1,1
    source:""
    canvas:
        Color:
            rgba:root.warna
        Line:
            width:root.tebal
            ellipse: (self.x, self.y, self.width, self.height, root.angle_start, root.angle_end)
            cap:"none"
<BtnCavian>:
    font_name:"fonts/cavian.ttf"
<BtnModern>:
    font_name:"fonts/modern.ttf"
<BtnHemi>:
    font_name:"fonts/hemi.ttf"
<BtnBatmfa>:
    font_name:"fonts/batmfa.ttf"
<BtnConsola>:
    font_name:"fonts/consola.ttf"
<BtnMono>:
    font_name:"fonts/Monoid-Retina.ttf"
<LabelModern>:
    font_name:"fonts/modern.ttf"
<LabelMonoid>:
    font_name:"fonts/Monoid-Retina.ttf"
<LabelHemi>:
    font_name:"fonts/hemi.ttf"
<LabelLcd>:
    font_name:"fonts/lcd_b.ttf"
<LabelBebas>:
    font_name:"fonts/bebas.ttf"
<LabelBatmfa>:
    font_name:"fonts/batmfa.ttf"
<LabelBatmfo>:
    font_name:"fonts/batmfo.ttf"
<LabelConsola>:
    font_name:"fonts/consola.ttf"
<LabelCavian>:
    font_name:"fonts/cavian.ttf"
<LabelFish>:
    font_name:"fonts/fish.ttf"

<BV>:
    orientation:"vertical"

''')
class BtnModern(TouchRippleButtonBehavior,Label):
    pass
class BtnHemi(TouchRippleButtonBehavior,Label):
    pass
class BtnMono(TouchRippleButtonBehavior,Label):
    pass
class BtnBatmfa(TouchRippleButtonBehavior,Label):
    pass

class BtnCavian(TouchRippleButtonBehavior,Label):
    pass
class BtnConsola(TouchRippleButtonBehavior,Label):
    pass

class BtnImg(TouchRippleButtonBehavior,Image):
    pass


class LabelHemi(Label):
    pass
class LabelModern(Label):
    pass
class LabelMonoid(Label):
    pass
class LabelLcd(Label):
    pass
class LabelCavian(Label):
    pass
class LabelConsola(Label):
    pass
class LabelBebas(Label):
    pass
class LabelFish(Label):
    pass
class LabelBatmfa(Label):
    pass
class LabelBatmfo(Label):
    pass

class BV(BoxLayout):
    pass
class BH(BoxLayout):
    pass
class Kotak(FloatLayout):
    pass
class Bulat(FloatLayout):
    pass
class LineBulat(FloatLayout):
    pass
class ItemBig(FloatLayout):
    pass
class Pop(FloatLayout):
    def __init__(self, **kwargs):
        self.register_event_type("on_hapus")
        super(Pop,self).__init__(**kwargs)
    def cc(self):
        self.dispatch("on_hapus")
    def on_hapus(self):
        pass
        

class PopInfo(FloatLayout):
    pass

print("ok")