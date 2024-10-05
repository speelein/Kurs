import sys

print(sys.version)

import os

print(os.getcwd())

import json

json_string = json.dumps([1, 2, 3, "a", "b"])
print(json_string)
      
import datetime

jetzt = datetime.datetime.now()

print(jetzt)

from  datetime import datetime # aus der Funktion wurde nur speziell datetime importiert, nicht alles (speicher)

jetzt = datetime.now()

print(jetzt)