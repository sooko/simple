from kivy.support import install_twisted_reactor
install_twisted_reactor()
from binascii import hexlify
import binascii
from twisted.internet import reactor, protocol
from kivy.app import App
from kivy.uix.floatlayout import FloatLayout
from kivy.properties import StringProperty,BooleanProperty
from kivy.clock import Clock
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
        self.app.print_message("gagal")
class TwisApp(FloatLayout):
    connection = None
    textbox = StringProperty("")
    label = StringProperty("")
    status = StringProperty("")
    start_looping=BooleanProperty(False)
    def __init__(self, **kwargs):
        super(TwisApp,self).__init__(**kwargs)
    def connect_to_server(self,data):
        reactor.connectTCP(data, 800, EchoClientFactory(self))
    def on_connection(self, connection):
        self.print_message("Connected")
        self.connection = connection
    def send_message(self, msg):
        if msg and self.connection:
            self.connection.write(msg.encode('utf-8'))
    def print_message(self, msg):
        self.status = "{}".format(msg)
        print("{}".format(msg))
        if self.start_looping==True:
            if self.status=="gagal" or self.status=="putus":
                Clock.unschedule(self.delay)
                Clock.schedule_once(self.delay,1)
                
    def delay(self,dt):
        self.connect_to_server("192.168.4.1")
    def print_data(self,msg):
        pass
