'''
Gegeben sei folgende Liste von Umsätzen, wobei einige Umsätze als "None" markiert sind, wo
die Umsatzdaten fehlen.
umsatz = [100, 200, None, 300, None, 400]
Verwende eine for Schleife, um die fehlenden Daten zu erkennen und zu ersetzen durch den
Durchschnitt der anliegenden Werte links und rechts vom None Wert.
'''

umsatz = [100, 200, None, 300, None, 400]

# Alternative Iteration durch die Liste umsatz
# for wert in umsatz:
#    print(wert)

for index in range(len(umsatz)): # 0, 1, 2, 3, 4, 5 --> da Länge len(umsatz) == 6
    if umsatz[index] == None:
        print(f"None-Wert an der Stelle {index} gefunden.")
        print(f"Der Wert links davon ist {umsatz[index-1]}")
        print(f"Der Wert rechts davon ist {umsatz[index+1]}")
        print(f"Der Durchschnitt ist {(umsatz[index+1] + umsatz[index-1])/2}")
        umsatz[index] = (umsatz[index+1] + umsatz[index-1])/2
        print("---")
    #print(umsatz[index])

print(umsatz)
