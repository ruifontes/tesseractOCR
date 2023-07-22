# TesseractOCR


* Authors: Rui Fontes, Ângelo Abrantes and Abel Passos do Nascimento Jr.
* Updated in 22/07/2023
* Download [stable version][1]
* Compatibility: NVDA version 2019.3 and beyond


## Information

This add-on uses the free and open source Tesseract OCR engine, to perform optical character recognition on an image file, PDF, JPG, TIF or other, without the need to open it.
It also allows access to WIA enabled scanners to perform OCR to a paper document.
In the NVDA menu, Preferences, a TesseractOCR section is added, where you can configure the following:
- languages to be used in recognition;
- the type of documents to be recognized;
- if should be asked or not a PDF password. If you have this option checked, and the PDF does not have a password, just press Enter in the dialog asking for password;
- Select the scanner to be used;
- set the scanner resolution between 150 and 400 dpi.

With the exception of English and Portuguese, which are already included in add-on, the other languages will be downloaded and installed when you select a language that does not already exist in the add-on.
Note that as the number of selected recognition languages increases, the OCR process will take longer.
We therefore recommend that you use only the languages you need.
Note also that the quality of recognition may vary according to the order of languages.
Therefore, if the recognition result is not satisfactory, you may want to try another language ordering.


## Shortcut

The default commands are:
Windows+Control+r - to recognize the selected document;
Windows+Control+w - to scan and recognize a document through the scanner;
Windows+Control+c - To cancel the scanning process.
Please note: It must be issued before the dialog asking if you want to scan more pages appear!

Then just wait the browseable message appears with the recognized text.
If you want to preserve the recognized text, don't forget to save it in some folder, as the results are deleted at the start of the next OCR process!

This commands can be modified in the "Input gestures" dialog in the "TesseractOCR" section.


## Known problems

* When selecting the "Various" option in the "Documents type" combobox, the recognized text probably appear with many blank lines
This is a known problem with Tesseract, and, without consumming lots of processing time, I haven't yet found any solution. But, I still haven't given up!


## Languages supported

The supported languages in this version are:
* Afrikans
* Albanian
* Amharik
* Arabic
* Armenian
* Assamese
* Azerbaijani (Latin)
* Basque
* Belarusian
* Bengali
* Bosnian
* Breton
* Bulgarian
* Burnese
* Catalan/Valencian
* Cebuano
* Cherokee
* Chinese simplified
* Chinese traditional
* Corsican
* Croatian
* Czech
* Dannish
* Deutch
* Dhivehi
* Dutch (Flemish)
* Dzongkha
* English
* Esperanto
* Estonian
* Faroese
* Filipino
* Finnish
* French
* Galician
* Georgian
* Greek
* Gujarati
* Haitian
* Hebrew
* Hindi
* Hungarian
* Icelandic
* Indonesian
* Inuktitut
* Irish
* Italian
* Javanese
* Japanese
* Kannada
* Kazakh
* Khmer (Central)
* Kirghiz
* Korean
* Kurdish Kurmanji
* Lao
* Latin
* Lativia
* Lituanian
* Luxembourgish
* Macedonian
* Malay
* Malayalam
* Maltese
* Maori
* Marathi
* Math / equation detection module
* Mongolian
* Nepali
* Norwegian
* Occitan
* Oriya
* Panjabi
* Pashto
* Persian
* Polish
* Portuguese
* Quechua
* Romanian/Moldave
* Russian
* Sanskrit
* Scottish Gaelic
* Serbian (Latin)
* Slovak)
* Slovenian)
* Sindhi
* Sinhalese
* Spanish
* Sundanese
* Swahili
* Swedish
* Syriac
* Tajik
* Tamil
* Tatar
* Telugu
* Thai
* Tibetan
* Tigrinya
* Tonga
* Turkish
* Uighur
* Ukrainian
* Urdu 
* Uzbek (Latin)
* Vietnamese
* Welsh
* West Frisian
* Yiddish
* Yoruba


## Image types supported

This add-on supports the following types of files:
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


[1]: https://github.com/ruifontes/tesseractOCR/releases/download/2023.07.22/tesseractOCR-2023.07.22.nvda-addon
