from kivy.app import App
from kivy.lang import Builder
from kivy.uix.tabbedpanel import TabbedPanel

# Allows designation of a specific .kv design file
Builder.load_file("tabs.kv")

class MyLayout(TabbedPanel):
    pass

class AwesomeApp(App):
    def build(self):
        return MyLayout()
    
if __name__ == '__main__':
    AwesomeApp().run()