******************************
Linking Kivy Widgets to Events
******************************

In Python file:

    class MainScreen(GridLayout):
        def buttonOne(self):
            print("pressed button 1")
::

In kv file

    BoxLayout:
        orientation: "horizontal"
        Button:
            text: "Button 1"
            on_press: root.buttonOne()
::