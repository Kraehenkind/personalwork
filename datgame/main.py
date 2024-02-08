from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button
from kivy.uix.popup import Popup
import csv
import random

class MainMenue(Popup):
    pass

class InputButtons(GridLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.rows = 3
        self.usedChars = []
        self.app = App.get_running_app()
        
        for i in range(0,26):
            charButton = Button(text = chr(65+i), bold = True, padding = 5)
            charButton.bind(on_press = self.charUsed)
            self.add_widget(charButton)
        getout = Button(text = "Menü")
        getout.bind(on_press = self.callMenue)
        self.add_widget(getout)
    
    def charUsed(self, instance):
        if instance.text.lower() not in self.usedChars:
            self.usedChars.append(instance.text.lower())
            if self.app.root.up.textfield.gameRound(instance.text):
                instance.background_color = "red"

    def callMenue(self, instance):
        self.app.root.menuePopUp(instance)

    def reset(self):
        self.usedChars = []
        for i in range(len(self.children)):
            self.children[i].background_color = [1,1,1,1]
        

class RiddleDisplay(Label):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.wordlist = []

        with open(r"Coding_practices/datgame/dictionary.csv",
                   encoding="utf-8") as file:
            csv_file = csv.reader(file)
    
            for line in list(csv_file):
                self.wordlist.append(line[0])
        
        self.riddle = random.choice(self.wordlist).lower()
        self.guesses = ["_"]*len(self.riddle)
        self.text = f"{'  '.join(self.guesses)}"
        self.wrongAnswers = 0

    def checkChar(self, char):
        if char.lower() in self.riddle.lower():
            for i in range(len(self.riddle)):
                if self.riddle[i].lower() == char.lower():
                    self.guesses[i] = char.upper()
                    self.text = f"{'  '.join(self.guesses)}"
            return True    
        self.wrongAnswers += 1
        return False

    def gameRound(self, char):
        if self.wrongAnswers < 10 and self.text != f"GEWONNEN\n\nDie Lösung war:\n\n{self.riddle.upper()}":
            if self.checkChar(char) and self.riddle.lower() == "".join(self.guesses).lower():
                self.text = f"GEWONNEN\n\nDie Lösung war:\n\n{self.riddle.upper()}"
            if self.wrongAnswers == 10:
                self.text = f"Leider verloren,\n\ndie richtige Lösung war:\n\n{self.riddle.upper()}"
            return True
        return False
    
    def newGame(self):
        self.riddle = random.choice(self.wordlist).lower()
        self.guesses = ["_"]*len(self.riddle)
        self.text = f"{'  '.join(self.guesses)}"
        self.wrongAnswers = 0


class HangMan(Label):

    def resetPicture(self):
        pass

class UpperHalf(GridLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.cols = 2
        self.textfield = RiddleDisplay()
        self.picturefield = HangMan()
        self.add_widget(self.textfield)
        self.add_widget(self.picturefield)

    def resetGame(self):
        self.textfield.newGame()
        self.picturefield.resetPicture()

class GameScreen(GridLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.rows = 2
        self.menue = MainMenue()
        self.up = UpperHalf(size_hint = (1,.75))
        self.down = InputButtons(size_hint = (1,.25))
        self.add_widget(self.up)
        self.add_widget(self.down)

    def startNewGame(self):
        self.up.resetGame()
        self.down.reset()
        self.menue.dismiss()

    def menuePopUp(self,instance):
        self.menue.open()

class GameApp(App):
    def build(self):
        return GameScreen() 
  
if __name__ == "__main__":
    GameApp().run()