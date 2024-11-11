from algemene_functies import mijn_functie_2

def aanbieding_1(smaak, prijs, korting):
    korting_1 = prijs * korting
    korting = prijs - korting_1
    uitvoer = f"Vandaag in de aanbieding: emmertje ijs (1 liter) in de smaak {smaak}, van {prijs} euro voor {korting} euro."
    return uitvoer

print(aanbieding_1("aardbei", 4, 0.1))

def inkomsten_totaal(inkomsten):
    btw = 0.09
    totale_inkomsten = sum(inkomsten)
    bedrag = totale_inkomsten * btw
    uitvoer = f"Het totaal van alle inkomsten van deze week is {totale_inkomsten} euro, waarover {bedrag} euro btw betaald dient te worden."
    return uitvoer

print(inkomsten_totaal([220, 430, 125, 160, 205, 90, 345]))

def laag_en_hoog(mijn_lijst):
    hoogste_waarde = max(mijn_lijst)
    laagste_waarde = min(mijn_lijst)
    uitvoer = hoogste_waarde, laagste_waarde
    return uitvoer

print(laag_en_hoog([220, 430, 125, 160, 205, 90, 345]))

def gemiddelde(mijn_lijst):
    totale_inkomsten = sum(mijn_lijst)
    gemiddelde_inkomsten = totale_inkomsten / 7
    uitvoer = f"De gemiddelde inkomsten deze week zijn {gemiddelde_inkomsten} euro"
    return uitvoer

print(gemiddelde([220, 430, 125, 160, 205, 90, 345]))

def meervoudig(invoer_lijst):
    hoog, laag = laag_en_hoog(invoer_lijst)
    return [hoog, laag]

print(meervoudig([10,5,3,2,1,2,9]))

def combinatie(invoer_lijst_2):
    korte_lijst = meervoudig(invoer_lijst_2)
    uitvoer = mijn_functie_2(*korte_lijst)
    return uitvoer

print(combinatie([10,5,3,2,1,2,9]))