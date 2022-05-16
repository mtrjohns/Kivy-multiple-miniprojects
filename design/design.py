from turtle import textinput
import kivy
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.widget import Widget
# used to use variables from the .kv design file
from kivy.properties import ObjectProperty

class MyGridLayout(Widget):
    # Set to none as on program start values are empty
    name = ObjectProperty(None)
    pizza = ObjectProperty(None)
    color = ObjectProperty(None)


    # Pass self and the instance of a Button
    def press(self):
        name = self.name.text
        pizza = self.pizza.text
        color = self.color.text
        
        #print(f'Hello {name}, you like {pizza}, and your favourite colour is {color} !')
        # Print to the screen
        #self.add_widget(Label(text=f'Hello {name}, you like {pizza}, and your favourite colour is {color} !'))
        print(f'Hello {name}, you like {pizza}, and your favourite colour is {color} !')
        
        # Clear input boxes
        self.name.text = ""
        self.pizza.text = ""
        self.color.text = ""


class MyApp(App):
    def build(self):
        return MyGridLayout()
    
if __name__ == '__main__':
    MyApp().run()