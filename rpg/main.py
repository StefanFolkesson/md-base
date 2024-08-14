spelare = "Gandalf"
spelare_liv = 100
spelare_vapen="Stav"
spelare_vapen_skada=10

fiende = "Balrog"
fiende_liv = 100
fiende_vapen="Piska"
fiende_vapen_skada=30
print("Den måktiga striden i morias grottor är påväg att starta")
print(spelare + " står på bron och " + fiende + " kommer närmare")
print(spelare + " slår med sin " +spelare_vapen +" och gör: "+ str(spelare_vapen_skada) +" skada")
fiende_liv = fiende_liv - spelare_vapen_skada
print(fiende + " har nu bara " + str(fiende_liv)+ " kvar")
