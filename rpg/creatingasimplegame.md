# Creating a Simple Game

För att skapa ett enkelt spel måste vi först ha några karaktärer.
Varför inte börja med Den episka striden i Morias grottor mellan Gandalf och Balrogen. 

Vi måste lagra våra karaktärers namn.

```python
spelare = "Gandalf"
fiende = "Balrog"
```
Till vänster om likamedtecknet har vi något vi kallar en variabel. Denna variabel innehåller det som är till höger om likamedtecknet.
Så vi har skapar två variabler: spelare och fiende  som innehåller namnet på våra karaktärer. Enkelt. 
Låt oss presentera fighten för vår användare genom att skriva ut på skärmen med hjälp av kommandont print.
```python
print("Den mäktiga striden i Morias grottor är påväg att starta")
```
För att hämta innehållet i variablerna skriver man bara variablernas namn:
```python
print(spelaren + "står på bron och tittar ned på " + fienden + " i avgrunden")
```

Vi kan även hålla reda på livet på våra karaktäerer. 
```python
spelare_liv = 100
fiende_liv = 100
```
Vad jag kallar variablerna är inte viktigt. Så länge de är lokiska för mig. I Detta fall känndes det bra att "koppla" livet till karaktären.

Nu till vapen. Vad har Gandalf att slåss med. En stav. Hrmm... Inte så mäktigt men effektivt. 
```python
spelare_vapen="Stav"
spelare_vapen_skada=10
```
Och Balrogen då. Han har en piska om jag inte missminner mig. 
```python
fiende_vapen="Piska"
fiende_vapen_skada=30
```
Så hur ser vår kod ut nu:
```python
spelare = "Gandalf"
spelare_liv = 100
spelare_vapen="Stav"
spelare_vapen_skada=10

fiende = "Balrog"
fiende_liv = 100
fiende_vapen="Piska"
fiende_vapen_skada=30

print("Den mäktiga striden i Morias grottor är påväg att starta.")
print(spelaren + "står på bron och tittar ned på " + fienden + " i avgrunden")

```

Nu kan vi börja slåss:

```python
print(spelare + " slår med sin " +spelare_vapen +" och gör: "+ str(spelare_vapen_skada) +" skada")
fiende_liv = fiende_liv - spelare_vapen_skada
print(fiende + " har nu bara " + str(fiende_liv)+ " hälsopoäng kvar")
```
Här hände det mycket + betyder att vi slåt ihop texterna. sen har vi str(spelare_vapen_skada) till exempel. spelare_vapen_skada innehåller ett tal (10 om jag inte missminner mig). Detta är ett problem så vi behöver göra om talet till en text och text i python heter string så str() är en förkortning till "gör om det i parentesen till en text" .

Hela programmet:

```python
spelare = "Gandalf"
spelare_liv = 100
spelare_vapen="Stav"
spelare_vapen_skada=10

fiende = "Balrog"
fiende_liv = 100
fiende_vapen="Piska"
fiende_vapen_skada=30

print("Den mäktiga striden i Morias grottor är påväg att starta.")
print(spelaren + "står på bron och tittar ned på " + fienden + " i avgrunden")

print(spelare + " slår med sin " +spelare_vapen +" och gör: "+ str(spelare_vapen_skada) +" skada")
fiende_liv = fiende_liv - spelare_vapen_skada
print(fiende + " har nu bara " + str(fiende_liv)+ " hälsopoäng kvar")
```
## Lägga till val
Allt detta är statiskt. För varje gång som vi kör programmet kommer det alltid se ut som det gör. 
Om vi skall göra detta till ett spel och inte bara en saga (där allting sker på samma sätt varje gång) så kanske vi vill lägga till lite interaktivitet.
Interaktivitet får man genom att låta användaren påverka saker. 
Jag vill kanske döpa om min spelarkaraktär. 
```python
spelare = input("Vad vill du att din spelare skall heta?")
```
Med hjälp av input() kan jag som spelare mata in saker till datorn med tangentbordet. Det som jag skriver innom parentesen är den text som kommer upp på skärmen innan jag matar in. 
Precis som förut så sparar vi namnet i variabeln spelare. Så vi lätt kan ta fram det när vi vill använda det i vår berättelse. 
```python
print("Var hälsad, "+spelare+"!")
```
Ett annat sätt att skapa interaktivitet är att låta spelaren bestämma saker i till exempel en strid. 
```python
svar = input("Vad vill du göra härnäst? (slå/fly) ")
if(svar=="slå"):
    print(spelare + " slår med sin " +spelare_vapen +" och gör: "+ str(spelare_vapen_skada) +" skada")
    fiende_liv = fiende_liv - spelare_vapen_skada
    print(fiende + " har nu bara " + str(fiende_liv)+ " hälsopoäng kvar")
else:
    print("Du flyr!")
```
## Upprepning
Vi skulle vilja fortsätta slå tills någon har vunnit/förlorat. För att hantera detta använder vi så kallade loopar.
Det finns två sätt att hantera loopar antingen så loopar man ett bestämt antal gånger eller så loopar man tills ett
villkor uppfylls. I detta fall vet vi inte hur många gångar vi behöver slå tills vi vunnit. Så vi sätter ett villkor så länge mitt liv är över 0 och fiendens liv är över 0.
```python
while(spelare_liv > 0 AND fiende_liv > 0):
    # Slåss!!
```
Så då kan vi lägga in slagsmålet i loopen. Jag slår, han slår och så fortsätter vi tills någon har 0 liv.
```python
while(spelare_liv > 0 AND fiende_liv > 0):
    # Du slår
    print(spelare + " slår med sin " +spelare_vapen +" och gör: "+ str(spelare_vapen_skada) +" skada")
    fiende_liv = fiende_liv - spelare_vapen_skada
    print(fiende + " har nu bara " + str(fiende_liv)+ " hälsopoäng kvar")
    # Fiende slår
    print(fiende + " slår med sin " +fiende_vapen +" och gör: "+ str(fiende_vapen_skada) +" skada")
    spelare_liv = spelare_liv - fiende_vapen_skada
    print(spelare + " har nu bara " + str(spelare_liv)+ " hälsopoäng kvar")

```



Nu har du grunderna till att göra ett enkelt äventyrsspel. 
Ditt uppdrag är att skapa ett enkelt spel där man kan bestämma sitt namn och där jag kan slåss mit en motståndare. 
Om jag överlever efter jag slagit så har jag vunnit. 
