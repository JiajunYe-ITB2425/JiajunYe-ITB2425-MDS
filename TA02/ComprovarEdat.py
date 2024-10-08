"""
Jiajun Ye
27/09/2024
ASIXc MDS TA02
Descripció: Programa que demana l'edat i diu si ets major d'edat.
"""
from datetime import datetime

dia = int(input("Quin dia vas néixer?\n"))
while dia > 31 or dia < 1:
    dia = int(input("Torna a introduir el dia:\n"))

mes = int(input("Quin mes vas néixer?\n"))
while mes > 12 or mes < 1:
    mes = int(input("Torna a introduir el mes:\n"))

any = int(input("Quin any vas néixer?\n"))
while any > datetime.now().year:
    any = int(input("Torna a introduir el any:\n"))

if any <= datetime.now().year - 18 and mes <= datetime.now().month and dia <= datetime.now().day:
    print("Ets major d'edat")
else:
    print("Ets menor d'edat")

print("Programa Finalitzat")