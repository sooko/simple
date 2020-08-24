from kivy.uix.behaviors.touchripple import  TouchRippleButtonBehavior
from kivy.lang import Builder
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.image import Image

Builder.load_string('''
<BtnModern>:
    font_name:"fonts/modern.ttf"
<LabelModern>:
    font_name:"fonts/modern.ttf"

<BtnHemi>:
    font_name:"fonts/hemi.ttf"
<BtnMono>:
    font_name:"fonts/Monoid-Retina.ttf"
<LabelMonoid>:
    font_name:"fonts/Monoid-Retina.ttf"
<LabelHemi>:
    font_name:"fonts/hemi.ttf"
<LabelLcd>:
    font_name:"fonts/lcd_b.ttf"
<LabelConsola>:
    font_name:"fonts/consola.ttf"
<LabelCavian>:
    font_name:"fonts/cavian.ttf"
<BtnCavian>:
    font_name:"fonts/cavian.ttf"

    

''')
class BtnModern(TouchRippleButtonBehavior,Label):
    pass
class BtnHemi(TouchRippleButtonBehavior,Label):
    pass
class BtnMono(TouchRippleButtonBehavior,Label):
    pass
class BtnCavian(TouchRippleButtonBehavior,Label):
    pass

class BtnImg(TouchRippleButtonBehavior,Image):
    pass


class LabelHemi(Label):
    pass
class LabelModern(Label):
    pass

class LabelMonoid(Label):
    pass
class LabelLcd(Label):
    pass

class LabelCavian(Label):
    pass

class LabelConsola(Label):
    pass



   

