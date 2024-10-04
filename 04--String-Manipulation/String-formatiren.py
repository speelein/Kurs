from cgitb import text


name = 'Lara'
alter = 15

tete = "Mein Name ist {} und ich bin {} Jahre alt!".format(name,alter)
print(tete)
tete2 = f"Mein Name ist {name} und ich bin {alter} Jahre alt." # ab Python 3.6 f-String
print(tete2)