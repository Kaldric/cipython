import statistics
numerot = input("Anna numeroita! \n")
numerot = numerot.split(",")
maara = len(numerot)
numerot = list(map(int, numerot))

summa = 0
maksimi = 0
minimi = min(numerot)
mediaani = statistics.median(numerot)

for numero in numerot:
	summa += numero
	if numero > maksimi:
		maksimi = numero
	if numero < minimi:
	 	minimi = numero

keskiarvo = summa / maara
keskiarvo = round(keskiarvo,2)
moodi = statistics.mode(numerot)
mediaani = round(mediaani,2)

print("Pienin " + str(minimi) + "\n" + "Suurin " + str(maksimi) + "\n" + "Keskiarvo " + str(keskiarvo) + "\n" + "Mediaani " + str(mediaani) + "\n" + "Moodi " + str(moodi) )