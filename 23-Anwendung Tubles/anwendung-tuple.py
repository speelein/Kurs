# unveraenderliche Datensaetze

konfiguration = (1920, 1080, 60) # Bildschirm

# Rueckgabewerte von Funktion

def berechen_statistiken(zahlen):
    mittelwert = sum(zahlen) / len(zahlen)
    varianz = sum((x - mittelwert)**2 for x in zahlen / len(zahlen))
    standardabweichung = varianz ** 0.5
    return mittelwert, standardabweichung

statistiken = berechen_statistiken([1, 2, 3, 4, 5])

print(statistiken)

for  (x, y) in [(1, 2), (3, 4), (5, 6)]:
    print(x, y)

farben = {(255, 0, 0): "Rot" , (0, 255, 0): "Gruen" , (0, 0, 255): "Blau"}
print(farben[(0, 0, 255)])

def position_berechnen(x, y, z):
    return(x**2 + y**2 + z**2) **0.5

position = (100, 200, 300)
entfernung = position_berechnen(*position) # * Weitergabe Tuble
print("Die Entfernung vom Ursprung ist:", entfernung)