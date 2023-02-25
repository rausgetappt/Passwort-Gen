# Anwendung:        Passwort Generator
# Autor:            Roj Nico Lange
# Datum:            24.02.2023
# Version:          1.o


import random

Länge = 10 # Länge des Passworts definieren
Passwort = [] # Liste für Zeichen des Passworts erstellen

# Solange die Länge unter 10 ist:
while len(Passwort) < Länge:
    # Zufällige Zahl zwischen 0 und 127 generieren
    Zufallszahl = random.randint(0, 127)

    # Zufallszahl dem entsprechenden ASCII-Zeichen zuordnen
    Zeichen = chr(Zufallszahl)

    # Falls ein ASCII-Zeichen unter 32 generiert wurde...
    if ord(Zeichen) < 32:
        # ...die Passwort-Liste zurücksetzen und eine neue generieren.
        Passwort = []
    else: #Falls kein ASCII-Zeichen unter 32 generiert wurde...
        Passwort.append(Zeichen) # ...das Zeichen der Passwort-Liste hinzufügen       

# Wandelt die Passwort-Liste in einen String ohne Abstände um
Passwort_string = ''.join(Passwort)

# Ausgabe des Passworts
print(Passwort_string)