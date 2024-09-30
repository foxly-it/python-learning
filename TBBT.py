import random

# Hauptfunktion des Spiels
def spiel():
    # Liste der möglichen Optionen
    optionen = ["Stein", "Schere", "Papier", "Echse", "Spock"]
    
    # Punkte für den Benutzer und den Computer
    punkte_benutzer = 0
    punkte_computer = 0

    # Regeln für das Spiel, jede Option schlägt bestimmte andere Optionen
    regeln = {
        "Schere": ["Papier", "Echse"],
        "Papier": ["Stein", "Spock"],
        "Stein": ["Echse", "Schere"],
        "Echse": ["Spock", "Papier"],
        "Spock": ["Schere", "Stein"]
    }

    # Begrüßung des Spielers
    print("Willkommen zu Stein, Schere, Papier, Echse, Spock! (Best of 3)")

    # Spiel läuft über 3 Runden
    for runde in range(1, 4):
        print(f"\nRunde {runde}:")
        print("Wähle eine Option:")
        
        # Zeige die Liste der verfügbaren Optionen
        for i, option in enumerate(optionen, 1):
            print(f"{i}: {option}")

        # Hole die Wahl des Benutzers und überprüfe die Eingabe
        while True:
            benutzerwahl = input("Gib die Nummer deiner Wahl ein (1-5): ")
            if benutzerwahl in ['1', '2', '3', '4', '5']:
                # Umwandlung der Benutzereingabe in die entsprechende Option
                benutzerwahl = optionen[int(benutzerwahl) - 1]
                break
            else:
                # Wiederhole die Eingabe, wenn sie ungültig ist
                print("Ungültige Eingabe. Bitte wähle eine Zahl zwischen 1 und 5.")

        # Der Computer wählt zufällig eine Option
        computerwahl = random.choice(optionen)
        print(f"\nDu hast gewählt: {benutzerwahl}")
        print(f"Der Computer hat gewählt: {computerwahl}")

        # Prüfe auf Unentschieden
        if benutzerwahl == computerwahl:
            print("Unentschieden!")
        # Prüfe, ob der Benutzer gewinnt
        elif computerwahl in regeln[benutzerwahl]:
            print(f"Du hast gewonnen! {benutzerwahl} schlägt {computerwahl}.")
            punkte_benutzer += 1
        # Wenn der Benutzer nicht gewinnt und es kein Unentschieden ist, gewinnt der Computer
        else:
            print(f"Der Computer hat gewonnen! {computerwahl} schlägt {benutzerwahl}.")
            punkte_computer += 1

    # Zeige die Endergebnisse nach 3 Runden
    print("\nErgebnisse:")
    print(f"Du hast {punkte_benutzer} Runden gewonnen.")
    print(f"Der Computer hat {punkte_computer} Runden gewonnen.")

    # Bestimme den Gesamtsieger und gib das Ergebnis aus
    if punkte_benutzer > punkte_computer:
        print("Herzlichen Glückwunsch! Du hast das Spiel gewonnen!")
    elif punkte_benutzer < punkte_computer:
        print("Der Computer hat das Spiel gewonnen!")
    else:
        print("Das Spiel endet Unentschieden!")

# Starte das Spiel, wenn das Skript ausgeführt wird
if __name__ == "__main__":
    spiel()
