planeten = ["merkur", "venus", "erde", "mars", "jupiter", "saturn", "uranus", "neptun"]
genannte_planeten = set()

print("Nenne alle 8 Planeten in unserem Sonnensystem!")

while len(genannte_planeten) < 8:
    eingabe = input("Nenne einen Planeten: ").strip().lower()

    if eingabe in planeten and eingabe not in genannte_planeten:
        print("Das ist richtig!")
        genannte_planeten.add(eingabe)
    elif eingabe in genannte_planeten:
        print("Diesen Planeten hast du bereits genannt.")
    else:
        print("Das ist falsch. Versuch es nochmal!")

if len(genannte_planeten) == 8:
    print("Herzlichen Glückwunsch! Du hast alle Planeten richtig genannt.")
else:
    fehlende_planeten = set(planeten) - genannte_planeten
    print(f"Du hast {len(genannte_planeten)} Planeten korrekt genannt.")
    print(f"Es fehlen noch: {', '.join(fehlende_planeten)}.")
