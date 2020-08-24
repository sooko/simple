from kivy.uix.behaviors.touchripple import  TouchRippleButtonBehavior
from kivy.lang import Builder
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.image import Image

Builder.load_string('''
<BtnModern>:
    font_name:"fonts/modern.ttf"
<BtnHemi>:
    font_name:"fonts/hemi.ttf"
''')
class BtnModern(TouchRippleButtonBehavior,Label):
    pass
class BtnHemi(TouchRippleButtonBehavior,Label):
    pass

class BtnImg(TouchRippleButtonBehavior,Image):
    pass

   

