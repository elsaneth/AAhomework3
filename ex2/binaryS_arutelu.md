# Bianry Search

## Binary Search vs Linear Search

Linear Search algoritmi ajakompleksus on O(n), Binary Search Algoritmi otsingu ajakompleksus on O(log(n)). Lineaarne otsing teostab otsingut ükshaaval, halvimal juhul on otsitav väärtus andmete lõpus või ei ole seda üldse. Kui lineaarset otsingut saab kasutada sorteerimata andmete korral, siis Binary Search algoritm töötab sorteeritud andmetega. Binary Search jagab andmed pooleks ning vaatab, kumba poolt jätkata (parem või vasak). Lõpuks peaks alamandmekogu (algoritm jagab kogu aeg andmed poolek) keskpunkt vastama otsitavale väärtusele (kui see väärtus esineb andmekogus).

Lineaarne otsing on lihtne, kuid selle otsimise ajakompleksus on samuti lineaarne O(n), mis võib suurte andmemahtude korral olla ebaefektiivne. Binaarsel otsingul peab olema täidetud tingimus, et andmed on sorteeritud, mis võib osutuda mingite andmete korral piiranguks. Binaarne otsing sobib paremini suurte andmemahtude korral, otsimine on kiirem kui lineaarse algoritmi puhul. Küll aga võib binaarse andmestruktuuri korral muutuda andmete lisamine mingi hetk lineaarseks (näidatud lilla kastiga joonisel (fail: binaryS_joonis.pdf)). Sellisel juhul oleks vaja andmestruktuur ümber teha, et ajalinekompleksus O(log(n)) säiliks.

## Binary Search kasulikum kui Linear Search

Nagu juba ka enne mainitud, sobib Binary Search algoritm paremini suurte andmemahtude korral. 

Binary Search võib olla kasulikum sõna otsimisel sõnaraamatust.

Eesti keelest on teada 2,4 miljardit sõna [1]. Eesti keele "Õigekeelsussõnaraamatus" 2006 on 130 000 sõna [2], mida on kõvasti vähem kui teadaolevaid sõnu, aga endiselt palju. Linear Search korral peaks otsitava sõna jaoks läbi käima sõnastiku algusest üks-haaval ning kui otsitav sõna on sõnastiku lõpus, tehtaks mõttetut tööd võrreldes iga sõna üks-haaval. Binary Search abil saaks need 130 000 pidevalt jagada kaheks ning valida vastavalt suuna kummale poole liigutakse (parem/vasak) ning otsitav sõna leitaks tunduvalt kiiremini.

[1] https://leht.postimees.ee/7460253/ak-eki-keelekool-kui-palju-on-eesti-keeles-sonu
[2] https://www.eki.ee/books/ekk09/index.php?id=551&p=6&p1=5
