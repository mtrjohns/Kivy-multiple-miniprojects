from kivy.app import App
from kivy.uix.widget import Widget
from kivy.lang import Builder
from kivy.core.window import Window
from kivy.properties import ObjectProperty

# Set the app size
Window.size = (500, 700)

# Allows designation of a specific .kv design file
Builder.load_file("calc.kv")

class MyLayout(Widget):
    def clear(self):
            self.ids.calc_input.text = "0"
            
    # Create button pressing function
    def button_press(self, button):
        # Create variable to contain current text box value
        prior = self.ids.calc_input.text
        
        # is 0 in the input
        if prior == "0":
            self.ids.calc_input.text = ""
            self.ids.calc_input.text = f"{button}"
        else:
            self.ids.calc_input.text = f"{prior}{button}"
            
    # Addition function
    def add(self):
        # Create variable to contain current text box value
        prior = self.ids.calc_input.text
        # add a plus sign to the text box
        self.ids.calc_input.text = f"{prior}+"
    
    def subtract(self):
        # Create variable to contain current text box value
        prior = self.ids.calc_input.text
        # add a plus sign to the text box
        self.ids.calc_input.text = f"{prior}-"
        
    def multiply(self):
        # Create variable to contain current text box value
        prior = self.ids.calc_input.text
        # add a plus sign to the text box
        self.ids.calc_input.text = f"{prior}*"
        
    def divide(self):
        # Create variable to contain current text box value
        prior = self.ids.calc_input.text
        # add a plus sign to the text box
        self.ids.calc_input.text = f"{prior}/"
        
    def equals(self):
        # Create variable to contain current text box value
        prior = self.ids.calc_input.text
        # add a plus sign to the text box
        #self.ids.calc_input.text = f"{prior}="
        
        # Addition
        if "+" in prior:
            # Separate into a list at each '+' sign
            num_list = prior.split("+")
            answer = 0
            
            # Loop through list
            for number in num_list:
                answer += int(number)
            
            # Print the answer in the text box
            self.ids.calc_input.text = str(answer)
            
    

class CalculatorApp(App):
    def build(self):
        return MyLayout()
    
if __name__ == '__main__':
    CalculatorApp().run()