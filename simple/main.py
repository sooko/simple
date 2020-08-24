from kivy.config import Config
Config.set('graphics', 'height', 370)
Config.set('graphics', 'width', 770)
from css import *
from kivy.lang import Builder
Builder.load_file("tabel.kv")
Builder.load_file("dash.kv")
from kivy.garden.navigationdrawer import NavigationDrawer
Builder.load_string("""
<Simple>:
    canvas:
        Color:
            rgba:0,0,.7,.5
        Rectangle:
            size:self.size
            pos:self.pos
            source:"img/img27.jpg"
    BoxLayout
        ScreenManager:
            id:sm
            Screen:
                id:root_tabel
                name:"table"
                Tabel:
                    tipe:root.tipe
                    id:tabel
            Screen:
                name:"dash"
                Dash
            Screen:
                name:"chart"
            Screen:
                name:"dtc"
            Screen:
                name:"info"
""")
from kivy.app import App
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.properties import NumericProperty,StringProperty,ListProperty,DictProperty
from kivy.clock import Clock
class Tabel(FloatLayout):
    
    rpm ="RPM-Puratan Mesin"
    tps ="TPS-Posisi Throttle"
    bat ="BAT-Tegangan Battery"
    ect ="ECT-Suhu Air Pendingin"
    iac ="IAC-Perintah Katup Udara Masuk"
    eot ="EOT-Suhu Oli"
    suhu="EOT-Suhu Oli"
    iat ="IAT-Suhu Udara Masuk"
    map ="MAP-tekanan Udara Masuk"
    inj ="INJ-Lebar Pulsa Injektor"
    adv ="ADV-Sudut Pengapian"
    o2  ="O2-Sensor Oksigen"
    bas ="BAS-Sensor kemiringan"
    stf ="STF-Campuran Bahan Bakar"
    pul ="IAC-Status Katup Udara Masuk"
    pom ="POM-Pompa Bahan Bakar"
    fan ="FAN-kipas Pendingin"
    gg  ="GG-Gigi Transmisi"
    eva ="EVA-Status Evaporator"
    scs ="SCS-Servis Check Signal"
    mil ="Jumlah Kode Error tersimpan"
    mil1 ="Jumlah Kode Error terjadi"
    ss  ="SS-Standart Samping"
    ssw ="SSW-Switch Stater"
    rts ="STS-Relay Stater"
    fis ="FIS-Fast Idle Switch"
    mod ="MOD-Mode Altitude"
    alt ="ALT-Koreksi Altitude"
    pr  ="PR-Pair Control"
    vss="vehicle speed sensor"
    iac_tar ="IAC-Katup Udara Masuk Target"
    tps1="TPS1-Posisi Throlle 1"
    tps2="TPS2-Posisi Throlle 2"
    aps1="APS1-Posisi Handle Gas 1"
    aps2="APS2-Posisi Handle Gas 2"
    korel="Nilai Korelasi"
    afr="AFR- Air Fuel Ratio"
    list_item=ListProperty([])
    list_value=ListProperty([])
    list_volt=ListProperty([])
    dict_item=DictProperty({})
    tipe=StringProperty("")
    def __init__(self, **kwargs):
        super(Tabel,self).__init__(**kwargs)
        self.c=0
        self.d=100
        self.list_item=[self.rpm,self.tps]
        self.list_value=[1,2]
        self.list_volt=[1,2]
class LabelValue(Label):
    no=StringProperty("")
    item=StringProperty("")
    value=StringProperty("")
    volt=StringProperty("")
    def __init__(self, **kwargs):
        super(LabelValue,self).__init__(**kwargs)
class Dash(FloatLayout):
    pass
class Simple(FloatLayout):
    tipe=StringProperty("")
    def __init__(self, **kwargs):
        super(Simple,self).__init__(**kwargs)
    def change_table(self):
        self.ids["root_tabel"].clear_widgets()
    def h_btn(self,data):
        for i in self.bx_btnimg.children:
            i.color=.5,.5,.5,1
        data.color=[0,1,1,1]
        self.ids["sm"].current=data.name
class H(App):
    def build(self):
        return Simple()
if __name__=="__main__":
    H().run()
