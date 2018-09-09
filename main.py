from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.properties import ObjectProperty


class ThetaTesterApp(App):
    # def build(self):
    #     greeting = "hello, world"
    #     return Button(text=greeting)
    pass


class FirstScreen(GridLayout):

    input_box = ObjectProperty

    def printIt(self):
        output_string = "the 1st button was pressed"
        print(output_string)
        self.button_output.text = output_string

    def secondButton(self):
        print("the 2nd button was pressed")
        print(self.button_output.text)
        self.button_output.text = (
            "Button 2 pressed. " +
            "Input box contains: " + self.input.text)
        print(self.input.text)


if __name__ == '__main__':
    ThetaTesterApp().run()
