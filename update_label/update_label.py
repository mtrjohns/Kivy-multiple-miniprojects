from kivy.app import App
from kivy.uix.widget import Widget
from kivy.lang import Builder
from kivy.core.window import Window

# Allows designation of a specific .kv design file
Builder.load_file("update_label.kv")

class MyLayout(Widget):
    def press(self):
        # Create variables for our widgets
        name = self.ids.name_input.text

        #Update the label
        self.ids.name_label.text = f"Hello {name}!"
        
        # Clear the input box
        self.ids.name_input.text = ""

class AwesomeApp(App):
    def build(self):
        # background colour of default window
        #Window.clearcolor = (1, 1, 1, 1)
        return MyLayout()
    
if __name__ == '__main__':
    AwesomeApp().run()