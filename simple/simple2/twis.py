from kivy.support import install_twisted_reactor
install_twisted_reactor()
import binascii
from twisted.internet import reactor, protocol
class EchoClient(protocol.Protocol):
    def connectionMade(self):
        self.factory.app.on_connection(self.transport)
    def dataReceived(self, data):
        self.factory.app.print_data(data)
class EchoClientFactory(protocol.ClientFactory):
    protocol = EchoClient
    def __init__(self, app):
        self.app = app
    def startedConnecting(self, connector):
        self.app.print_message('connecting')
    def clientConnectionLost(self, connector, reason):
        self.app.print_message('putus')
    def clientConnectionFailed(self, connector, reason):
        self.app.print_message('gagal')
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import StringProperty,NumericProperty,ListProperty,BooleanProperty
class TwisApp(FloatLayout):
    status = StringProperty("")
    connection = None
    textbox = None
    label = None
    data_masuk=StringProperty("")
    count=NumericProperty(0)
    start_looping=BooleanProperty(False)
    def __init__(self,*args,**kwargs):
        super(TwisApp,self).__init__(*args,**kwargs)

    def connecting(self):
        root = self.setup_gui()
        # self.connect_to_server()
    def setup_gui(self):
        self.textbox = TextInput(size_hint_y=.1, multiline=False)
        self.textbox.bind(on_text_validate=self.send_message)
        self.label = Label(text='connecting...\n')
        layout = BoxLayout(orientation='vertical')
        layout.add_widget(self.label)
        layout.add_widget(self.textbox)
        # return layout
    def connect_to_server(self,data):
        reactor.connectTCP(data,800, EchoClientFactory(self))
    def on_connection(self, connection):
        self.print_message("Connected")
        self.connection = connection
    def send_message(self, msg):
        if msg and self.connection:
            self.connection.write(msg.encode('utf-8'))
    def print_message(self, msg):
        self.status = "{}".format(msg)
        print("{}".format(msg))
        if self.start_looping:
            if self.status=="gagal":
                self.connect_to_server("192.168.4.1")
            if self.status=="putus":
                self.connect_to_server("192.168.4.1")

    def print_data(self, msg):
        self.data_masuk=binascii.hexlify(msg).decode()


