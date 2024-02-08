import os

banner = "Willkommen bei ihrer  Money-Bank" 

def header(menue):
    fenster = os.get_terminal_size()
    padding = (fenster.columns) //2 -len(banner)
    os.system("cls")
    print(" "*padding,"_"*len(banner)+" "*padding)
    print(" "*padding+"|"+" "*len(banner)+"|"+" "*padding)
    print(" "*padding+"|"+banner+"|"+" "*padding)
    print(" "*padding+"|"+"_"*len(banner)+"|"+" "*padding+"\n")
    print("Sie sind hier:")
    print("              Consolebanking-",menue)
    print("_"*fenster.columns+"\n")
    print("Ihr imaginärer Kontostand beträgt:", kontostand,"€")
    
kontostand = 100
pin = "0815"

while True:
    head="Kontoübersicht"
    header(head)
    print("Navigationsmenü:")
    print("[1] >>> Einzahlung")
    print("[2] >>> Überweisung/Abhebung")
    print("[Q] >>> Log-out")
    ziel = input(">>>")


#Menü zur Einzahlung

    if ziel == "1":                                                 
        head = "Einzahlung"
        header(head)
        print("\nWelchen Betrag möchten Sie einzahlen?") 
        print("Abbruch mit [Q]")
        betrag= input(">>>")

        if betrag.isdecimal() and int(betrag) > 0:                  #Alles gut... User hat mehr Geld
            print("Ihr Kontostand wird um",betrag,"erhöht")
            kontostand= kontostand+int(betrag)
            input("Bitte [Enter] drücken...")
        elif betrag.isdecimal() and int(betrag) == 0:               #User hat 0 nicht verstanden
            print("Vielen Dank für diese Eingabe")
            input("Bitte [Enter] drücken...")
        elif betrag == "Q" or betrag == "q":                        #User will doch lieber gehen
            pass
        else:                                                        #User hat Probleme mir der Aufgabe   
            print("\nLeider ist Ihre Eingabe nicht eindeutig.\nSie kehren zur Kontoübersicht zurück\n")
            input("Bitte [Enter] drücken...")
            
        
#Menü zum Abheben/Überweisen

    elif ziel == "2":                                                   
        head= "Überweisung/Abhebung"
        while True:
            header(head)
            print("Navigationsmenü:")
            print("[1] >>> Betrag direkt abheben.")
            print("[2] >>> Überweisung vornehmen")
            print("[Q] >>> Zurück zur Kontoübersicht")
            ziel2 = input(">>>")

            if ziel2.isdecimal() and ziel2 == "1":                      #Einen Betrag Abheben
                header(head)
                print("\nWelchen Betrag möchten sie abheben?")
                abhebung = input("Gewünschter Betrag: ")

                if abhebung.isdecimal() and int(abhebung) <= kontostand:            #User hat genug Geld
                    header(head)
                    print("Für diese Transaktion ist ihre persönliche PIN notwendig!\n")
                    versuche = 3
                    while versuche > 0:                                             #PIN Abfrage für Auszahlung
                        pinEingabe = input("Bitte PIN eingeben: ")
                        if pinEingabe == pin:                                       #Richtige Pin erhalten
                            print("Ihr Kontostand wird um",abhebung,"reduziert")
                            input("Bitte [Enter] drücken...")
                            kontostand = kontostand-int(abhebung)
                            break
                        elif versuche > 0:                                          #PIN Falsch neuer Versuch
                            header("Überweisung/Abhebung")
                            print("Für diese Transaktion ist ihre persönliche PIN notwendig!\n")
                            versuche -= 1
                            print("Da ist ihnen leider ein Fehler unterlaufen. Versuchen sie es bitte nochmals")
                            print("Verbleibende Versuche:",versuche)
                            
                        else:                                                       #Alle Versuche aufgebraucht
                            break
                    header(head)                                                                   #User wählt Überweisung oder Hauptmenü
                    print("Geben Sie [1] ein, wenn Sie eine weitere Überweisung/Abhebung machen möchten")
                    print("Andere Eingaben bringen Sie zurück zur Kontoübersicht.")
                    check = input(">>>")
                    if check == "1":
                        pass
                    else:            
                        break   
                elif abhebung.isdecimal() and int(abhebung) > kontostand:           #User ist zu gierig--->>> Rückkehr ins Menü Überweisung
                    header(head)
                    print("Für diese Transaktion fehlen Ihnen die finanziellen Mittel")                                                                   
                    print("Geben Sie [1] ein, wenn Sie eine weitere Überweisung/Abhebung machen möchten")           #User wählt Überweisung oder Hauptmenü
                    print("Andere Eingaben bringen Sie zurück zur Kontoübersicht.")
                    check = input(">>>")
                    if check == "1":
                        pass
                    else:            
                        break
                    

            elif ziel2.isdecimal() and ziel2 == "2":                    #Eine Überweisung
                header(head)
                print("\nBitte geben Sie den Empfänger an:")
                empfang= input("Name ihres imaginären Freundes:")
                abhebung = input("Welcher Betrag soll überwiesen werden:")

                if abhebung.isdecimal() and int(abhebung) <= kontostand:                        #PIN abfrage für Überweisung
                    header(head)
                    print("Für diese Transaktion ist ihre persönliche PIN notwendig!\n")
                    versuche = 3
                    while versuche > 0:                                                         #Schleife für mehrere Versuche
                        pinEingabe = input("Bitte PIN eingeben: ")
                        if pinEingabe == pin:                                                   #User hat es geschafft
                            header(head)
                            print(empfang,"wird eine Zahlung von",abhebung,"€ erhalten")
                            kontostand = kontostand-int(abhebung)
                            input("Bitte [Enter] drücken...")
                            break
                            
                        elif versuche > 0:                                                       #Neuer Versuch
                            versuche -= 1
                            header(head)
                            print("Für diese Transaktion ist ihre persönliche PIN notwendig!\n")
                            print("Da ist ihnen leider ein Fehler unterlaufen. Versuchen sie es bitte nochmals")
                            print("Verbleibende Versuche:",versuche)

                        else:                                                                     #Alle versuche aufgebraucht 
                            break
                    header(head)                                                                   #User wählt Überweisung oder Hauptmenü
                    print("Geben Sie [1] ein, wenn Sie eine weitere Überweisung/Abhebung machen möchten")
                    print("Andere Eingaben bringen Sie zurück zur Kontoübersicht.")
                    check = input(">>>")
                    if check == "1":
                        pass
                    else:            
                        break

                elif abhebung.isdecimal() and int(abhebung) > kontostand:                       #User ist zu gierig--->>> Rückkehr ins Menü Überweisung
                    header(head)
                    print("Für diese Transaktion fehlen Ihnen die finanziellen Mittel")
                    input("Bitte [Enter] drücken...")
                
                else:                                                                           #User hat Probleme mir der Aufgabe...
                    header(head)
                    print("\nLeider ist Ihre Eingabe nicht eindeutig, bitte versuchen Sie es noch einmal")
                    input("Bitte [Enter] drücken...")
            
            elif ziel2 == "q" or ziel2 == "Q":                          #Zurück zur Kontoübersicht
                break

#Das Programm beenden            
    elif ziel == "q" or ziel == "Q":                                    
        header("Logout")
        print("\nVielen Dank für ihr Geld!")
        print("Noch einen schönen Tag!")
        exit()

#User hat Probleme mit der Aufgabe
    else:                                                               
        header(head)
        print("\nLeider ist Ihre Eingabe nicht eindeutig, bitte versuchen Sie es noch einmal")
        input("Bitte [Enter] drücken...")