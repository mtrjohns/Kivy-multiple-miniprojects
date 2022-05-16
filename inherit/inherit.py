from kivy.app import App
from kivy.uix.widget import Widget
# used to use variables from the .kv design file
from kivy.properties import ObjectProperty
from kivy.lang import Builder

# Allows designation of a specific .kv design file
Builder.load_file("inherit.kv")

class MyLayout(Widget):
    pass


class AwesomeApp(App):
    def build(self):
        return MyLayout()
    
if __name__ == '__main__':
    AwesomeApp().run()