
from kivy.garden.graph import Graph,MeshLinePlot,SmoothLinePlot
from kivy.clock import Clock
from kivy.properties import NumericProperty,StringProperty,ListProperty,DictProperty
from kivy.lang import Builder
from kivy.uix.floatlayout import FloatLayout
from css import *
Builder.load_file("chart.kv")
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
class Grafik(FloatLayout):
    xmax=NumericProperty(100)
    xmin=NumericProperty(0)
    plot_rpm=None
    plot_tps=None
    plot_iat=None
    plot_map=None
    plot_bat=None
    plot_inj=None
    plot_adv=None
    AllPlot=DictProperty({})
    chart_speed=NumericProperty(.5)
    chartitem=DictProperty({
        "rpm":ChartRpm(),
        "tps":ChartTps(),
        "iat":ChartIat(),
        "map":ChartMap(),
        "bat":ChartBat(),
        "inj":ChartInj(),
        "adv":ChartAdv(),
    })

    def __init__(self, **kwargs):
        super(Grafik,self).__init__(**kwargs)
        Clock.schedule_once(self.delay,1)
    def delay(self,dt):
        self.plot_rpm = SmoothLinePlot(color=[1, 0, 0, 1])
        self.plot_tps = SmoothLinePlot(color=[0, 1, 0, 1])
        self.plot_iat = SmoothLinePlot(color=[0, 0, 1, 1])
        self.plot_map = SmoothLinePlot(color=[1, 1, 0, 1])
        self.plot_bat = SmoothLinePlot(color=[1, 0, 1, 1])
        self.plot_inj = SmoothLinePlot(color=[0, 1, 1, 1])
        self.plot_adv = SmoothLinePlot(color=[1, 1, 1, 1])
        self.AllPlot  ={        "rpm":self.plot_rpm,
                                "tps":self.plot_tps,
                                "iat":self.plot_iat,
                                "map":self.plot_map,
                                "bat":self.plot_bat,
                                "inj":self.plot_inj,
                                "adv":self.plot_adv
                                }

    def add(self,data):
        self.ids["ylabel"].add_widget(self.chartitem[data])
        self.ids["main_chart"].add_plot(self.AllPlot[data])
    def remove(self,data):
        self.ids["ylabel"].remove_widget(self.chartitem[data])
        self.ids["main_chart"].remove_plot(self.AllPlot[data])
    def set_chart_speed(self,data):
        
        if data=="200ms/div":
            self.chart_speed=.5
        if data=="100ms/div":
            self.chart_speed=1
        if data=="50ms/div":
            self.chart_speed=1
        
# from kivy.app import App

# class M(App):
#     def build(self):
#         return Grafik()
# if __name__=="__main__":
#     M().run()
