from kivy.app import App
from kivy.uix.widget import Widget
from kivy.lang import Builder

# Allows designation of a specific .kv design file
Builder.load_file("spin.kv")

class MyLayout(Widget):
    def spinner_clicked(self, value):
        # output the value back to screen
        self.ids.click_label.text = f"You selected : {value}"

class AwesomeApp(App):
    def build(self):
        return MyLayout()
    
if __name__ == '__main__':
    AwesomeApp().run()