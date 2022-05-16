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
        self.cols = 1
        self.row_force_default=True
        self.row_default_height=120
        self.col_force_default=True
        self.col_default_width=100
        
        # Create second gridlayout
        self.top_grid = GridLayout(
            row_force_default=True,
            row_default_height=40,
            col_force_default=True,
            col_default_width=100
            )
        self.top_grid.cols = 2
        
        # Add widgets
        self.top_grid.add_widget(Label(text="Name: "))
        #add input box
        self.name = TextInput(multiline=True)
        self.top_grid.add_widget(self.name)

        self.top_grid.add_widget(Label(text="Favourite Pizza: "))
        self.pizza = TextInput(multiline=False)
        self.top_grid.add_widget(self.pizza)

        self.top_grid.add_widget(Label(text="Favourite Colour: "))
        self.color = TextInput(multiline=False)
        self.top_grid.add_widget(self.color)
        
        # Add new top_grid to the app
        self.add_widget(self.top_grid)
        
        
        # Create a submit button
        self.submit = Button(text="Submit",
                             font_size=32,
                             size_hint_y=None, # Need this to adjust height
                             height=50,
                             size_hint_x=None,
                             width=200)
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