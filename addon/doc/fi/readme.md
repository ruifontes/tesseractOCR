# TesseractOCR


* Tekijät: Rui Fontes, Ângelo Abrantes ja Abel Passos do Nascimento nuorempi
* Päivitetty 25.02.2024
* Lataa [vakaa versio][1]
* Yhteensopivuus: NVDA 2019.3 ja uudemmat


## Tiedot

Tämä lisäosa käyttää ilmaista, avoimen lähdekoodin Tesseract-tekstintunnistusmoottoria tekstintunnistuksen suorittamiseen kuvatiedostolle (PDF, JPG, TIF ja muut) tarvitsematta avata sitä.
Se mahdollistaa myös WIA-yhteensopivan scannerin käytön tekstintunnistuksen suorittamiseen paperimuotoisille asiakirjoille.
Finally, it also can get the accessible text from an accessible PDF.
NVDA:n asetusvalintaikkunaan on lisätty TesseractOCR-kategoria, jossa voit muuttaa seuraavia asetuksia:
- Tunnistuksessa käytettävät kielet
- Tunnistettavat asiakirjaformaatit
- Kysytäänkö PDF-asiakirjan salasanaa. Jos tämä asetus on valittuna ja PDF-ää ei ole suojattu salasanalla, paina Enter salasanaa pyytävässä valintaikkunassa.
- Valitse käytettävä skanneri
- Määritä skannerin tarkkuus väliltä 150–400 pistettä tuumalla.

Lisäosaan sisältyviä englantia ja portugalia lukuun ottamatta tunnistuskielet ladataan ja asennetaan niitä valittaessa.
Huom: Tekstintunnistus kestää sitä kauemmin, mitä enemmän tunnistuskieliä on valittuna.
Siksi suosittelemme, että käytät vain tarvitsemiasi kieliä.
Huomaa myös, että tunnistuksen laatu voi vaihdella sen mukaan, missä järjestyksessä kielet ovat.
Siksi kannattaa kokeilla järjestää kielet eri tavalla, jos tunnistuksen tulos ei ole tyydyttävä.


## Pikanäppäimet

Oletuskomennot ovat:
Win+Ctrl+R: Suorittaa tekstintunnistuksen valitulle asiakirjalle
Win+Ctrl+W: Skannaa skannerissa olevan asiakirjan ja suorittaa sille tekstintunnistuksen
Windows+Control+t - To get the text from an accessible PDF;
Win+Ctrl+C: Peruuttaa skannauksen
Huom: Komentoa on käytettävä ennen lisäsivujen skannausta kysyvän valintaikkunan ilmestymistä.

Tunnistettu teksti ilmestyy jonkin ajan kuluttua erilliseen ikkunaan, jossa voit tarkastella sitä.
Muista tallentaa tunnistettu teksti, jos haluat säilyttää sen, koska tunnistuksen tulokset poistetaan, kun seuraava tunnistusprosessi alkaa.

Näitä komentoja on mahdollista muuttaa \"Näppäinkomennot\"-valintaikkunan \"TesseractOCR\"-osiossa.


## Tunnetut ongelmat

* Kun \"Asiakirjan tyyppi\" -yhdistelmäruudusta valitaan \"Useita\"-vaihtoehto, tunnistettuun tekstiin tulee todennäköisesti paljon tyhjiä rivejä.
Tämä on tunnettu ongelma Tesseractissa, eikä toistaiseksi ole löytynyt sellaista ratkaisua, jota käytettäessä tiedoston käsittely ei kestäisi kauan.


## Tuetut kielet

Tämä versio tukee seuraavia kieliä:
* afrikaans
* albania
* amhara
* arabia
* armenia
* assami
* azeri (latinalainen)
* baski
* valkovenäjä
* bengali
* bosnia
* bretoni
* bulgaria
* burma
* katalaani/valencia
* cebuano
* cherokee
* kiina (yksinkertaistettu)
* kiina (perinteinen)
* korsika
* kroatia
* tšekki
* tanska
* saksa
* divehi
* hollanti (flaami)
* dzongkha
* englanti
* esperanto
* viro
* fääri
* filipino
* suomi
* ranska
* galicia
* georgia
* kreikka
* gudžarati
* haitilainen kreoli
* heprea
* hindi
* unkari
* islanti
* indonesia
* inuktitut
* iiri
* italia
* jaava
* japani
* kannada
* kazakki
* keski-khmer
* kirgiisi
* korea
* kurdi (kurmandži)
* lao
* latina
* latvia
* liettua
* luxemburg
* makedonia
* malaiji
* malajalam
* malta
* maori
* marathi
* matemaattiset yhtälöt
* mongoli
* nepali
* norja
* oksitaani
* orija
* pandžabi
* paštu
* persia
* puola
* portugali
* ketšua
* romania/moldova
* venäjä
* sanskrit
* gaeli
* serbia (latinalainen)
* slovakki
* sloveeni
* sindhi
* sinhali
* espanja
* sunda
* swahili
* ruotsi
* syyria
* tadžik
* tamili
* tataari
* telugu
* thai
* tiibet
* tigrinja
* tonga
* turkki
* uiguuri
* ukraina
* urdu
* uzbekki (latinalainen)
* vietnam
* kymri
* länsifriisi
* jiddiš
* joruba


## Tuetut kuvaformaatit

Tämä lisäosa tukee seuraavia tiedostotyyppejä:
* PDF
* JPG
* TIF
* PNG
* BMP
* PNM
* PBM
* PGM
* JP2
* GIF
* JFIF
* JPEG
* TIFF
* SPIX
* WebP


[1]: https://github.com/ruifontes/tesseractOCR/releases/download/2024.02.25/tesseractOCR-2024.02.25.nvda-addon
