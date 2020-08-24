from dash import Dash
from kivy.garden.graph import Graph,MeshLinePlot
from kivy.garden.navigationdrawer import NavigationDrawer
from kivy.clock import Clock
from kivy.properties import NumericProperty,StringProperty,ListProperty,DictProperty
from kivy.lang import Builder
from kivy.uix.floatlayout import FloatLayout
from kivy.app import App
from kivy.config import Config
Config.set('graphics', 'height', 370)
Config.set('graphics', 'width', 770)
Builder.load_file("tabel.kv")
Builder.load_file("chart.kv")
# Builder.load_file("chartrpm.kv")

from kivy.uix.screenmanager import ScreenManager,WipeTransition
from css import *
Builder.load_string("""
# :attr:`ScreenManager.transition` property::
<Ml>:
    NavigationDrawer:
        anim_type :"slide_above_simple"
        id:nd
        BV
            pos_hint:{"center_x":.5,"center_y":.5}
            BtnCavian:
                text:"DashBoard"
                font_size:self.height/3
                on_press:
                    sm.current="0"
                    nd.toggle_state(False)
            BtnCavian:
                text:"List"
                font_size:self.height/3
                on_press:
                    sm.current="1"
                    nd.toggle_state(False)
            BtnCavian:
                text:"Chart"
                font_size:self.height/3
                on_press:
                    sm.current="2"
                    nd.toggle_state(False)
            BtnCavian:
                text:"Info"
                font_size:self.height/3
            BtnCavian:
            BtnCavian:
            BtnCavian:
            
        FloatLayout
            pos_hint:{"center_x":.5,"center_y":.5}
            ScreenManager:
                pos_hint:{"center_x":.5,"center_y":.5}
                id:sm
                Screen:
                    pos_hint:{"center_x":.5,"center_y":.5}
                    name:"0"
                    Dash:
                        id:0
                Tabel:
                    name:"1"
                    pos_hint:{"center_x":.5,"center_y":.5}
                Screen:
                    name:"2"  
                    pos_hint:{"center_x":.5,"center_y":.5}
                    Grafik
                    
    BtnCavian:
        # source:"img/setting.png"
        text:"  Menu"
        size_hint:.2,.1
        pos_hint:{"x":0,"y":0}
        on_press:nd.toggle_state(True)
        font_size:self.height/1.5
""")

class ChartRpm(Graph):
    def __init__(self,*args,**kwargs):
        super(ChartRpm,self).__init__(**kwargs)
        self.size_hint=None,1
        self.width="25sp"
        
        

class ChartTps(Graph):
    def __init__(self,*args,**kwargs):
        super(ChartTps,self).__init__(**kwargs)
        self.size_hint=None,1
        self.width="25sp"
class ChartIat(Graph):
    def __init__(self,*args,**kwargs):
        super(ChartIat,self).__init__(**kwargs)
        self.size_hint=None,1
        self.width="25sp"

class ChartMap(Graph):
    def __init__(self,*args,**kwargs):
        super(ChartMap,self).__init__(**kwargs)
        self.size_hint=None,1
        self.width="25sp"
class ChartBat(Graph):
    def __init__(self,*args,**kwargs):
        super(ChartBat,self).__init__(**kwargs)
        self.size_hint=None,1
        self.width="25sp"
class ChartInj(Graph):
    def __init__(self,*args,**kwargs):
        super(ChartInj,self).__init__(**kwargs)
        self.size_hint=None,1
        self.width="25sp"
class ChartAdv(Graph):
    def __init__(self,*args,**kwargs):
        super(ChartAdv,self).__init__(**kwargs)
        self.size_hint=None,1
        self.width="25sp"

class Chart(Graph):
    def __init__(self,*args,**kwargs):
        super(Chart,self).__init__(**kwargs)


        
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
        "iat":ChartIat(),
        "map":ChartMap(),
        "bat":ChartBat(),
        "inj":ChartInj(),
        "adv":ChartAdv(),
    })
    # self.add_widget(maingrafik)
    def __init__(self, **kwargs):
        super(Grafik,self).__init__(**kwargs)
    def add(self,data):
        # print(data)
        self.ids["ylabel"].add_widget(self.chartitem[data])
    def remove(self,data):
        print(data)
        self.ids["ylabel"].remove_widget(self.chartitem[data])
class Ml(FloatLayout):
    screen_count=NumericProperty(0)
    def __init__(self, **kwargs):
        super(Ml,self).__init__(**kwargs)
        self.ids["sm"].transition=WipeTransition()
    def change_screen(self):
        self.screen_count+=1
        if self.screen_count>2:
            self.screen_count=0
        print(self.screen_count)
        self.ids["sm"].current=str(self.screen_count)
import sys
class H(App):
    def build(self):
        return Ml()
    def on_stop(self):
        return sys.exit()
if __name__=="__main__":
    H().run()
