from all_config import *
import math
from kivy.uix.label import Label
Builder.load_string('''

#:import math math
<TableDash@BoxLayout>
    o2:"-"
    stf:"-"
    pom:"off"
    stfn:0
    orientation:"vertical"
    size_hint:.65,.45
    pos_hint:{"x":.0,"y":.34}
    id:table_kiri 
    one1:"short term fuel trim"
    two1:"oxigen sensor"
    three1:"fuel pump"
    lean:"lean"
    rich:"rich"
    
    BoxLayout:
        orientation:"vertical"
        Label
            text:root.o2
            font_name:"fonts/modern.ttf"
            font_size:self.height/2
            halign:"center"
            valign:"bottom"
            text_size:self.size
            color:0,1,1,1
        LineTable
        Label
            size_hint:1,.3
            text:root.two1
            font_name:"fonts/modern.ttf"
            color:0,1,1,1
            font_size:self.height
    BoxLayout:
        orientation:"vertical"
        FloatLayout:
            Label:
                pos_hint:{"center_x":.5,"center_y":.5}
                text:root.stf
                font_name:"fonts/modern.ttf"
                font_size:self.height/2
                halign:"center"
                valign:"bottom"
                text_size:self.size
                color:0,1,1,1
            Label:
                pos_hint:{"x":root.stfn/2,"center_y":.5}
                size_hint:.01,1
                canvas:
                    Color:
                        rgba:1,1,1,1
                    Rectangle:
                        size:self.size
                        pos:self.pos
                        source:"asset/slider.png"
            BoxLayout:
                pos_hint:{"center_x":.5,"center_y":.5}
                Label
                    text:root.rich
                    font_name:"fonts/modern.ttf"
                    font_size:self.height/3.5
                    color:1,1,0,1
                Label
                    font_name:"fonts/modern.ttf"
                    font_size:self.height/3.5
                    text:root.lean
                    color:1,1,0,1
                
        LineTable     
        Label
            size_hint:1,.3
            text:root.one1
            font_name:"fonts/modern.ttf"
            color:0,1,1,1
            font_size:self.height
    BoxLayout:
        orientation:"vertical"
        Label
            text:root.pom
            font_name:"fonts/modern.ttf"
            font_size:self.height/2
            halign:"center"
            valign:"bottom"
            text_size:self.size
            color:0,1,1,1
        LineTable
        Label
            size_hint:1,.3
            text:root.three1
            font_name:"fonts/modern.ttf"
            color:0,1,1,1
            font_size:self.height
<LineTable@Label>:
    size_hint:.8,None
    pos_hint:{"center_x":.5,"center_y":.5}
    height:"1.5sp"
    canvas:
        Color:
            rgba:1,1,1,1
        Rectangle:
            size:self.size
            pos:self.pos
            source:"asset/linewhite.png"         
<ClockNumber>:
    text: "1"
    pos_hint: {"center_x": 0.5+0.42*math.sin(math.pi*(root.angle)), "center_y": 0.5+0.42*math.cos(math.pi*(root.angle))}
    font_size: self.height/18
    font_name:"fonts/hemi.ttf"
    color:1,1,1,.6
<TitikDua@Label>:
    size_hint:.05,1
    text:":"
<Kanan@FloatLayout>:
    size_hint:.3,1
    pos_hint:{"right":1}
    canvas:
        Color:
            rgba:1,1,1,1
        Rectangle:
            size:self.size
            pos:self.pos
            source:"asset/kanan.png"

<DashTable>:
    key:"aku"
    val:"10"
    Button:
        text:root.key
    TitikDua
    Button:
        text:root.val

<Kiri@FloatLayout>:
    size_hint:.3,1
    pos_hint:{"x":0}
    canvas:
        Color:
            rgba:1,1,1,1
        Rectangle:
            size:self.size
            pos:self.pos
            source:"asset/kiri.png"


<LblRPM@BoxLayout>:
    data_rpm:"0"
    pos_hint:{"center_x":.5,"center_y":.4}
    size_hint:1,.3
    orientation:"vertical"
    Label
        text:root.data_rpm
        font_size:self.height
        font_name:"fonts/bebas.ttf"
        halign:"center"
        valign:"bottom"
        text_size:self.size
        color:0,1,1,.7
    Label
        text:"RPM"
        font_size:self.height/2.5
        font_name:"fonts/hemi.ttf"
        size_hint:1,.8
        halign:"center"
        valign:"top"
        text_size:self.size
        color:0,1,1,.8
<Dash>:
    canvas:
        Color:
            rgba:1,1,1,1
        Rectangle:
            size:self.size
            pos:self.pos
            source:"asset/01.jpg"
    Kanan

        TableDash
            
            size_hint:.65,.45
            pos_hint:{"x":.35,"y":.34}
            one1:"manifolt pressure"
            two1:"intake temp"
            three1:"idle control"
            o2:"{}".format(root.iat)
            stf:"{}".format(root.map)
            pom:"{}".format(root.iac)
            lean:""
            rich:""
            
            

        Label:
            size_hint:.1,.1
            text:"{:.0f}".format(root.adv)
            font_size:self.height/1.7
            pos_hint:{"center_x":.4,"center_y":.19}
            font_name:"fonts/hemi.ttf"
        Image:
            source:"asset/jagang.png"
            pos_hint:{"right":.951,"y":-.01}
            color:root.ss_color
            size_hint:.18,.18
        Image:
            source:"asset/cbr.png"
            pos_hint:{"right":.951,"y":-.05}
            color:root.cbr_color
            size_hint:.18,.18

        
        FloatLayout
            size_hint:None,None
            size:.19*min(root.size),.19*min(root.size)
            pos_hint:{"right":.47,"top":.85}
            canvas.before:
                Color:
                    rgba:
                Rectangle:
                    source:"asset/ect.png"
                    size:self.size
                    pos:self.pos
            Label:
                text:"temp"
                pos_hint:{"center_x":.5,"top":.88}
                size_hint:.1,.2
                font_size:self.height
                font_name:"fonts/hemi.ttf"
                color:0,1,1,1
            BoxLayout:
                pos_hint:{"center_x":.5,"center_y":.5}
                Label:
                    markup:True
                    text:"{:.0f}".format(root.ect)
                    font_size:self.height/3.1
                    font_name:"fonts/hemi.ttf"
                    halign:"right"
                    valign:"middle"
                    text_size:self.size
                Label:
                    markup:True
                    text:"[sup]O[/sup]"
                    font_size:self.height/3
                    font_name:"fonts/hemi.ttf"
                    size_hint:.4,1
                    halign:"left"
                    valign:"middle"
                    text_size:self.size
            
            
        
           
    Kiri
        TableDash:
            stfn:root.stf
            o2:"{:.2f}".format(root.o2)
            stf:"{:.2f}".format(root.stf)
            pom:root.pom
            
        Label:
            size_hint:.1,.1
            text:"{:.1f}".format(root.inj)
            font_size:self.height/1.7
            pos_hint:{"center_x":.6,"center_y":.19}
            font_name:"fonts/hemi.ttf"
        
        FloatLayout
            size_hint:None,None
            size:.19*min(root.size),.19*min(root.size)
            pos_hint:{"right":.87,"top":.85}

            canvas.before:
                Color:
                    rgba:
                Rectangle:
                    source:"asset/bt.png"
                    size:self.size
                    pos:self.pos
            BoxLayout:
                pos_hint:{"center_x":.5,"center_y":.5}
                Label:
                    markup:True
                    text:"{:.1f} ".format(root.bat)
                    font_size:self.height/3.1
                    font_name:"fonts/hemi.ttf"
                    halign:"right"
                    valign:"middle"
                    text_size:self.size
                Label:
                    markup:True
                    text:"[sub]v[/sub]"
                    font_size:self.height/3
                    font_name:"fonts/hemi.ttf"
                    size_hint:.3,1
                    halign:"left"
                    valign:"middle"
                    text_size:self.size
            Label:
                text:"bat"
                pos_hint:{"center_x":.5,"top":.88}
                size_hint:.1,.2
                font_size:self.height
                font_name:"fonts/hemi.ttf"
                color:0,1,1,1
        Image:
            source:"asset/mil_light.png"
            pos_hint:{"right":.82,"top":.98}
            size_hint:.15,.1
            color:1,1,1,0
            id:mil_icon
        Image:
            source:"asset/fan.png"
            pos_hint:{"right":1,"top":.985}
            size_hint:.11,.11
            color:root.fan_color
            id:fan_icon
        


    FloatLayout:
        id:rt
        size_hint:None,None
        pos_hint:{"center_x":.5,"top":.97}
        size:.95*1.3575129533678756*min(root.size),.95*min(root.size)
        FloatLayout:    
            size_hint: None, None
            size: 0.85*min(root.size), 0.8*min(root.size)
            orientation:"vertical"
            pos_hint:{"center_x":.5,"center_y":.47}
            canvas.before:
                Color:
                    rgba:0,0,0,1
                Ellipse:
                    size:self.size
                    pos:self.pos
        FloatLayout:    
            size_hint: None, None
            size: 0.85*min(root.size), 0.8*min(root.size)
            orientation:"vertical"
            pos_hint:{"center_x":.5,"center_y":.47}
            canvas.before:
                Color:
                    rgba:0,1,1,1
                Ellipse:
                    size:self.size
                    pos:self.pos
                    angle_start:255
                    angle_end:255+root.rpm/72.22222222222223
        FloatLayout:
            orientation:"vertical"
            pos_hint:{"center_x":.5,"center_y":.5}
            canvas.before:
                Color:
                    rgba:1,1,1,1
                Rectangle:
                    size:self.size
                    pos:self.pos
                    source:"asset/tengah.png"
        
        FloatLayout:
            size_hint: None, None
            pos_hint: {"center_x":0.5, "center_y":0.5}
            size: 0.95*min(rt.size), 0.9*min(rt.size)
            id:marker_text
        LblRPM:
            data_rpm:str(root.rpm)
        BoxLayout:
            size_hint: None, None
            pos_hint: {"center_x":0.76, "center_y":0.275}
            size: 0.26*min(rt.size), 0.26*min(rt.size)
            canvas.before:
                Color:
                    rgba:0,1,1,.8
                Line:
                    circle:(self.center_x, self.center_y, min(self.width, self.height)/ 2,210,210+root.tps*1.8)
                    width:self.height/26
                    cap:"none"
        FloatLayout:
            size_hint: None, None
            pos_hint: {"center_x":0.76, "center_y":0.275}
            size: 0.32*min(rt.size), 0.32*min(rt.size)
            canvas.before:
                Color:
                    rgba:0,1,1,.4
                Line:
                    circle:(self.center_x, self.center_y, min(self.width, self.height)/ 2,210,210+root.tps*1.8)
                    width:self.height/10
                    cap:"none"

        Label
            text:"{}".format(root.tps)
            size_hint: None, None
            pos_hint: {"center_x":0.755, "center_y":0.275}
            size: 0.25*min(rt.size), 0.2*min(rt.size)
            font_name:"fonts/hemi.ttf"
            font_size:self.height/3
            color:0,1,1,.8
        Label
            text:"TPS"
            size_hint: None, None
            pos_hint: {"center_x":0.755, "center_y":0.329}
            size: 0.25*min(rt.size), 0.2*min(rt.size)
            font_name:"fonts/hemi.ttf"
            font_size:self.height/7
            color:0,1,1,.8
    BtnImg:
        size_hint:.08,.14
        source:"asset/setting.png"
        on_press:root.sett()
        color:0,1,1,.3
        
        
        

         
            

        
                    
            
''')
class DashTable(BoxLayout):
    pass
class ClockNumber(Label):
    angle=NumericProperty(0)
class Dash(FloatLayout):

    rpm=NumericProperty(0)
    o2=NumericProperty(0)
    stf=NumericProperty(0)
    pom=StringProperty("off")
    tps=NumericProperty(0)
    adv=NumericProperty(0)
    inj=NumericProperty(0)
    ss_color=ListProperty([0,0,0,.2])
    fan_color=ListProperty([0,0,0,0])
    cbr_color=ListProperty([1,.5,0,0])
    
    ss=StringProperty("off")
    hitung=NumericProperty(0)
    bat=NumericProperty(0)
    ect=NumericProperty(0)
    mil=ListProperty([])
    mil1=ListProperty([])
    map=NumericProperty(0)
    iat=NumericProperty(0)
    iac=NumericProperty(0)
    fan=StringProperty("")
    bas=StringProperty("")

    
    
    def __init__(self,*args,**kwargs):
        self.register_event_type("on_set")
        super(Dash,self).__init__(*args,**kwargs)
        Clock.schedule_once(self.delay,.1)
        Clock.schedule_interval(self.kedip,.5)
        
    def delay(self,dt):
        for i in range(14):
            self.ids["marker_text"].add_widget(ClockNumber(angle=1.41+i/12.5,text=(str(i))))
    def get_value(self,rpm=0,tps=0,inj=0,adv=0,pom="off",ss="off",bat=0,ect=0,mil=[],mil1=[],o2=0,stf=1,map=0,iat=0,iac=0,fan="",bas=""):
        self.rpm=rpm
        self.tps=int(tps)
        self.adv=adv
        self.inj=inj
        self.ss=ss
        self.ect=ect
        self.bat=bat
        self.mil=mil
        self.mil1=mil1
        self.o2=o2
        self.stf=stf
        self.pom=pom
        self.iac=iac
        self.iat=iat
        self.map=map
        self.fan=fan
        self.bas=bas


    def kedip(self,dt):

        self.hitung+=1
        if self.hitung==3:
            self.hitung=0
        if self.ss=="on":
            if self.hitung==1:
                self.ss_color=[1,.5,0,.6]
            else:
                self.ss_color=[0,0,0,.2]
        else:
            self.ss_color=[0,0,0,.2]
        if self.bat=="on":
            if self.hitung==1:
                self.cbr_color=[1,.5,1,1]
            else:
                self.cbr_color=[1,.5,1,0]
        else:
            self.cbr_color=[1,.5,1,0]
        if self.mil !=[] or self.mil1 !=[]:
            if self.hitung==1:
                self.ids["mil_icon"].color=[1,1,1,1]
            else:
                self.ids["mil_icon"].color=[1,1,1,0]
        if self.fan=="on":
            self.fan_color=[0,1,0,1]
        else:
            self.fan_color=[0,1,0,0]
    def clean(self):
        self.ids["mil_icon"].color=[1,1,1,0]
    def sett(self):
        self.dispatch("on_set")
    def on_set(self):
        print("ok")