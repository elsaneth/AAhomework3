# Linear Search

## Ajaline keerukus

Ajaline keerukus on parimal juhul O(1) - sellisel juhul peab otsitav väärtus olema esimesel indeksil. Algoritm leiab otsitava väärtuse esimesel võrdlusel.

Halvimal ja ilmselt ka keskmisel juhul on ajaline keerukus O(n).

## Ruumiline keerukus

Ruumiline keerukus on O(1), kuna iteratsiooni käigus mälu kasutus ei suurene sisendi suurenedes.

## Reaalmaailma rakendused

Linear Search sobib kasutamiseks andmete puhul, mis ei ole sorteeritud ning väiksematele andmemahtudele või kui on teada, et otsitav väärtus on listi alguses. Samuti on see hea otsimisalgoritm algajale arendajale, kuna seda on lihtne implementeerida.

1. E-poed: selle abil saab filtreerida tooteid nt hinna, tüübi või firma järgi

2. Raamatukogu: aitab leida õige riiuli autori nime, raamatu pealkirja või tüübi järgi

3. Telefonikontaktid: aitab leida kiiresti soovitud nimega kontakti. Üldjuhul soovitakse helistamisel leida kindla inimesi kontakti ning Linear Search otsib hästi vastava nimega kontakti.

Rakendusi leidub veel, ka sarnastel eesmärkidel nagu eelnevalt kirjeldatud. 

## Piirangud

1. Kuna otsitakse väärtust ükshaaval, siis algoritm on aeglane suurte andemahtude juures

2. Kui suured andmemahud on juba sorteeritud kujul oleks mõistlik kasutada mingit muud algoritmi, mis on suurte andmemahtude korral efektiivsem ja kiirem

3. Lineaarne otsing on lihtne kasutada, aga seda ka lihtsate päringute korral. Kui on tarvis teha keerukamaid päringuid erinevate tingumustega, siis võib Linear Search osutuda ebaefektiivseks.

4. Võib kasutada ka suurte andmemahtude korral kui otsingut teostatakse harva. Kui on vaja otsingut teostada tihti on mõistlik kasutada muud algoirtimi. 

