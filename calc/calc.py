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
        
    # Create function to remove last charatcer
    def remove(self):
        prior = self.ids.calc_input.text
        # grab the last value and remove
        prior = prior[:-1]
        # output back to the text box
        self.ids.calc_input.text = prior
        
    # Create function to convert positive or negative
    def pos_neg(self):
        prior = self.ids.calc_input.text
        # Test to see if there is a subtract sign
        if "-" in prior:
            # Replace '-' with nothing
            self.ids.calc_input.text = f'{prior.replace("-", "")}'
        else:
            self.ids.calc_input.text = f"-{prior}"
        
    # Create a decimal function    
    def dot(self):
        prior = self.ids.calc_input.text
        
        num_list = prior.split("+")

        # If there is a '+' and the last input is not a '.'
        if "+" in prior and "." not in num_list[-1]:
            # Add a decimal to the end of the text
            prior = f"{prior}."
            # output back to the text box
            self.ids.calc_input.text = prior
        elif "." in prior:
            pass
        else:
            # Add a decimal to the end of the text
            prior = f"{prior}."
            # output back to the text box
            self.ids.calc_input.text = prior
            
    # Addition function
    def math_sign(self, sign):
        # Create variable to contain current text box value
        prior = self.ids.calc_input.text
        if prior[-1] != "+":
            # add a plus sign to the text box
            self.ids.calc_input.text = f"{prior}{sign}"

    def equals(self):
        # Create variable to contain current text box value
        prior = self.ids.calc_input.text
        # add a plus sign to the text box
        #self.ids.calc_input.text = f"{prior}="
        
        # Addition
        if "+" in prior:
            # Separate into a list at each '+' sign
            num_list = prior.split("+")
            answer = 0.0
            
            # Loop through list
            for number in num_list:
                answer += float(number)
            
            # Print the answer in the text box
            self.ids.calc_input.text = str(answer)
            
    

class CalculatorApp(App):
    def build(self):
        return MyLayout()
    
if __name__ == '__main__':
    CalculatorApp().run()