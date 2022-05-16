from kivy.app import App
from kivy.uix.widget import Widget
# used to use variables from the .kv design file
from kivy.properties import ObjectProperty
from kivy.lang import Builder

# Allows designation of a specific .kv design file
Builder.load_file("whatever.kv")

# OR 
'''
Builder.load_string("""
                    # paste all .kv kivy design elements here
                    # not the best practice
                    """)
'''

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


class AwesomeApp(App):
    def build(self):
        return MyGridLayout()
    
if __name__ == '__main__':
    AwesomeApp().run()