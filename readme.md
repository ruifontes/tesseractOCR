# TesseractOCR


* Authors: Rui Fontes <rui.fontes@tiflotecnia.com> and  Angelo Abrantes <ampa4374@gmail.com>
* Updated in 21/03/2022
* Download [stable version][1]
* Compatibility: NVDA version 2019.3 and beyond


## Informations

This add-on uses the free and open source Tesseract OCR engine, to perform optical character recognition on an image file, PDF, JPG, TIF or other, without the need to open it.
It also can scan and recognize a paper document through a WIA compatible scanner.
In the Preferences of NVDA, it  is created a cathegory, TesseractOCR, where you can set the language to be used on the recognition and the type of documents to be recognized.


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

* This version only works in 64-bit Windows.
* When selecting the "Various" option in the "Documents type" combobox, the recognized text probably appear with many blank lines
This is a known problem with Tesseract, and, without consumming lots of processing time, I haven't yet found any solution. But, I still haven't given up!


## Languages supported

The supported languages in this version are:
Afrikans
Amharik
Arabic
Bulgarian
Burnese
Catalan/Valencian
Chinese simplified
Chinese traditional
Croatian
Czech
Dannish
Deutch
Dutch
English
Finnish
French
Galician
Georgian
Greek
Hebrew
Hindi
Hungarian
Icelandic
Indonesian
Irish
Italian
Japanese
Kannada
Kirghiz
Korean
Lativia
Lituanian
Macedonian
Nepali
Norwegian
Panjabi
Persian
Polish
Portuguese
Romanian/Moldave
Russian
Serbian (Latin)
Slovak)
Slovenian)
Spanis
Swedish
Tamil
Thai
Turkish
Ukrainian
Urdu 
Vietnamese

 
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


[1]: https://github.com/ruifontes/tesseractOCR/releases/download/2022.05/tesseractOCR-2022.05.nvda-addon
