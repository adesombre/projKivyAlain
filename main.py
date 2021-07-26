from kivy.app import App
from kivy.properties import ObjectProperty
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.widget import Widget
# from layout import *
# from widget import *
# from navigation_screen_manager import *
from canvas_exemples import *
from navigation_screen_manager import NavigationScreenManager


class MenuPrincipal(BoxLayout):
    pass


class MyScreenManager(NavigationScreenManager):
    pass





class  LelabApp(App):
    manager = ObjectProperty(None)
    def build(self):
        self.manager = MyScreenManager()
        return self.manager
        #return CanvasExemple7()




LelabApp().run()
