# TesseractOCR


* Autores: Rui Fontes, Ângelo Abrantes e Abel Passos do Nascimento Jr.
* Actualizado em 04/09/2023
* Descarregar a [versão estável][1]
* Compatibilidade: NVDA 2019.3 e seguintes


## Informações

Este extra utiliza o motor de OCR Tesseract, de código aberto e gratuito, para executar o reconhecimento óptico de caracteres a um documento de imagem, seja PDF, JPG, TIF ou outro, sem necessidade de abrir o documento.
Também usa o módulo wia-cmd-scanner para aceder a scanners compatíveis WIA para digitalizar e reconhecer um documento em papel.
No menu do NVDA, Preferências é adicionada uma secção TesseractOCR, onde poderá configurar os idiomas a utilizar no reconhecimento e o tipo de documentos a reconhecer.
Neste diálogo, para poder fazer OCR a arquivos PDF protegidos por senha, pode marcar para ser solicitada uma senha.
Se esta opção estiver marcada, e o PDF não necessitar de senha, basta pressionar Enter na caixa de diálogo a pedir a senha.
À excepção dos idiomas português e inglês, que já são incluidos no extra, os restantes idiomas serão descarregados e instalados quando for seleccionado um idioma que ainda não exista no extra.
Note que à medida que aumenta o número de idiomas de reconhecimento seleccionados, o processo de OCR será mais longo.
Por isso, recomendamos a utilização apenas dos idiomas necessários.
Note também que a qualidade do reconhecimento pode variar de acordo com a ordem dos idiomas.
Portanto, se o resultado do reconhecimento não for satisfatório, pode tentar outra ordenação dos idiomas.


## Comandos

Os comandos predefinidos são:

Windows+Control+r - Para reconhecer o ficheiro seleccionado;
Windows+Control+w - Para digitalizar e reconhecer um documento através do scanner.

Depois é só esperar que se abra o ficheiro ocr.pdf.
Se pretender preservar o texto reconhecido, não se esqueça de guardar o documento com outro nome e noutro local, pois todos os ficheiros da pasta temporária são eliminados no início do próximo processo de OCR!


## Problemas conhecidos

* * Em alguns sistemas é possível que o add-on se recuse a trabalhar devido a um erro nos comtypes...
Em alguns sistemas é suficiente ir à pasta temp, e apagar a pasta comtypes_cache.
* Quando se selecciona a opção "Documentos variados" na caixa combinada "Tipo de documento", é provável que o texto reconhecido fique com demasiadas linhas em branco.


## Idiomas suportados

Os idiomas suportados nesta versão são:
* Africânder
* Albanês
* Alemão
* Amárico
* Árabe
* Arménio
* Assamês
* Azerbaijanês (Latim)
* Bangla
* Basco
* Belarrusso
* Bósnio (Latim)
* Bretão
* búlgaro
* Burnês
* Canarim
* Catalão/Valenciano
* Cazaquistanês
* Cebuano
* Checo
* Cheroqui
* Chinês simplificado
* Chinês tradicional
* Coreano
* Corso
* Croata
* Curdo Central
* Dinamarquês
* Divehi
* Dzongkha
* Equações matemáticas
* Eslovaco
* Esloveno
* Espanhol
* Esperanto
* Estónio
* Feroês
* Filipino
* Finlandês
* Francês
* Frísico Ocidental
* Galego
* Galês
* Galês da Escócia
* Georgiano
* Grego
* Guzarate
* Haitian
* Hebraico
* Hindi
* Húngaro
* Indonésio
* Inglês
* Inuktitut (Latim)
* Irlandês
* Islandêsv
* Italiano
* Javanês
* Japonês
* Kiswahili
* Kurdo do norte
* Laosiano
* Latim
* Letão
* Lituano
* Luxemburguês
* Macedónio
* Malaio
* Malayalam
* Maltês
* Maori
* Marati
* Mongol
* Neerlandês
* Nepalês 
* Norueguês
* Ocitano
* Odia
* Pastó
* Persa
* Polaco
* Português
* Punjabi
* Quechua
* Quirguize
* Romeno / Moldavo
* Russo
* Sânscrito
* Sérvio (Latino)
* Sindhi
* Sinhala
* Sudanês
* Sueco
* Siriaque
* Tailandês
* Tajique (Cirílico)
* Tamil
* Tatar
* Télego
* Tibetano
* Tigrínia
* Tonganês
* Turco
* Ucraniano
* Uigur
* Urdu
* Usbeque (Latim)
* Vietnamita
* Yiddish
* Yoruba

 
## Tipos de imagens suportados

Este extra suporta os seguintes tipos de ficheiros:
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


[1]: https://github.com/ruifontes/tesseractOCR/releases/download/2023.09.04/tesseractOCR-2023.09.04.nvda-addon
