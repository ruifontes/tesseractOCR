# TesseractOCR


* Autori: Rui Fontes, Ângelo Abrantes e Abel Passos do Nascimento Jr.
* Scarica la [versione stabile][1]
* Compatibilità: NVDA version 2019.3 e successive


## Informazioni

Questo componente aggiuntivo utilizza il motore gratuito ed open source Tesseract OCR  per eseguire il riconoscimento ottico dei caratteri su un file immagine, PDF, JPG, TIF o altro, senza la necessità di aprire il file stesso.
Consente inoltre l'accesso agli scanner compatibili con WIA per eseguire l'OCR di un documento cartaceo.
Nel menu di NVDA, Preferenze, Impostazioni..., viene aggiunta una sezione TesseractOCR, nella quale è possibile configurare quanto segue:
- le lingue da utilizzare per il riconoscimento;
- la tipologia dei documenti da riconoscere;
- se deve essere richiesta o meno una password per i files PDF. Se hai selezionato questa opzione e il PDF non è protetto da una password, premi semplicemente Invio nella finestra di dialogo che ne richiede l'inserimento;
- Lo scanner da usare;
- la risoluzione dello scanner tra 150 e 400 dpi.

Ad eccezione dell'inglese e del portoghese, che sono già incluse, le altre lingue verranno scaricate ed installate quando ne viene selezionata una che non è già presente all'interno del componente.
Tieni presente che con l'aumento del numero di lingue di riconoscimento selezionate, il processo OCR richiederà più tempo.
Ti consigliamo quindi di utilizzare solo quelle di cui hai bisogno.
Si noti inoltre che la qualità del riconoscimento può variare in base all'ordine delle lingue. Pertanto, se il risultato non è soddisfacente, potresti provare un altro ordinamento.

## Comandi rapidi

I comandi predefiniti sono:
Windows+Control+r - per riconoscere il documento selezionato;
Windows+Control+w - per riconoscere un documento dallo scanner;
Windows+Control+c - Per annullare la scansione in corso.
Nota: il comando sopra deve essere dato prima che venga visualizzata la finestra di dialogo che chiede se si desidera scansionare più pagine!

Ora attendi che venga visualizzato il file di testo con il risultato del processo OCR.
Se vuoi conservarlo, non dimenticare di salvarlo in una cartella, poiché i risultati verranno eliminati all'inizio del successivo processo OCR!

Questi comandi possono essere modificati nella finestra "gesti e tastidi immissione", nella sezione tesseractOCR".


## Problemi conosciuti

* Quando si seleziona l'opzione "Varie" nella casella combinata "Tipo documenti", il testo riconosciuto probabilmente appare con molte righe vuote
questo è un problema noto con Tesseract, e, senza perdere molto tempo, non ho ancora trovato alcuna soluzione. Ma ancora non mi sono arreso!


## Lingue supportate

Le lingue supportate in questa versione sono:
* Afrikano
* Albanese
* Amarico
* Arabo
* Armeno
* Assamese
* Azero (latino)
* Basco
* Bengalese
* Bielorusso
* Bosniaco
* Bretone
* Bulgaro
* Burnese
* Catalano/Valenciano
* Cebuano
* Ceco
* Cherokee
* Cinese semplificato
* Cinese tradizionale
* Coreano
* Corso
* Croato
* Danese
* Dhivehi
* Dzongkha
* Ebraico
* Equazioni matematiche
* Esperanto
* Estone
* Faroese
* Filippino
* Finlandese
* Francese
* Frisone occidentale
* Gaelico Scozzese
* Galiziano
* Gallese
* Georgiano
* Giapponese
* Giavanese
* Greco
* Gujarati
* Haitiano
* Hindi
* Indonesiano
* Inglese
* Inuktitut
* Irlandese
* Islandese
* Italiano
* Kannada
* Kazako
* Khmer (centrale)
* Kirghiso
* Kurmanji Curdo
* Laotiano
* Latino
* Lettone
* Lituano
* Lussemburghese
* Macedone
* Malayalam
* Malese
* Maltese
* Maori
* Marathi
* Mongolo
* Nepalese
* Norvegese
* Occitano
* Olandese (fiammingo)
* Oriya
* Panjabi
* Pashtu
* Persiano
* Polacco
* Portoghese
* Quechua
* Rumeno/Moldavo
* Russo
* Sanscrito
* Serbo (latino)
* Sindhi
* Singalese
* Siriaco
* Slovacco)
* Sloveno)
* Spagnolo
* Sundanese
* Svedese
* Swahili
* Tagico
* Tailandese
* Tamil
* Tartaro
* Tedesco
* Telugu
* Tibetano
* Tigrino
* Tonga
* Turco
* Ucraino
* Uiguro
* Ungherese
* Urdu 
* Uzbeco (latino)
* Vietnamita
* Yiddish
* Yoruba


## Tipi di immagini supportate

Questo addon supporta i seguenti tipi di files:
* PDF
* jpg
* tif
* png
* bmp
* pnm
* pbm
* pgm
* jp2
* gif
* jfif
* jpeg
* tiff
* spix
* webp


[1]: https://github.com/ruifontes/tesseractOCR/releases/download/2024.03.24/tesseractOCR-2024.03.24.nvda-addon
