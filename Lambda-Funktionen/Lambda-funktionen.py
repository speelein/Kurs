# kompakt und schnell

quadrat = lambda x: x*x # gibt Quadrat von x aus
print(quadrat(5))

zahlen = [1, 2, 3, 4, 5]

Quadrate = list(map(lambda x: x*x, zahlen))
print(Quadrate)

ungerade_zahlen = list(filter(lambda x: x % 2 != 0, zahlen)) # gibt ungerade Zahlen von zahlen aus , nicht Quadrate
print(ungerade_zahlen)

fruechte = ["Ananas" , "Bananenschalen" , "Apfel" , "Kirschenmarmelade"]

sortiert = sorted(fruechte, key=lambda x: len(x)) # sortiert nach Laenge
print(sortiert)