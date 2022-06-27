# TesseractOCR


* Authors: Rui Fontes <rui.fontes@tiflotecnia.com> and  Angelo Abrantes <ampa4374@gmail.com>
* Updated in 26/06/2022
* Download [stable version][1]
* Compatibility: NVDA version 2019.3 and beyond


## Informations

This add-on uses the free and open source Tesseract OCR engine, to perform optical character recognition on an image file, PDF, JPG, TIF or other, without the need to open it.
It also uses wia-cmd-scanner to be able to access WIA enabled scanners and perform OCR to a paper document.
In the Preferences of NVDA, it  is created a cathegory, TesseractOCR, where you can set the first and second languages to be used on the recognition and the type of documents to be recognized.
It is also available a combobox to select tmore recognition languages to download and install on the add-on. So, the add-on now ships only with english and portuguese recognition languages.
Note that using two recognition languages makes the OCR process a bit longer. So, it is available a button to forget the second language. And also note that the quality of the recognition may vary according to the order of the languages.


## Shortcut

The default commands are:
Windows+Control+r - to recognize the selected document;
Windows+Control+Shift+r - to scan and recognize a document through the scanner.

Then just wait that ocr.txt opens with the recognized text.
If you want to preserve the recognized text, don't forget to save the document under another name and in another location, as all files in the temporary directory are deleted at the start of the next OCR process!

This commands can be modified in the "Input gestures" dialog in the "TesseractOCR" section.


## Automatic update
This add-on includes an automatic update feature.
The check for a new version will be executed everytime NVDA is loaded.
If you want this, go to NVDA, Preferences, Options and in the add-on category check the check box.


## Known problems

* When selecting the "Various" option in the "Documents type" combobox, the recognized text probably appear with many blank lines
This is a known problem with Tesseract, and, without consumming lots of processing time, I haven't yet found any solution. But, I still haven't given up!


## Languages supported

The supported languages in this version are:
Afrikans
Albanian
Amharik
Arabic
Armenian
Assamese
Azerbaijani (Latin)
Basque
Belarusian
Bengali
Bosnian
Breton
Bulgarian
Burnese
Catalan/Valencian
Cebuano
Cherokee
Chinese simplified
Chinese traditional
Corsican
Croatian
Czech
Dannish
Deutch
Dhivehi
Dutch (Flemish)
Dzongkha
English
Esperanto
Estonian
Faroese
Filipino
Finnish
French
Galician
Georgian
Greek
Gujarati
Haitian
Hebrew
Hindi
Hungarian
Icelandic
Indonesian
Inuktitut
Irish
Italian
Javanese
Japanese
Kannada
Kazakh
Khmer (Central)
Kirghiz
Korean
Kurdish Kurmanji
Lao
Latin
Lativia
Lituanian
Luxembourgish
Macedonian
Malay
Malayalam
Maltese
Maori
Marathi
Math / equation detection module
Mongolian
Nepali
Norwegian
Occitan
Oriya
Panjabi
Pashto
Persian
Polish
Portuguese
Quechua
Romanian/Moldave
Russian
Sanskrit
Scottish Gaelic
Serbian (Latin)
Slovak)
Slovenian)
Sindhi
Sinhalese
Spanis
Sundanese
Swahili
Swedish
Syriac
Tajik
Tamil
Tatar
Telugu
Thai
Tibetan
Tigrinya
Tonga
Turkish
Uighur
Ukrainian
Urdu 
Uzbek (Latin)
Vietnamese
Welsh
West Frisian
Yiddish
Yoruba


## Image types supported

This add-on supports the following types of files:
PDF
jpg
tif
png
bmp
pnm
pbm
pgm
jp2
gif
jfif
jpeg
tiff
spix
webp


[1]: https://github.com/ruifontes/tesseractOCR/releases/download/2022.06.27/tesseractOCR-2022.06.27.nvda-addon
