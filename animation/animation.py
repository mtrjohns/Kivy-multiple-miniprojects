from kivy.app import App
from kivy.uix.widget import Widget
from kivy.lang import Builder
from kivy.animation import Animation

# Allows designation of a specific .kv design file
Builder.load_file("animation.kv")

class MyLayout(Widget):

    # Animation definition
    def animate_it(self, widget, *args):
        animate = Animation(
            # animate the button press
            background_color = (0, 0, 1, 1),
            duration = 0.2)

        # do second animation
        animate += Animation(
            size_hint = (1, 1))

        # do third animation
        animate += Animation(
            size_hint = (0.5, 0.5))

        # do fourth animation
        animate += Animation(
            pos_hint = {"center_x":0.1})

            # do fourth animation
        animate += Animation(
            pos_hint = {"center_x":0.5})

        # Start the animation (pass what to animate)
        animate.start(widget)

        # Create a callback function to animate
        animate.bind(on_complete = self.my_callback)

    def my_callback(self, *args):
        self.ids.my_label.text = "Wow! Look at that animation!"

class AwesomeApp(App):
    def build(self):
        return MyLayout()
    
if __name__ == '__main__':
    AwesomeApp().run()