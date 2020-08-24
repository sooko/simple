from kivy.config import Config
Config.set('graphics', 'height', 370)
Config.set('graphics', 'width', 770)
# from error_message import install_exception_handler
# from kivy.garden.graph import Graph,MeshLinePlot,LinePlot
from kivy.garden.navigationdrawer import NavigationDrawer
from kivy.clock import Clock
from kivy.properties import NumericProperty,StringProperty,ListProperty,DictProperty
from kivy.lang import Builder
from kivy.uix.floatlayout import FloatLayout
from kivy.app import App
from data_throuble import DTC
import binascii
from binascii import hexlify,unhexlify
from dash import Dash
from chart import Grafik
from ecmid import ecmid
from tabel import Tabel
Builder.load_file("ml.kv")
from struct import unpack
from tcp import TwisApp
class Clear_DTC(FloatLayout):
    pass
class Ml(FloatLayout):
    children_layout=StringProperty("")
    chart_count=NumericProperty(0)
    rpm_val =NumericProperty(0)
    tps_val =NumericProperty(0)
    ect_val =NumericProperty(0)
    iat_val =NumericProperty(0)
    map_val =NumericProperty(0)
    bat_volt=NumericProperty(0)
    vss_val =NumericProperty(0)
    inj_val =NumericProperty(0)
    adv_val =NumericProperty(0)
    gigi=DictProperty({
        "80":"6",
        "10":"5",
        "08":"4",
        "04":"3",
        "02":"2",
        "01":"1",
        "00":"-",
        "20":"-"
    })
    
    state=NumericProperty(0)
    dash=None
    chart=None
    G=DictProperty({})
    Wg=DictProperty({})
    twis=None
    tabel=None
    init_cmd    ="fe04728c"
    delay_init  ="250"
    baud_init   ="48"
    baud_main   ="10400"
    cmd_initial=ListProperty([  "7205710018",
                                "7205710018",
                                "7205730016",
                                "7205711008",#10
                                "7205711701",#17
                                "7205711602",#16
                                "7205730016",
                                "7205711305",#13
                                "7205730016",
                                "7205710018"])
    main_cmd=None
    oxi_cmd="72057120f8"
    his_cmd="7205730115"
    cur_cmd="7205740114"
    act_cmd="720571d147"
    tip_cmd="7205710018" #get_model
    init_count=NumericProperty(0)
    request_count=NumericProperty(0)
    list_his=ListProperty([])
    list_cur=ListProperty([])
    twist_state=StringProperty("")
    list_request=ListProperty([])
    return_list_request=ListProperty()
    dash=Dash()
    tabel_type=NumericProperty(0)
    twis=TwisApp()
    clear_dtc=Clear_DTC()
    def __init__(self, **kwargs):
        super(Ml,self).__init__(**kwargs)
        Clock.schedule_once(self.delay,4)
        self.kontainer.add_widget(self.dash)
        self.dash.bind(on_hapus_dtc=self.ok)
    def delay(self,dt):
        self.twis.connect_to_server("192.168.4.1")
        self.twis.start_looping=True
        self.twis.bind(status=self.on_twis_status)
        self.twis.print_data=self.on_twis_data_masuk 
        self.list_request=[  
                            self.his_cmd,
                            self.main_cmd,
                            self.act_cmd,
                            self.oxi_cmd,
                            self.main_cmd,
                            self.act_cmd,
                            self.oxi_cmd,
                            self.main_cmd,
                            self.cur_cmd,
                            self.main_cmd,
                            ]
        self.chart=Grafik()
        self.tabel=Tabel()
        self.Wg={"DashBoard":self.dash,
                "Chart":self.chart,
                "List":self.tabel,
                "Clear_DTC":self.clear_dtc
        }
        self.G=self.dash.G
        Clock.schedule_once(self.delay2,1)
    def delay2(self,dt):
        Clock.schedule_interval(self.login,1)
        Clock.schedule_interval(self.initial,.1)
        Clock.schedule_interval(self.make_chart,.1)
    def change_widget(self,data):
        self.kontainer.clear_widgets()
        self.kontainer.add_widget(self.Wg[data])
        self.children_layout=data
        self.chart.plot_tps.points.clear()
        self.chart.plot_rpm.points.clear()
        self.chart.plot_iat.points.clear()
        self.chart.plot_map.points.clear()
        self.chart.plot_bat.points.clear()
        self.chart.plot_inj.points.clear()
        self.chart.plot_adv.points.clear()
        self.chart.xmax=100
        self.chart.xmin=0
        self.chart_count=0
        if data=="Chart":
            self.list_request=[
                self.oxi_cmd,
                self.main_cmd,
                self.oxi_cmd,
                self.main_cmd,
                self.oxi_cmd,
                self.main_cmd,
                self.oxi_cmd,
                self.main_cmd,
                self.oxi_cmd,
                self.main_cmd]
            self.return_list_request=[
                self.oxi_cmd,
                self.main_cmd,
                self.oxi_cmd,
                self.main_cmd,
                self.oxi_cmd,
                self.main_cmd,
                self.oxi_cmd,
                self.main_cmd,
                self.oxi_cmd,
                self.main_cmd]
            
        else:
            self.list_request=[  
                self.his_cmd,
                self.main_cmd,
                self.act_cmd,
                self.oxi_cmd,
                self.main_cmd,
                self.act_cmd,
                self.oxi_cmd,
                self.main_cmd,
                self.cur_cmd,
                self.tip_cmd]
            self.return_list_request=[  
                self.his_cmd,
                self.main_cmd,
                self.act_cmd,
                self.oxi_cmd,
                self.main_cmd,
                self.act_cmd,
                self.oxi_cmd,
                self.main_cmd,
                self.cur_cmd,
                self.tip_cmd]
            
    def on_twis_status(self,a,b):
        self.twist_state=b
        if self.twist_state!="Connected":
            self.state=0
    def on_twis_data_masuk(self,b):
        if "fe04728c0e04727c" in hexlify(b).decode():
            self.state=1
        self.get_table_type(b)
        self.get_ecm_id(b)
        print(hexlify(b))
        if self.main_cmd !=None:
            mr=unhexlify(self.main_cmd)
            if mr in b and self.main_cmd=="7205711701" and len(b[9:])==20 and b[5]==2:
                data=unpack(">HBBxxxxBBBHBBBBBBB",b[9:])
                dat1=unpack(">HBBBBxxxxBHBBBBBBB",b[9:])
                #dat3=unpack(">HBBBBBBBBBHBBBBBBB",b[9:])
                dat9=unpack(">H9BH7B",b[9:])
                #dat3=unpack(">HBBBBBBBBBHBBBBBBB",b[9:])
                self.rpm_val    =data[0] 
                self.tps_volt   =data[1] *5/256
                self.tps_val    =data[2] /2
                self.ect_volt   =data[3] *5/256  if data[3]!=255 else dat1[3]*5/256
                self.ect_val    =data[4] -40     if data[4]!=255 else dat1[4]-40
                self.bat_volt   =data[5] /10
                self.inj_val    =data[6] /200
                self.adv_val    =data[7] /2-64
                self.alt_val    =data[8] /1000
                self.vss_val    =data[9] 
                try:
                    self.mod_val=self.mo[data[8]]
                except:
                    self.mod_val="0"
                self.dash.rpm=self.rpm_val
                self.dash.tps=self.tps_val
                self.dash.vss=self.vss_val
                self.dash.inj=self.inj_val
                self.dash.adv=self.adv_val
                self.dash.temp=self.ect_val
                self.G[0].unit="volt"
                self.G[0].key="battery"
                self.G[0].value=self.bat_volt
                self.G[0].svalue="{:.1f}".format(self.bat_volt)
                self.G[0].max=16
                if self.bat_volt > 15.5   or self.bat_volt < 12 :
                    self.dash.I[4].color=[1,0,0,1]
                else:
                    self.dash.I[4].color=[0,1,0,1]
            elif mr in b and self.main_cmd=="7205711602" and len(b[9:])==27 and b[5]==2:
                data=unpack(">H19BH4B",b[9:])
                self.rpm_val    =data[0]
                self.aps1_volt  =data[1]*5/256
                self.aps2_volt  =data[2]*5/256
                self.aps1_val   =data[3]/2
                self.aps2_val   =data[4]/2
                self.tps1_volt  =data[5]*5/256
                self.tps2_volt  =data[6]*5/256
                self.tps1_val   =data[7]/2
                self.tps2_val   =data[8]/2
                self.corel_val  =data[9]
                self.ect_volt   =data[10]*5/256
                self.ect_val    =data[11]-40
                self.iat_volt   =data[12]*5/256
                self.iat_val    =data[13]-40
                self.map_volt   =data[14]*5/256
                self.map_val    =data[15]
                self.bat_volt   =data[18]/10
                self.vss_val    =data[19]
                self.inj_val    =data[20]/200
                self.adv_val    =data[21]/2-64
                
                self.dash.rpm=self.rpm_val
                self.dash.tps=self.tps_val
                self.dash.vss=self.vss_val
                self.dash.inj=self.inj_val
                self.dash.adv=self.adv_val
                self.dash.temp=self.ect_val
                self.G[0].key="battery"
                self.G[0].unit="volt"
                self.G[0].value=self.bat_volt
                self.G[0].svalue="{:.1f}".format(self.bat_volt)
                self.G[0].max=16
                self.G[1].key="IAT"
                self.G[1].unit=" [sup] O[/sup]c"
                self.G[1].value=self.iat_val
                self.G[1].svalue="{:.1f}".format(self.iat)
                self.G[1].max=60
                self.G[2].key="MAP"
                self.G[2].unit="kpa"
                self.G[2].value=self.map_val
                self.G[2].svalue="{:.1f}".format(self.map)
                self.G[2].max=120
            elif mr in b and self.main_cmd=="7205711107" and len(b[9:])==21 and b[5]==2:
                
                data =unpack(">H12BHBBH", b[9:-1])
                datav=unpack(">H12BH4B", b[9:-1])
                
                self.rpm_val    =data[0]
                self.tps_volt   =data[1]*5/256
                self.tps_val    =data[2]/2
                self.ect_volt   =data[3]*5/256
                self.ect_val    =data[4]-40
                self.iat_volt   =data[5]*5/256
                self.iat_val    =data[6]-40
                self.map_volt   =data[7]*5/256
                self.map_val    =data[8]
                self.bat_volt   =data[11]/10
                self.vss_val    =data[12]
                self.inj_val    =data[13]/200
                self.adv_val    =data[14]/2-64
                self.pul_val    =data[15]
                self.iac_val    =data[16]/10000
                self.dash.rpm=self.rpm_val
                self.dash.tps=self.tps_val
                self.dash.vss=self.vss_val
                self.dash.inj=self.inj_val
                self.dash.adv=self.adv_val
                self.dash.temp=self.ect_val
                self.G[0].key="battery"
                self.G[0].unit="volt"
                self.G[0].value=self.bat_volt
                self.G[0].svalue="{:.1f}".format(self.bat_volt)
                self.G[0].max=16
                self.G[1].key="IAT"
                self.G[1].unit=" [sup] O[/sup]c"
                self.G[1].value=self.iat_val
                self.G[1].svalue="{:.1f}".format(self.iat)
                self.G[1].max=60
                self.G[2].key="MAP"
                self.G[2].unit="kpa"
                self.G[2].value=self.map_val
                self.G[2].svalue="{:.1f}".format(self.map)
                self.G[2].max=120
                
            elif mr in b and self.main_cmd=="7205711305" and len(b)==24 and b[5]==2:
                data=(unpack(">H9BHBB",b[9:]))
                self.rpm_val    =data[0]
                self.tps_volt   =data[1]*5/256
                self.tps_val    =data[2]/2
                self.ect_volt   =data[3]*5/256
                self.ect_val    =data[4]-40
                self.iat_volt   =data[5]*5/256
                self.iat_val    =data[6]-40
                self.map_volt   =data[7]*5/256
                self.map_val    =data[8]
                self.bat_volt   =data[9]/10
                self.inj_val    =data[10]/400
                self.adv_val    =data[11]/2-64
                
                self.dash.rpm=self.rpm_val
                self.dash.tps=self.tps_val
                self.dash.vss=self.vss_val
                self.dash.inj=self.inj_val
                self.dash.adv=self.adv_val
                self.dash.temp=self.ect_val
                self.G[0].key="battery"
                self.G[0].unit="volt"
                self.G[0].value=self.bat_volt
                self.G[0].svalue="{:.1f}".format(self.bat_volt)
                self.G[0].max=16
                self.G[1].key="IAT"
                self.G[1].unit=" [sup] O[/sup]c"
                self.G[1].value=self.iat_val
                self.G[1].svalue="{:.1f}".format(self.iat)
                self.G[1].max=60
                self.G[2].key="MAP"
                self.G[2].unit="kpa"
                self.G[2].value=self.map_val
                self.G[2].svalue="{:.1f}".format(self.map)
                self.G[2].max=120
            elif mr in b and self.main_cmd=="7205711008" and len(b)==27 and b[5]==2:
                data=(unpack(">H12BHBB",b[9:]))
                self.rpm_val    =data[0]
                self.tps_volt   =data[1]*5/256
                self.tps_val    =data[2]/2
                self.ect_volt   =data[3]*5/256
                self.ect_val    =data[4]-40
                self.iat_volt   =data[5]*5/256
                self.iat_val    =data[6]-40
                self.map_volt   =data[7]*5/256
                self.map_val    =data[8]
                self.bat_volt   =data[11]/10
                self.vss_val    =data[12]
                self.inj_val    =data[13]/200
                self.adv_val    =data[14]/2-64
                self.dash.rpm=self.rpm_val
                self.dash.tps=self.tps_val
                self.dash.vss=self.vss_val
                self.dash.inj=self.inj_val
                self.dash.adv=self.adv_val
                self.dash.temp=self.ect_val
                self.G[0].key="battery"
                self.G[0].unit="volt"
                self.G[0].value=self.bat_volt
                self.G[0].svalue="{:.1f}".format(self.bat_volt)
                self.G[0].max=16
                self.G[1].key="IAT"
                self.G[1].unit=" [sup] O[/sup]c"
                self.G[1].value=self.iat_val
                self.G[1].svalue="{:.1f}".format(self.iat)
                self.G[1].max=60
                self.G[2].key="MAP"
                self.G[2].unit="kpa"
                self.G[2].value=self.map_val
                self.G[2].svalue="{:.1f}".format(self.map)
                self.G[2].max=120
            elif unhexlify(self.oxi_cmd) in b  and len(b[9:])==4:
                self.o2_volt    =unpack(">Hxx",b[9:])[0]/13.142708/1000
                self.stf_val    =unpack(">xBxx",b[9:])[0]/128.25651
                self.afr_val    =self.stf_val*14.76
                self.G[3].key="o2"
                self.G[3].unit="volt"
                self.G[3].value=self.o2_volt
                self.G[3].svalue="{:.2f}".format(self.o2_volt)
                self.G[3].max=5
                self.G[4].key="stf"
                self.G[4].unit="lamda"
                self.G[4].value=self.stf_val
                self.G[4].svalue="{:.2f}".format(self.stf_val)
                self.G[4].max=2
                self.G[5].key="afr"
                self.G[5].unit=" : 1"
                self.G[5].value=self.afr_val
                self.G[5].svalue="{:.1f}".format(self.afr_val)
                self.G[5].max=30
            elif unhexlify(self.act_cmd) in b and len(b[9:])==7:  #actu
                data=hexlify(b[9:]).decode()
                self.ssw_val    ="on" if data[0]=="2" else "off"
                self.rts_val    ="on" if data[0]=="2" else "off"
                self.bas_val    ="on" if data[0]=="1" else "off"
                self.ss_val     ="on" if data[1]=="2" else "off"
                self.fan_val    ="on" if data[11]=="1" else "off"
                self.gg_sta     ="N" if data[1] =="1" else "-"
                self.ss_val     ="on" if data[1] =="2" else "off"
                self.fis_val    =data[-6]
                self.pom_val    ="on" if data[-5]=="1" or data[-5]=="5" else "off"
                try:
                    self.gg_val     =self.gigi[data[4:6]]
                except:
                    self.gg_val     ="N"
                self.dash.I[1].color=[0,1,0,1] if self.fan_val == "on" else [1,1,1,.1]
                self.dash.I[3].color=[1,.5,0,1] if self.ss_val == "on" else [1,1,1,.1]
                if self.main_cmd=="7205711602":
                    self.dash.I[2].text=self.gg_val
                else:
                    self.dash.I[2].text=self.gg_sta
            elif unhexlify(self.his_cmd) in b and len(b[9:])<16:
                data=hexlify(b[9:]).decode()
                self.list_his  =["Tersimpan kerusakan pada "+ DTC[i] + " "+ i[0:2]+"-" + i[2:4] for i in DTC if i in data]
                self.dash.I[0].color=[1,.5,0,1] if self.list_his !=[] else [1,1,1,.1]
            elif unhexlify(self.cur_cmd) in b and len(b[9:])<16:
                data=hexlify(b[9:]).decode()
                self.list_cur  =["Terjadi   kerusakan pada " + DTC[i]+ " "+ i[0:2]+"-" + i[2:4] for i in DTC if i in data]
                self.dash.I[0].color=[1,.5,0,1] if self.list_his !=[] else [1,1,1,.1]
            e=self.list_his+self.list_cur
            for i in e:
                if i not in self.dash.data_eror:
                    self.dash.data_eror+=i+"\n"
    def login(self,dt):
        if self.twist_state!="Connected":
            self.state=0
        if self.state==0:
            # self.main_cmd=None
            self.dash.data_eror=""
            self.twis.send_message("{},{},{},{},init".format(self.init_cmd,self.delay_init,self.baud_init,self.baud_main)) 
    def initial(self,dt):
        if self.twist_state=="Connected":
            self.init_count+=1
            if self.init_count==len(self.cmd_initial):
                self.init_count=0
            if self.state==1:
                if self.main_cmd==None:
                    self.twis.send_message(self.cmd_initial[self.init_count])
                else:
                    self.twis.send_message(self.list_request[self.init_count])
                    
    def get_table_type(self,b):
        if unhexlify("7205711701") in b and len(b[9:])==20:
            self.main_cmd   ="7205711701"
            self.tabel_type=1
        if unhexlify("7205711008") in b and len(b)==27:
            self.main_cmd   ="7205711008"
            self.tabel_type=2
        if unhexlify("7205711602") in b and len(b[9:])==27:
            self.main_cmd   ="7205711602"
            self.tabel_type=3
        if unhexlify("7205711305") in b and len(b)==24:
            self.main_cmd   ="7205711305"
            self.tabel_type=4
    def on_tabel_type(self,a,b):
        if self.children_layout=="Chart":
            self.list_request=[
                self.oxi_cmd,
                self.main_cmd,
                self.oxi_cmd,
                self.main_cmd,
                self.oxi_cmd,
                self.main_cmd,
                self.oxi_cmd,
                self.main_cmd,
                self.oxi_cmd,
                self.main_cmd]
            self.terurn_list_request=[
                self.oxi_cmd,
                self.main_cmd,
                self.oxi_cmd,
                self.main_cmd,
                self.oxi_cmd,
                self.main_cmd,
                self.oxi_cmd,
                self.main_cmd,
                self.oxi_cmd,
                self.main_cmd]
            
        else:
            self.list_request=[  
                self.his_cmd,
                self.main_cmd,
                self.act_cmd,
                self.oxi_cmd,
                self.main_cmd,
                self.act_cmd,
                self.oxi_cmd,
                self.main_cmd,
                self.cur_cmd,
                self.tip_cmd]
            self.return_list_request=[  
                self.his_cmd,
                self.main_cmd,
                self.act_cmd,
                self.oxi_cmd,
                self.main_cmd,
                self.act_cmd,
                self.oxi_cmd,
                self.main_cmd,
                self.cur_cmd,
                self.tip_cmd]

    def get_ecm_id(self,b):
        if "7205710018" in hexlify(b).decode() and len(b)==20:
            self.ecm_id=hexlify(b[9:9+5]).decode()
            try:
                self.pn     =ecmid[self.ecm_id.upper()]["pn"]
                self.model  =ecmid[self.ecm_id.upper()]["model"]
                self.years  =ecmid[self.ecm_id.upper()]["years"]
                self.dash.model=self.model
                self.dash.years=self.years
                self.dash.pn=self.pn
            except:
                self.pn   ="auto"
                self.model="-"
                self.years="-"
    def refresh(self):
        pass
    def make_chart(self,dt):
        if self.ids["kontainer"].children[0]==self.chart:
            if self.chart:
                self.chart_count+=self.chart.chart_speed
                rpm_point=(self.chart_count,self.rpm_val/1500)
                tps_point=(self.chart_count,self.tps_val/10)
                iat_point=(self.chart_count,self.iat_val/6)
                map_point=(self.chart_count,self.map_val/12)
                bat_point=(self.chart_count,self.bat_volt/1.5)
                inj_point=(self.chart_count,self.inj_val)
                adv_point=(self.chart_count,self.adv_val/6)
                self.chart.plot_tps.points.append(tps_point)
                self.chart.plot_rpm.points.append(rpm_point)
                self.chart.plot_iat.points.append(iat_point)
                self.chart.plot_map.points.append(map_point)
                self.chart.plot_bat.points.append(bat_point)
                self.chart.plot_inj.points.append(inj_point)
                self.chart.plot_adv.points.append(adv_point)
                if self.chart_count>100:
                    self.chart.xmax+=self.chart.chart_speed
                    self.chart.xmin+=self.chart.chart_speed
                    self.chart.plot_tps.points.remove(self.chart.plot_tps.points[0])
                    self.chart.plot_rpm.points.remove(self.chart.plot_rpm.points[0])
                if self.chart_count>500:
                    self.chart.plot_tps.points.clear()
                    self.chart.plot_rpm.points.clear()
                    self.chart.plot_iat.points.clear()
                    self.chart.plot_map.points.clear()
                    self.chart.plot_bat.points.clear()
                    self.chart.plot_inj.points.clear()
                    self.chart.plot_adv.points.clear()
                    self.chart.xmax=100
                    self.chart.xmin=0
                    self.chart_count=0
    def ok(self,a):
        self.list_request=["7205600326",
        "7205600326",
        "7205600326",
        "7205600326",
        "7205600326",
        "7205710018",
        "720500F198",
        "7205600326",
        "7205600326",
        "7205710018",
        "720500F198",
        ]
        Clock.unschedule(self.delay3)
        Clock.schedule_once(self.delay3,3)
        self.dash.data_eror=""
    def delay3(self,dt):
        # self.main_cmd=None

        self.state=0
        self.list_request=self.return_list_request
        self.dash.data_eror=""
import sys
class FidashBoard(App):
    def build(self):
        return Ml()
    def on_stop(self):
        sys.exit()
if __name__=="__main__":
    FidashBoard().run()
