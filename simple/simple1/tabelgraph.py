from kivy.lang import Builder
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.config import Config
Config.set('graphics', 'height', 370)
Config.set('graphics', 'width', 770)
from kivy.uix.screenmanager import ScreenManager, Screen,WipeTransition,RiseInTransition,FadeTransition,CardTransition
from css import *
from kivy.garden.graph import Graph,MeshLinePlot
Builder.load_string("""
<Grafik>:
    BoxLayout:
        BoxLayout:
            id:ylabel
            size_hint:None,1
            width:self.minimum_width
        Chart
        BoxLayout:
            size_hint:.2,1
            orientation:"vertical"
            BoxLayout:
                LabelConsola:
                    text:"rpm"
                CheckBox:
                    state:"down"
                    data:"rpm"
                    on_state:
                        root.add(self.data) if self.state=="down" else root.remove(self.data)
            BoxLayout:
                LabelConsola:
                    text:"tps"
                CheckBox
                    on_state:print(self.state)
            BoxLayout:
                LabelConsola:
                    text:"iat"
                CheckBox
                    on_state:print(self.state)
            BoxLayout:
                LabelConsola:
                    text:"map"
                CheckBox
                    on_state:print(self.state)
            BoxLayout:
                LabelConsola:
                    text:"bat"
                CheckBox
            BoxLayout:
                LabelConsola:
                    text:"inj"
                CheckBox
                    on_state:print(self.state)
            BoxLayout:
                LabelConsola:
                    text:"adv"
                CheckBox
                    on_state:print(self.state)
            Spinner:
                text:"times"
                values:["100ms","200ms"]
                font_name:"fonts/consola.ttf"
                background_color:1,1,1,.3
            Label
    
<Label>:
    markup:True
<Xline@Label>:
    tebal:"2sp"
    size_hint:None,1
    width:root.tebal
    warna:1,1,1,1
    canvas:
        Color:
            rgba:root.warna
        Rectangle:
            size:self.size
            pos:self.pos
<Yline@Label>:
    tebal:"2sp"
    size_hint:1,None
    height:root.tebal
    warna:1,1,1,1
    canvas:
        Color:
            rgba:root.warna
        Rectangle:
            size:self.size
            pos:self.pos

<ItemBig@FloatLayout>:
    key:""
    value:""
    unit:""
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
            color:1,1,1,.5
        BoxLayout
            Label
                color:1,1,0,1
                text:root.value
                font_size:self.height*1.2
                font_name:"fonts/lcd_b.ttf"
            Label:
                text:root.unit
                font_name:"fonts/consola.ttf"
                font_size:self.height/2.5
                halign:"center"
                valign:"bottom"
                text_size:self.size
                color:1,1,1,.5
        ProgressBar
            size_hint:1,.3
            pos_hint:{"right":1}
            value:root.pgvalue
            max:root.max
<LineCircle@FloatLayout>:
    angle_end:0
    angle_start:360
    tebal:1.2
    warna:1,1,1,1
    pos_hint:{"center_x":.5,"center_y":.5}
    canvas:
        Color:
            rgba:root.warna
        Line:
            width:root.tebal
            circle:
                (self.center_x, self.center_y, min(self.width, self.height)
                / 2,root.angle_start,root.angle_end)
            cap:"none"
<LineCircleBg@FloatLayout>
    pos_hint:{"center_x":.5,"center_y":.5}
    angle_start:0
    angle_end:360
    warna:0,1,1,1
    tebal:3
    source:""
    FloatLayout:
        pos_hint:{"center_x":.5,"center_y":.5}
        size_hint:None,None
        size:1*min(root.size),1*min(root.size)
        canvas:
            Color
                rgba:root.warna
            Ellipse:
                size:self.size
                pos:self.pos
                angle_start:root.angle_start
                angle_end:root.angle_end
                source:root.source
<Dial@FloatLayout>:
    warna:0,0,1,.4
    pos_hint:{"center_x":.5,"center_y":.5}
    LineCircleBg:
        warna:0,0,0,1
        size_hint:1.05,1.05
    LineCircleBg:
        pos_hint:{"center_x":.5,"center_y":.5}
        size_hint:1.15, 1.15
        source:"img/cb.png"
        warna:root.warna
        angle_start:220
        angle_end:220+280
    LineCircleBg
        size_hint:.65,.65
        pos_hint:{"center_x":.5,"center_y":.5}
        tebal:1.1
        warna:0,0,0,1
    LineCircle:
        pos_hint:{"center_x":.5,"center_y":.5}
        size_hint:.971,.971
        warna:0,0,1,1
        tebal:min(self.size)/140
        LineCircle:
            pos_hint:{"center_x":.5,"center_y":.5}
            size_hint:.98,.98
            warna:1,1,1,.4
            tebal:min(self.size)/150
            LineCircleBg:
                pos_hint:{"center_x":.5,"center_y":.5}
                size_hint:.99,.99
                angle_start:220
                angle_end:220+280
                warna:1,1,1,1
                source:"img/rain3.png"
            LineCircle:
                pos_hint:{"center_x":.5,"center_y":.5}
                size_hint:.965,.965
                warna:0,0,0,1
                tebal:min(self.size)/95
            Label:
                text:"speed"
                font_name:"fonts/batmfa.ttf"
                size_hint:1,.1
                pos_hint:{"center_x":.5,"center_y":.18}
                font_size:self.height/2
                color:1,1,1,.5
            Label:
                text:"100"
                font_name:"fonts/lcd_b.ttf"
                size_hint:1,.1
                pos_hint:{"center_x":.5,"center_y":.12}
                font_size:self.height
                color:1,1,0,.7
            Label:
                text:"kph"
                font_name:"fonts/lcd_b.ttf"
                size_hint:1,.1
                pos_hint:{"center_x":.65,"center_y":.12}
                font_size:self.height/2
                color:1,1,1,.7
    LineCircle
        size_hint:.6,.6
        pos_hint:{"center_x":.5,"center_y":.5}
        tebal:1.1
        warna:0,0,1,1
    LineCircleBg:   
        source:'img/img81.png'
        size_hint:1.1,1.1
        warna:1,1,1,1
    Label:
        text:"rpm"
        pos_hint:{"center_x":.5,"center_y":.65}
        size_hint:1,.15
        font_name:"fonts/batmfa.ttf"
        font_size:self.height/2
        color:1,1,0,1
    Label:
        text:"15000"
        pos_hint:{"center_x":.5,"center_y":.5}
        font_name:"fonts/fish.ttf"
        font_size:self.height/4
        color:0,0,1,1
    
<Dash>:
    pos_hint:{"center_x":.5,"center_y":.5}  
    FloatLayout
    ScreenManager:
        id:sm
        on_parent:root.change_transition()
        Screen:
            name:"0"
            Dial
                pos_hint:{"x":.03,"center_y":.5}
                size_hint:.45,1
            BoxLayout
                Label:
                    size_hint:.8,1
                GridLayout
                    cols:2
                    pos_hint:{"center_x":.5,"center_y":.49}
                    size_hint:1,.85
                    padding:0,0,20,1
                    ItemBig:
                        key:"Tps"
                        value:"0"
                        unit:"deg"
                        on_parent:
                            root.disp[1]=self
                    ItemBig
                        key:"temp"
                        value:"0"
                        unit:"[sup]O[/sup]c"
                        on_parent:
                            root.disp[2]=self
                    ItemBig:
                        key:"iat"
                        value:"0"
                        unit:"[sup]O[/sup]c"
                        on_parent:
                            root.disp[5]=self
                    ItemBig
                        key:"map"
                        value:"0"
                        unit:"kpa"
                        on_parent:
                            root.disp[6]=self
                    ItemBig
                        key:"Battery"
                        value:"0"
                        unit:"volt"
                        on_parent:
                            root.disp[3]=self
                    ItemBig
                        key:"iacv"
                        value:"0"
                        unit:"g/s"
                        on_parent:
                            root.disp[4]=self
                    ItemBig
                        key:"inj"
                        value:"0"
                        unit:"m/s"
                        on_parent:
                            root.disp[7]=self
                    ItemBig
                        key:"adv"
                        value:"0"
                        unit:"deg"
                        on_parent:
                            root.disp[8]=self
        Screen:
            name:"1"
            Dial
                pos_hint:{"x":.03,"center_y":.5}
                size_hint:.45,1
            BoxLayout
                Label:
                    size_hint:.8,1
                GridLayout
                    cols:2
                    pos_hint:{"center_x":.5,"center_y":.49}
                    size_hint:1,.85
                    padding:0,0,20,1
                    ItemBig
                        key:"02"
                        value:"0"
                        unit:"volt"
                        on_parent:
                            root.disp[9]=self
                    ItemBig
                        key:"stf"
                        value:"0"
                        unit:"lamda"
                        on_parent:
                            root.disp[10]=self
                    ItemBig
                        key:"afr"
                        value:"0"
                        unit:" : 1"
                        on_parent:
                            root.disp[11]=self
                    ItemBig
                        on_parent:
                            root.disp[12]=self
                    ItemBig
                        on_parent:
                            root.disp[13]=self
                    ItemBig
                        on_parent:
                            root.disp[14]=self
                    ItemBig
                        on_parent:
                            root.disp[15]=self
                    ItemBig
                        on_parent:
                            root.disp[16]=self
        Screen:
            name:"2"
            GridLayout
                cols:4
                pos_hint:{"center_x":.5,"center_y":.5}
                size_hint:1,1
                padding:0,0,20,1
                ItemBig:
                    on_parent:
                        root.disp[17]=self
                    key:"rpm"
                    value:"0"
                ItemBig
                    on_parent:
                        root.disp[18]=self
                    key:"tps"
                    value:"0"
                ItemBig
                    on_parent:
                        root.disp[19]=self
                    key:"temp"
                    value:"0"
                ItemBig
                    on_parent:
                        root.disp[20]=self
                    key:"iat"
                    value:"0"
                ItemBig
                    on_parent:
                        root.disp[21]=self
                    key:"map"
                    value:"0"
                ItemBig
                    on_parent:
                        root.disp[22]=self
                    key:"battery"
                    value:"0"
                ItemBig
                    on_parent:
                        root.disp[23]=self
                    key:"inj"
                    value:"0"
                ItemBig
                    on_parent:
                        root.disp[24]=self
                    key:"adv"
                    value:"0"
                ItemBig
                    on_parent:
                        root.disp[25]=self
                    
                ItemBig
                    on_parent:
                        root.disp[26]=self
                ItemBig
                    on_parent:
                        root.disp[27]=self
                ItemBig
                    on_parent:
                        root.disp[28]=self
                ItemBig
                    on_parent:
                        root.disp[28]=self
                ItemBig
                    on_parent:
                        root.disp[30]=self
                ItemBig
                    on_parent:
                        root.disp[31]=self
                ItemBig
                    on_parent:
                        root.disp[32]=self
                ItemBig
                    on_parent:
                        root.disp[33]=self
                ItemBig
                    on_parent:
                        root.disp[34]=self
                ItemBig
                    on_parent:
                        root.disp[35]=self
                ItemBig
                    on_parent:
                        root.disp[36]=self
                ItemBig
                    on_parent:
                        root.disp[37]=self
                ItemBig
                    on_parent:
                        root.disp[38]=self
                ItemBig
                    on_parent:
                        root.disp[39]=self
                ItemBig
                    on_parent:
                        root.disp[40]=self
        Screen:
            name:"3"  
            Grafik
            
                    

    BoxLayout:
        size_hint:1,.1
        pos_hint:{"right":1,"top":1}
        # BtnImg:
        #     source:"img/menu.png"
        #     size_hint:.05,1
        Label:
            text:""
            font_size:self.height
            font_name:"fonts/hemi.ttf"
            halign:"right"
            valign:"middle"
            text_size:self.size
            color:0,0,1,1
    
            
        
            
""")
from kivy.uix.floatlayout import FloatLayout
from kivy.properties import NumericProperty,ListProperty,StringProperty,DictProperty
class ChartRpm(Graph):
    def __init__(self,*args,**kwargs):
        super(ChartRpm,self).__init__(**kwargs)
        self.size_hint=None,1
        self.width="5sp"

class ChartTps(Graph):
    def __init__(self,*args,**kwargs):
        super(ChartTps,self).__init__(**kwargs)
        self.size_hint=None,1
        self.width="5sp"
        
class ChartIat(Graph):
    def __init__(self,*args,**kwargs):
        super(ChartIat,self).__init__(**kwargs)
        self.size_hint=None,1
        self.width="5sp"

class ChartMap(Graph):
    def __init__(self,*args,**kwargs):
        super(ChartMap,self).__init__(**kwargs)
        self.size_hint=None,1
        self.width="5sp"

class ChartBat(Graph):
    def __init__(self,*args,**kwargs):
        super(ChartBat,self).__init__(**kwargs)
        self.size_hint=None,1
        self.width="5sp"
class ChartInj(Graph):
    def __init__(self,*args,**kwargs):
        super(ChartInj,self).__init__(**kwargs)
        self.size_hint=None,1
        self.width="5sp"
class ChartAdv(Graph):
    def __init__(self,*args,**kwargs):
        super(ChartAdv,self).__init__(**kwargs)
        self.size_hint=None,1
        self.width="5sp"




        
class Xlabel(Button):
    pass
class Ylabel(Button):
    pass
class Xline(Label):
    pass
class Yline(Label):
    pass
from kivy.clock import Clock


class Grafik(FloatLayout):
    chartitem=DictProperty({
        "rpm":ChartRpm(),
        "tps":ChartTps(),
        "iat":ChartTps(),
        "map":ChartTps(),
        "tps":ChartTps(),
        
    })
    def __init__(self, **kwargs):
        super(Grafik,self).__init__(**kwargs)
    def add(self,data):
        # print(data)
        self.ids["ylabel"].add_widget(self.chartitem[data])
        
    def remove(self,data):
        print(data)
        self.ids["ylabel"].remove_widget(self.chartitem[data])
        




class Dash(FloatLayout):
    xgrid=NumericProperty(13)
    c=NumericProperty(0)
    ygrid=NumericProperty(11)
    dataloger=StringProperty("")
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
    c_screen=NumericProperty(0)
    dataloger=StringProperty("rpm :0\ntps :0\nect :0\n")
    disp=DictProperty({})
    def __init__(self, **kwargs):
        super(Dash,self).__init__(**kwargs)
        Clock.schedule_once(self.delay,1)
    def delay(self,dt):
        pass
    def change_display(self,data):
        self.ids["sm"].current = data
    def change_transition(self):
        self.ids["sm"].transition=WipeTransition(duration=.5)
class Chart(Graph):
    
    def __init__(self,*args,**kwargs):
        super(Chart,self).__init__(**kwargs)
        self.xlabel='time'
        self.x_ticks_minor=1
        self.x_ticks_major=1
        self.y_ticks_major=10
        self.y_grid_label=False
        self.x_grid_label=False
        self.x_grid=True
        self.y_grid=True
        self.xmin=0
        self.xmax=10
        self.ymin=0
        self.ymax=100



from kivy.app import App
class My(App):
    def build(self):
        return Dash()
if __name__=="__main__":
    My().run()
