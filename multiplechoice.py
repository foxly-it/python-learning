import json
import os

fragen = [
    {
        "frage": "Was ist 5 + 3?",
        "auswahl": ["6", "7", "8", "9"],
        "korrekt": 3
    },
    {
        "frage": "Was ist 10 * 2?",
        "auswahl": ["20", "25", "30", "15"],
        "korrekt": 1
    },
    {
        "frage": "Was ist 9 / 3?",
        "auswahl": ["2", "3", "4", "5"],
        "korrekt": 2
    },
    {
        "frage": "Was ist 6 - 4?",
        "auswahl": ["1", "2", "3", "0"],
        "korrekt": 2
    },
    {
        "frage": "Was ist 12 + 8?",
        "auswahl": ["18", "19", "20", "21"],
        "korrekt": 3
    }
]

highscore_datei = "highscore.json"

def lade_highscore():
    if os.path.exists(highscore_datei):
        with open(highscore_datei, 'r') as datei:
            return json.load(datei)
    return {"name": "", "score": 0}

def speichere_highscore(name, score):
    highscore = {"name": name, "score": score}
    with open(highscore_datei, 'w') as datei:
        json.dump(highscore, datei)

def starte_quiz():
    punkte = 0

    aktueller_highscore = lade_highscore()
    print(f"\nAktueller Highscore: {aktueller_highscore['score']} Punkte von {aktueller_highscore['name']}")

    print("Willkommen beim Mathe-Multiple-Choice-Test!")
    for i, frage in enumerate(fragen, 1):
        print(f"\nFrage {i}: {frage['frage']}")
        for j, antwort in enumerate(frage['auswahl'], 1):
            print(f"{j}: {antwort}")

        while True:
            try:
                eingabe = int(input("Wähle die richtige Antwort (1-4): "))
                if 1 <= eingabe <= 4:
                    break
                else:
                    print("Ungültige Eingabe. Bitte eine Zahl zwischen 1 und 4 eingeben.")
            except ValueError:
                print("Ungültige Eingabe. Bitte eine Zahl eingeben.")

        if eingabe == frage["korrekt"]:
            print("Richtig!")
            punkte += 100
        else:
            print("Falsch!")

    print(f"\nDu hast {punkte} Punkte erreicht.")

    if punkte > aktueller_highscore["score"]:
        print("Glückwunsch! Du hast den neuen Highscore erreicht!")
        name = input("Bitte gib deinen Namen ein: ")
        speichere_highscore(name, punkte)
    else:
        print(f"Der aktuelle Highscore bleibt: {aktueller_highscore['score']} Punkte von {aktueller_highscore['name']}.")

    # Highscore am Ende anzeigen
    print(f"\nEndgültiger Highscore: {aktueller_highscore['score']} Punkte von {aktueller_highscore['name']}")

if __name__ == "__main__":
    starte_quiz()
