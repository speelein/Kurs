meine_liste = ['a', 'b', 'c','d', 'e', [1, 2, 3]] # Liste in Liste

print(meine_liste[0])
print(meine_liste[3])
print(meine_liste[5])
print(meine_liste[-1])
print(meine_liste[-6])

# Slicing auch fuer Tuple
teil_liste = meine_liste[1:4:2] # Startpunk:Endpunkt:Schrittgroesse
print(teil_liste)


teil_liste1 = meine_liste[1:4:] # Schrittgroesse 0
print(teil_liste1)

teil_liste2 = meine_liste[::] # alles print
print(teil_liste2)

# append ( nicht Tuple)

meine_liste3 = meine_liste
meine_liste3.append('f')
print(meine_liste3)

meine_liste3.insert(1,'x')
print(meine_liste3)

meine_liste3.remove('b')
print(meine_liste3)

# viele weitere Methoden moeglich zB. extend reverse sort

meine_liste3.sort() # achtung !!!!!! geht nur einheitlich
print(meine_liste3)