# TesseractOCR


* Tekijät: Rui Fontes, Ângelo Abrantes ja Abel Passos do Nascimento nuorempi
* Lataa [vakaa versio][1]
* Yhteensopivuus: NVDA 2019.3 ja uudemmat


## Tiedot

Tämä lisäosa käyttää ilmaista, avoimen lähdekoodin Tesseract-tekstintunnistusmoottoria tekstintunnistuksen suorittamiseen kuvatiedostolle (PDF, JPG, TIF ja muut) tarvitsematta avata sitä.
Tunnistuksen tulokset tallennetaan tekstitiedostoon, joka sijoitetaan samaan kansioon tunnistettavan tiedoston kanssa, ja sen nimi on sama kuin alkuperäisen tiedoston, mutta tiedostopääte on .txt.
Se mahdollistaa myös WIA-yhteensopivan scannerin käytön tekstintunnistuksen suorittamiseen paperimuotoisille asiakirjoille.
Tulokset näytetään OCR.txt-nimisessä tiedostossa, joka sijoitetaan käyttäjän Tiedostot-kansioon.
Lisäksi se voi hakea tekstin saavutettavasta PDF-tiedostosta XPDF-työkaluja käyttäen.
NVDA:n asetusvalintaikkunaan on lisätty TesseractOCR-kategoria, jossa voit muuttaa seuraavia asetuksia:
- Tunnistuksessa käytettävät kielet
- Tunnistettavat asiakirjamuodot
- Pyydetäänkö PDF-asiakirjan salasanaa. Jos tämä asetus on valittuna ja PDF-ää ei ole suojattu salasanalla, paina Enter salasanaa pyytävässä valintaikkunassa.
- Määritä skannerin tarkkuus väliltä 150–400 pistettä tuumalla
- Paperin asennon tunnistaminen
- Käytetäänkö tunnistuksen edistymistä ilmaisevia äänimerkkejä

Lisäosaan sisältyviä englantia ja portugalia lukuun ottamatta tunnistuskielet ladataan ja asennetaan niitä valittaessa.
Huom: Tekstintunnistus kestää sitä kauemmin, mitä enemmän tunnistuskieliä on valittuna.
Siksi suosittelemme, että käytät vain tarvitsemiasi kieliä.
Huomaa myös, että tunnistuksen laatu voi vaihdella sen mukaan, missä järjestyksessä kielet ovat.
Siksi kannattaa kokeilla järjestää kielet eri tavalla, jos tunnistuksen tulos ei ole tyydyttävä.


## Pikanäppäimet

Oletuskomennot ovat:
Windows+Ctrl+W: Skannaa skannerissa olevan asiakirjan ja suorittaa sille tekstintunnistuksen
Windows+Ctrl+R: Suorittaa tekstintunnistuksen valitulle asiakirjalle
Windows+Ctrl+T: Hakee tekstin saavutettavasta PDF-tiedostosta
Windows+Ctrl+C: Peruuttaa skannauksen
Huom: Komentoa on käytettävä ennen lisäsivujen skannausta kysyvän valintaikkunan ilmestymistä.

Tunnistetun tekstin sisältävä tekstitiedosto avautuu jonkin ajan kuluttua.

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
* skottilainen gaeli
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


[1]: https://github.com/ruifontes/tesseractOCR/releases/download/2024.11.02/tesseractOCR-2024.11.02.nvda-addon
