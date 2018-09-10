from kivy.app import App
from kivy.uix.gridlayout import GridLayout


class CameraTester(App):
    pass


class MainScreen(GridLayout):
    def buttonOne(self):
        print("pressed button 1")


CameraTester().run()
