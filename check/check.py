from kivy.app import App
from kivy.uix.widget import Widget
from kivy.lang import Builder

# Allows designation of a specific .kv design file
Builder.load_file("check.kv")

class MyLayout(Widget):
    
    checks = []
    
    # pass instance, the instance of the checkbox, value is a bool
    def checkbox_click(self, instance, value, topping):
        if value == True:
            MyLayout.checks.append(topping)
            tops = ""
            for x in MyLayout.checks:
                tops =f"{tops} {x}"
            self.ids.output_label.text = f"You selected: {tops}"
        else:
            MyLayout.checks.remove(topping)
            tops = ""
            for x in MyLayout.checks:
                tops = f"{tops} {x}"
            self.ids.output_label.text = f"You selected: {tops}"

class AwesomeApp(App):
    def build(self):
        return MyLayout()
    
if __name__ == '__main__':
    AwesomeApp().run()