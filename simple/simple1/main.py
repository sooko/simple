from kivy.config import Config
Config.set('graphics', 'height', 370)
Config.set('graphics', 'width', 770)
from tabelgraph import Dash
from kivy.lang import Builder
from kivy.app import App
from kivy.uix.floatlayout import FloatLayout
from twis import TwisApp
from binascii import hexlify,unhexlify
from kivy.properties import StringProperty,NumericProperty,ListProperty,DictProperty
from kivy.clock import Clock
from ecmid import ecmid
from data_throuble import DTC
from struct import unpack
from css import *
from allvar import *
Builder.load_file("ml.kv")
class Ml(FloatLayout):
    rpm_val=NumericProperty(0)
    tps_val=NumericProperty(0)
    tps_volt=NumericProperty(0)
    ect_val=NumericProperty(0)
    ect_volt=NumericProperty(0)
    mo=DictProperty({
        128:"1",
        103:"1",
        102:"2",
        60:"3",
        89:"4"
    })
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
    twis=TwisApp()
    state=NumericProperty(0)
    init_cmd    ="fe04728c"
    delay_init  ="250"
    baud_init   ="48"
    baud_main   ="10400"
    twis_state=StringProperty("connecting ....")
    list_login_state=["connecting","connecting..","connecting....","connecting......."]
    state=NumericProperty(0)
    init_count=0
    request_count=0
    cmd_initial=ListProperty(["7205710018","7205710018","7205730016","7205711008","7205711701","7205711602","7205730016","7205711305","7205730016"])
    main_cmd=None
    oxi_cmd="72057120f8"
    his_cmd="7205730115"
    cur_cmd="7205740114"
    act_cmd="720571d147"
    l_val_main=ListProperty([])
    l_volt_main=ListProperty([])
    l_item_main=ListProperty([])
    l_val_oxi=ListProperty([])
    l_volt_oxi=ListProperty([])
    l_item_oxi=ListProperty([])
    l_val_act=ListProperty([])
    l_volt_act=ListProperty([])
    l_item_act=ListProperty([])
    l_val_mil=ListProperty([])
    l_volt_mil=ListProperty([])
    l_item_mil=ListProperty([])
    l_val_mil1=ListProperty([])
    l_volt_mil1=ListProperty([])
    l_item_mil1=ListProperty([])
    all_item=ListProperty([])
    all_val=ListProperty([])
    all_volt=ListProperty([])
    pn=StringProperty("")
    model=StringProperty("")
    years=StringProperty("")
    lis_request=ListProperty([])
    count_login=NumericProperty(0)
    log1=StringProperty("")
    log2=StringProperty("")
    log3=StringProperty("")
    disp_count=NumericProperty(0)
    def __init__(self, **kwargs):
        super(Ml,self).__init__(**kwargs)
        Clock.schedule_once(self.delay,2)
    def delay(self,dt):
        self.twis.connect_to_server("192.168.4.1")
        self.twis.bind(status=self.on_twis_status)
        self.twis.print_data=self.on_twis_data_masuk 
        self.twis.start_looping=True
        Clock.schedule_interval(self.login,1)
        Clock.schedule_interval(self.initial,.1)
    def login(self,dt):
        if self.twis_state!="Connected":
            self.state=0
        if self.state==0:
            self.twis.send_message("{},{},{},{},init".format(self.init_cmd,self.delay_init,self.baud_init,self.baud_main)) 
    def initial(self,dt):
        if self.state==1:
            self.init_count+=1
            if self.init_count==len(self.cmd_initial):
                self.init_count=0
            self.twis.send_message(self.cmd_initial[self.init_count])
        if self.state==2 and self.main_cmd:
            self.lis_request=[self.main_cmd,self.oxi_cmd,self.his_cmd,self.cur_cmd,self.act_cmd]
            self.request_count+=1
            if self.request_count==len(self.lis_request):
                self.request_count=0
            self.twis.send_message(self.lis_request[self.request_count])
    def on_twis_status(self,a,b):
        self.twis_state=b
        if self.twis_state!="Connected":
            self.state=0
            self.main_cmd=None
    def on_twis_data_masuk(self,b): 
        print(hexlify(b))
        if "7205710018" in hexlify(b).decode() and len(b)==20:
            self.ecm_id=hexlify(b[9:9+5]).decode()
            try:
                self.pn     =ecmid[self.ecm_id.upper()]["pn"]
                self.model  =ecmid[self.ecm_id.upper()]["model"]
                self.years  =ecmid[self.ecm_id.upper()]["years"]
                print(self.pn,self.model,self.years)
            except:
                self.pn   =""
                self.model=""
                self.years=""
            self.ids["dash"].model=self.model
            self.ids["dash"].pn=self.pn
            self.ids["dash"].years=self.years
        if self.state==0:
            if "0e04727c" in hexlify(b).decode():
                self.state=1
        if self.state==1:
            if unhexlify("7205711701") in b and len(b[9:])==20:
                self.main_cmd   ="7205711701"
            if unhexlify("7205711008") in b and len(b)==27:
                self.main_cmd   ="7205711008"
            if unhexlify("7205711602") in b and len(b[9:])==27:
                self.main_cmd   ="7205711602"
            if unhexlify("7205711305") in b and len(b)==24:
                self.main_cmd   ="7205711305"
        if self.state==2:
            if hexlify(b).decode()==self.main_cmd:
                self.state=0
            mr=unhexlify(self.main_cmd)
            if mr in b and self.main_cmd=="7205711701" and len(b[9:])==20:
                data=unpack(">HBBxxxxBBBHBBBBBBB",b[9:])
                dat1=unpack(">HBBBBxxBBBHBBBBBBB",b[9:])
                self.rpm_val    =data[0] 
                self.tps_volt   =data[1] *5/256
                self.tps_val    =data[2] /2
                self.ect_volt   =data[3] *5/256  if data[3]!=255 else dat1[3]*5/256
                self.ect_val    =data[4] -40     if data[4]!=255 else dat1[3]-40
                self.bat_volt   =data[5] /10
                self.inj_val    =data[6] /200
                self.adv_val    =data[7] /2-64
                self.alt_val    =data[8] /1000
                self.vss_val    =data[9] 
                try:
                    self.mod_val=self.mo[data[8]]
                except:
                    self.mod_val="0"
                self.l_val_main =[self.rpm_val,self.tps_val    ,self.ect_val ,"-"          ,self.inj_val,self.adv_val,self.alt_val,self.vss_val,self.mod_val]
                self.l_volt_main=["-"         ,self.tps_volt  ,self.ect_volt,self.bat_volt,"-"         ,"-"         ,"-","-"         ,"-"]
                self.l_item_main=[rpm         ,tps            ,ect          ,bat          ,inj          ,adv         ,alt,vss         ,mod]
                # self.log1 = "rpm :{}\ntps :{}\ntemp :{}\nbat :{}\ninj :{}\nadv :{}\nadv :{}\nalt :{}\nmod:{}\n".format(self.rpm_val,self.tps_val,self.ect_val ,self.bat_volt,self.inj_val,self.adv_val,self.alt_val,self.vss_val,self.mod_val)
            if mr in b and self.main_cmd=="7205711602" and len(b[9:])==27:
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
                self.l_item_main=[rpm           ,tps1            ,tps2          ,aps1          ,aps2          ,korel         ,ect           ,iat          ,map          ,bat          ,vss         ,inj         ,adv         ]
                self.l_val_main=[self.rpm_val   ,self.tps1_val   ,self.tps2.val ,self.aps1_val ,self.aps2_val ,self.corel_val,self.ect_val  ,self.iat_val ,self.map_val ,"-"          ,self.vss_val,self.inj_val,self.adv_val]
                self.l_volt_main=[self.rpm_volt ,self.tps1_volt  ,self.tps2.volt,self.aps1_volt,self.aps2_volt,"-"           ,self.ect_volt ,self.iat_volt,self.map_volt,self.bat_volt,"-"         ,"-"         ,"-"         ]
            if mr in b and self.main_cmd=="7205711107" and len(b[9:])==21:
                data=unpack(">H12BHBBH", b[9:-1])
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
                self.l_item_main =[rpm         ,tps           ,ect          ,iat           ,map          ,bat           ,vss              ,inj          ,adv         ,pul         ,iac         ]
                self.l_val_main  =[self.rpm_val,self.tps_val  ,self.ect_val ,self.iat_val  ,self.map_val ,"-"           ,self.vss_val     ,self.inj_val ,self.adv_val,self.pul_val,self.iac_val]
                self.l_volt_main =["-"         ,self.tps_volt ,self.ect_volt ,self.iat_volt,self.map_volt,self.bat_volt ,"-"               ,"-"         ,"-"         ,"-"         ,"-"         ]
            if mr in b and self.main_cmd=="7205711305" and len(b)==24:
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
                self.l_item_main =[rpm         ,tps           ,ect          ,iat            ,map         ,bat     ,inj          ,adv]
                self.l_val_main  =[self.rpm_val,self.tps_val  ,self.ect_val ,self.iat_val   ,self.map_val,"-"     ,self.inj_val ,self.adv_val]
                self.l_volt_main =["-"         ,self.tps_volt ,self.ect_volt ,self.iat_volt ,self.map_volt,self.bat_volt,"-","-"]
            if mr in b and self.main_cmd=="7205711008" and len(b)==27:
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
                self.l_item_main =[rpm         ,tps           ,ect          ,iat            ,map         ,bat     ,vss,         inj          ,adv]
                self.l_val_main  =[self.rpm_val,self.tps_val  ,self.ect_val ,self.iat_val   ,self.map_val,"-",self.vss_val     ,self.inj_val ,self.adv_val]
                self.l_volt_main =["-"         ,self.tps_volt ,self.ect_volt ,self.iat_volt ,self.map_volt,self.bat_volt,"-","-","-"]
            if unhexlify(self.oxi_cmd) in b  and len(b[9:])==4:
                self.o2_volt    =unpack(">Hxx",b[9:])[0]/13.142708/1000
                self.stf_val    =unpack(">xBxx",b[9:])[0]/128.25651
                self.afr_val    =self.stf_val*14.76
                self.l_item_oxi =[o2,stf,afr]
                self.l_val_oxi  =["-",self.stf_val,self.afr_val]
                self.l_volt_oxi =[self.o2_volt,"-","-"]
            if unhexlify(self.his_cmd) in b and len(b[9:])==8:
                data=hexlify(b[9:]).decode()
                self.list_hist  =[DTC[i] for i in DTC if i in data]
                self.l_item_mil =[mil]
                self.l_val_mil  =[str(len(self.list_hist))]
                self.l_volt_mil =["-"]
            if unhexlify(self.cur_cmd) in b and len(b[9:])==8:
                data=hexlify(b[9:]).decode()
                self.list_cur   =[DTC[i] for i in DTC if i in data]
                self.l_item_mil1 =[mil]
                self.l_val_mil1  =[str(len(self.list_cur))]
                self.l_volt_mil1 =["-"]
            if unhexlify(self.act_cmd) in b and len(b[9:])==7:  #actu
                data=hexlify(b[9:]).decode()
                self.ssw_val    ="on" if data[0]=="2" else "off"
                self.rts_val    ="on" if data[0]=="2" else "off"
                self.bas_val    ="on" if data[0]=="1" else "off"
                self.ss_val     ="on" if data[1]=="2" else "off"
                self.fan_val    ="on" if data[11]=="1" else "off"
                self.gg_sta     ="netral" if data[1] =="1" else "masuk"
                self.ss_val     ="on" if data[1] =="2" else "off"
                self.fis_val    =data[-6]
                self.gg_val     =self.gigi[data[4:6]]
                self.pom_val    ="on" if data[-5]=="1" or data[-5]=="5" else "off"
            self.all_item=self.l_item_main  +self.l_item_oxi  +self.l_item_mil  +self.l_item_mil1+["model","years","part number"]
            self.all_val =self.l_val_main   +self.l_val_oxi   +self.l_val_mil   +self.l_val_mil1+[self.model,self.years,self.pn]
            self.all_volt=self.l_volt_main  +self.l_volt_oxi  +self.l_volt_mil  +self.l_volt_mil1+["","",""]
            # for i in range (len(self.all_item)):
            #     self.ids["tabel"].l_item[i].text=self.all_item[i]
            #     self.ids["tabel"].l_val[i].text="{:.3f}".format(self.all_val[i]) if type(self.all_val[i])==float and len(str(self.all_val[i]))>6 else "{}".format(self.all_val[i])
            #     self.ids["tabel"].l_volt[i].text="{:.3f}".format(self.all_volt[i]) if type(self.all_volt[i])==float and len(str(self.all_volt[i]))>6 else "{}".format(self.all_volt[i])
            #     self.ids["tabel"].l_no[i].text=str(i)
    def on_state(self,a,b):
        print(b)
        if b==1:
            pass
    def down_display(self):
        if self.disp_count>0:
            self.disp_count-=1
        self.ids["dash"].change_display(str(self.disp_count))
    def up_display(self):
        if self.disp_count<3:
            self.disp_count+=1
        self.ids["dash"].change_display(str(self.disp_count))

import sys
class MyApp(App):
    def build(self):
        return Ml()
    def on_stop(self):
        return sys.exit()
if __name__=="__main__":
    MyApp().run()


