# TesseractOCR


* Autores: Rui Fontes, Ângelo Abrantes y Abel Passos do Nascimento Jr.
* Actualizado el 23/07/2022
* Descargar [versión estable][1]
* Compatibilidad con NVDA: versión 2019.3 y posteriores


## Información

Este complemento usa el motor libre y de código abierto Tesseract OCR para realizar reconocimiento óptico de caracteres en un archivo de imagen, PDF, JPG, TIF o de otro tipo, sin que sea necesario abrirlo.
También puede escanear y reconocer un documento en papel mediante un escáner compatible con WIA.
En las Preferencias de NVDA, se añade la categoría TesseractOCR, donde se pueden configurar los idiomas a utilizar durante el reconocimiento y los tipos de documentos a reconocer.
En este diálogo, para poder hacer el reconocimiento  de texto a los archivos PDF protegidos con contraseña, puede marcar para solicitar contraseña.
Si tiene esta opción marcada y el PDF no tiene una contraseña, simplemente pulse  Intro en el diálogo  solicitando contraseña.
Con la excepción del inglés y el portugués, que ya están incluidos en el complemento, los otros idiomas se descargarán e instalarán cuando seleccione un idioma que aún no existe en el complemento.
Tenga en cuenta que a medida que aumenta el número de idiomas de reconocimiento seleccionados, el proceso OCR llevará más tiempo.
Por lo tanto, recomendamos que use solo los idiomas que necesita.
Tenga en cuenta también que la calidad del reconocimiento puede variar según el orden de los idiomas.
Por lo tanto, si el resultado del reconocimiento no es satisfactorio, es posible que desee probar otro orden de los idiomas.


## Atajos

Los atajos por defecto son:
Windows+Control+r - para reconocer el documento seleccionado;
Windows+Control+w - para escanear y reconocer un documento desde el escáner.

A continuación, espera a que se abra el archivo ocr.txt con el texto reconocido.
Si quieres conservar el texto reconocido, ¡no olvides guardar el documento con otro nombre y en otro lugar, ya que todos los archivos de la carpeta temporal se eliminan al comienzo del siguiente proceso OCR!

Estas órdenes pueden modificarse desde el diálogo Gestos de entrada, en la categoría "TesseractOCR".


## Actualización automática
Este complemento incluye una función de actualización automática.
La comprobación de una nueva versión se realizará cada vez que se cargue NVDA.
Si quieres que esto suceda, vas al menú de NVDA, Preferencias, Opciones y en la categoría del complemento marcas la casilla de verificación.


## Problemas conocidos

* En algunos sistemas es posible que el complemento no funcione debido a un error de comtypes...
En algunas máquinas es suficiente ir a la carpeta temp y eliminar la carpeta comtypes_cache.
* Al elegir la opción "Diversos" en el cuadro combinado "Tipo de documento", el texto reconocido puede aparecer con muchas líneas en blanco.
Este es un problema conocido de Tesseract y, sin consumir un montón de tiempo de procesamiento, todavía no he encontrado una solución. ¡Pero aún no me he rendido!


## Idiomas soportados

Los idiomas soportados en esta versión son:
* Africano
* Albanés
* Amárico
* Árabe
* Armenio
* Asamés
* Azerbaiyano (Latino)
* Vasco
* Bielorruso
* Bengalí
* Bosnio
* Bretón
* Búlgaro
* Burmés
* Catalán / Valenciano
* Cebuano
* Cherokee
* Chino simplificado
* Chino tradicional
* Corso
* Croata
* Checo
* Danés
* Alemán
* Dhivehi
* Holandés (Flamenco)
* Dzongkha
* Inglés
* Esperanto
* Estonio
* Feroés
* Filipino
* Finlandés
* Francés
* Gallego
* Georgiano
* Griego
* Gujarati
* Haitiano
* Hebreo
* Hindi
* Húngaro
* Islandés
* Indonesio
* Inuktitut
* Irlandés
* Italiano
* Javanés
* Japonés
* Kannada
* Kazajo
* Jemer (Central)
* Kirguís
* Coreano
* Kurdo Kurmanji
* Laosiano
* Latino
* Letón
* Lituano
* Luxemburgo
* Macedonio
* Malayo
* Malayalam
* Maltés
* Maori
* Marathi
* Ecuaciones matemáticas
* Mongol
* Nepalí
* Noruego
* Occitano
* Oriya
* Panyabí
* Pashto
* Persa
* Polaco
* Portugués
* Quechua
* Rumano / Moldavo
* Ruso
* Sanskrit
* Gaélico Escocés
* Serbio (Latino)
* Eslovaco
* Esloveno
* Sindhi
* Cingalés
* Español
* Sondanés
* Swahili
* Sueco
* Siríaco
* Tajik
* Tamil
* Tatar
* Telugu
* Tailandés
* Tibetan
* Tigrinya
* Tongano
* Turco
* Uigures
* Ucraniano
* Urdu
* Uzbeko (Latino)
* Vietnamita
* Galés
* Frisio Oeste
* Yídish
* Yoruba


## Tipos de imagen soportados

Este complemento soporta los siguientes tipos de archivos:
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


[1]: https://github.com/ruifontes/tesseractOCR/releases/download/2022.07.23/tesseractOCR-2022.07.23.nvda-addon
