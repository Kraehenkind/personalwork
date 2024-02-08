from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button
from kivy.uix.screenmanager import ScreenManager, Screen

installedGames = {
    "Test1": "second",
    "Test2": "Game",
    "test3": "And",
    "test4": "another",
    "test5": "one"
    }

class SpecialButton(Button):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def callback(self,instance):
        print(self.text)
        self.parent.parent.parent.current = self.text

class MenueGrid(GridLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.cols = 2
                
        for game in installedGames.keys():
            addIt = SpecialButton(text=installedGames[game])
            addIt.bind(on_press= addIt.callback)
            self.add_widget(addIt)

class MenueScreen(Screen):
    pass

class SecondTestScreen(Screen):
    pass

class WindowManager(ScreenManager):
    pass
   
class Game(BoxLayout):
    pass

class GamesProjectApp(App):
    def build(self):
        sm = WindowManager()
        return sm

if __name__ == "__main__":
    GamesProjectApp().run()