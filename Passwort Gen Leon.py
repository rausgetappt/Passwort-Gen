# -*- coding: utf-8 -*-

# Anwendung:    Passwort Generator
# Auto:         Leon Frerichs
# Datum:        23.02.2023
# Version:      1.0

import random

ascii_range = range(0, 128)  # ändere die Range auf 0 bis 127

password = [] # erstellt eine Liste für die generierten Zahlen
while len(password) < 10: # wenn die länge des Passworts kleiner als 10 ist
    char = chr(random.choice(ascii_range)) # werden neue Zahlen generiert
    if ord(char) >= 32:  # überprüfe, ob der ASCII-Wert über 32 liegt
        password.append(char) # füge die Zahlen zur Liste hinzu

password_str = "".join(password)

print(password_str) # printet das Passwort
