from turtle import textinput
import kivy
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput#
from kivy.uix.button import Button

class MyGridLayout(GridLayout):
    # Initialise infinite keywords
    def __init__(self, **kwargs):
        # Call grid layout constructor
        super(MyGridLayout, self).__init__(**kwargs)
        
        # Columns
        self.cols = 2
        
        # Add widgets
        self.add_widget(Label(text="Name: "))
        #add input box
        self.name = TextInput(multiline=False)
        self.add_widget(self.name)

        self.add_widget(Label(text="Favourite Pizza: "))
        self.pizza = TextInput(multiline=False)
        self.add_widget(self.pizza)

        self.add_widget(Label(text="Favourite Colour: "))
        self.color = TextInput(multiline=False)
        self.add_widget(self.color)
        
        # Create a submit button
        self.submit = Button(text="Submit", font_size=32)
        # Bind the button
        self.submit.bind(on_press=self.press)
        self.add_widget(self.submit)
        
    # Pass self and the instance of a Button
    def press(self, instance):
        name = self.name.text
        pizza = self.pizza.text
        color = self.color.text
        
        #print(f'Hello {name}, you like {pizza}, and your favourite colour is {color} !')
        # Print to the screen
        self.add_widget(Label(text=f'Hello {name}, you like {pizza}, and your favourite colour is {color} !'))
        
        # Clear input boxes
        self.name.text = ""
        self.pizza.text = ""
        self.color.text = ""


class MyApp(App):
    def build(self):
        return MyGridLayout()
    
if __name__ == '__main__':
    MyApp().run()