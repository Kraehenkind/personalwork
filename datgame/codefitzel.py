
# Alter Programmteil. Erstellen der Menübuttons, etc.
"""
        newGame = Button(text = "New Game", padding = 10, background_color = "blue")
        leaveGame = Button(text = "Leave Game", padding = 10, background_color = "blue")
        closeMenue = Button(text = "Close menue", padding = 10, background_color = "blue")
        menueContent.add_widget(Label())
        menueContent.add_widget(newGame)
        menueContent.add_widget(closeMenue)
        menueContent.add_widget(Label())
        menueContent.add_widget(leaveGame)
        popup = Popup(title = "Menue", size_hint = (.5, .5), content = menueContent, auto_dismiss = False)
        closeMenue.bind(on_press = popup.dismiss)
        newGame.bind(on_press = instance.parent.reset)
        leaveGame.bind(on_press = instance.parent.leaveGame)
"""

