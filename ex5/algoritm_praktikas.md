# Kiire kontakti leidmine telefoni rakenduses

## Personaalne telefoni rakendus

Kui telefonis ei ole kontakte palju, mis võib olla inimesel, kes kasutab helistamist rääkimaks vaid kõige lähedasematega. Sellisel juhul võiks ka Linear Search algoritm väga hästi toimida. Soovitakse leida kindla nimega kontakti ning nt 20 kontakti seast võiks Linear Search vastava kontakti kiiresti leida. Kontakte võib olla ka tunduvalt rohkem, lineaarne otsing võiks sellega ka hakkama saada. Lineaarne otsing sobib ka seetõttu, et tegemist ilmselt ei ole väga keerulise andmestruktuuriga, üldujul kontaktinimele vastab telefoninumber. Kontaktide loend võib aja jooksul muutuda, sh suureneda või väheneda. Lineaarse otsingu puhul on kontaktide uuendamine kiire ja lihtne. 

Selleks, et antud algoritm suudaks paremini leida kontakte on võimalik lisada rakendusele nt automaatne täitmine, kui kasutaja kirjutab kontakti nime, siis rakendus pakub juba võimaliku nime, mida kasutaja otsib. Samuti on võimalik salvestada kiirmenüüse tihti kasutatud kontakid või viimati kasutatud kontaktid.

## Ettevõtte telefoni rakendus

Kui tegemist on nt mingi suure ettevõtte töötajate telefoninumbrite andmebaasiga. Siis võib osutuda paremaks juhuks binaarne otsing või isegi kolmikotsing. Binaarne otsing sobiks paremini kuna suurel ettevõttel on kontakte palju ning oleks parem kui need kontaktid on sorteeritud nt nime alusel. Samuti võib olla lisaks nimele ja numbrile olla kirjas nt osakond, kus vastav inimene töötab, mis lisab andmetele keerukust ning lineaarne otsing ei ole enam sobilik. Samas kui kontakte uuendatakse pidevalt, on võimalik, et peab andmeid ümber struktureerima. Kontaktide pideval lisamisel võib juhtuda, et otsimine muutub mingis suunas lineaarseks. 

Algoritmi saaks paremaks muuta nt indekseerimisega ning teostada otsinguid indeksite alusel, otsing muutuks kiiremaks. Lisaks tähestikulisele sorteerimisele, oleks ettevõttel mõistlik jagada ka kontaktid vastaval osakonnale ning samamoodi osakonnad tiimideks vms. Kui on tegemist suurema tiimiga, kus on liikmeid erinevatest valdkondadest saab ka nt nt tiimi jagada vastavalt (nt äripool ja insenerid). 