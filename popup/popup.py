from kivy.app import App
from kivy.uix.widget import Widget
from kivy.lang import Builder

# Allows designation of a specific .kv design file
Builder.load_file("popup.kv")

class MyLayout(Widget):
    pass

class AwesomeApp(App):
    def build(self):
        return MyLayout()
    
if __name__ == '__main__':
    AwesomeApp().run()