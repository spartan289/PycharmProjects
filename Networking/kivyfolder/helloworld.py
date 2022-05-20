from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
class LoginScreen(GridLayout):
    def __init__(self,**kwargs):
        super(LoginScreen,self).__init__(**kwargs)
        self.cols=2
        self.add_widget(Label(text='UserName'))
        self.username = TextInput(multiline=False)
        self.add_widget(self.username)
        self.add_widget(Label(text='password'))
        self.password = TextInput(password=True, multiline=False)
        self.add_widget(self.password)
        self.button = Button(text='Login')
        self.add_widget(self.button)
class MyApp(App):
    def build(self):
        return LoginScreen()
MyApp().run()