from kivy.lang import Builder
from kivy.properties import StringProperty, BooleanProperty
from kivy.uix.gridlayout import GridLayout

Builder.load_file("widget_exemples.kv")


class WidgetsExemple(GridLayout):
    compteur_actif = BooleanProperty(False)
    mon_texte = StringProperty("1")
    compteur=1
    #slider_value_txt = StringProperty("1")
    text_input_str = StringProperty("toto")
    def on_button_click(self):
        print("Compteur")
        if self.compteur_actif:
            self.compteur +=1
            self.mon_texte= str(self.compteur)

    def on_toggle_button_state(self,widget):
        #print("toggle state :" + widget.state)
        if widget.state =="normal":
            print("OF")
            widget.text = "OFF"
            self.compteur_actif = False
        else:
            print("ON")
            widget.text = "ON"
            self.compteur_actif = True

    def on_switch_active(self, widget):
        print("switch :" + str(widget.active))

    def on_slider_value(self, widget):
        print("slider:"+str(int(widget.value)))
        #self.slider_value_txt = str(int(widget.value))

    def on_text_validate(self, widget):
        self.text_input_str = widget.text


