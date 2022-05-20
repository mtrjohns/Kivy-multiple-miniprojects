from kivy.app import App
from kivy.lang import Builder
from kivy.uix.widget import Widget

# Allows designation of a specific .kv design file
Builder.load_file("button_image.kv")

class MyLayout(Widget):
    def hello_on(self):
        self.ids.my_image.source = "login_pressed.png"
         
    def hello_off(self):
        self.ids.my_label.text = "You pressed a button"
        self.ids.my_image.source = "login.png"

class AwesomeApp(App):
    def build(self):
        return MyLayout()
    
if __name__ == '__main__':
    AwesomeApp().run()