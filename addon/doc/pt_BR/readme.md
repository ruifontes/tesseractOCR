# TesseractOCR


* Autores: Rui Fontes <rui.fontes@tiflotecnia.com>, Ângelo Abrantes <ampa4374@gmail.com> e Abel Passos do Nascimento Jr. <abel.passos@gmail.com>
* Actualizado em 26/06/2022
* Descarregar a [versão estável][1]
* Compatibilidade: NVDA 2019.3 e seguintes


## Informações

Este extra utiliza o motor de OCR Tesseract, de código aberto e gratuito, para executar o reconhecimento óptico de caracteres a um documento de imagem, seja PDF, JPG, TIF ou outro, sem necessidade de abrir o documento.
Também usa o módulo wia-cmd-scanner para aceder a scanners compatíveis WIA para digitalizar e reconhecer um documento em papel.
No menu do NVDA, Preferências é adicionada uma secção TesseractOCR, onde poderá configurar o primeiro e segundo idioma a utilizar no reconhecimento e o tipo de documentos a reconhecer.
Está também disponível uma caixa comvinada para seleccionar mais idiomas de reconhecimento para descarregar e instalar no extra. Assim, o extra é agora distribuido apenas com os idiomas de reconhecimento em português e inglês.
Note que a utilização de dois idiomas de reconhecimento torna o processo de OCR um pouco mais lento. Por isso, está disponível um botão para esquecer o segundo idioma. Note também que a qualidade do reconhecimento pode variar de acordo com a ordem dos idiomas.



## Comandos

Os comandos predefinidos são:
Windows+Control+r - Para reconhecer o ficheiro seleccionado;
Windows+Control+Shift+r - Para digitalizar e reconhecer um documento através do scanner.

Depois é só esperar que se abra o ficheiro ocr.txt.
Se pretender preservar o texto reconhecido, não se esqueça de guardar o documento com outro nome e noutro local, pois todos os ficheiros da pasta temporária são eliminados no início do próximo processo de OCR!


## Problemas conhecidos

* Quando se selecciona a opção "Documentos variados" na caixa combinada "Tipo de documento", é provável que o texto reconhecido fique com demasiadas linhas em branco.


## Idiomas suportados

Os idiomas suportados nesta versão são:
Africânder
Albanês
Alemão
Amárico
Árabe
Arménio
Assamês
Azerbaijanês (Latim)
Bangla
Basco
Belarrusso
Bósnio (Latim)
Bretão
búlgaro
Burnês
Canarim
Catalão/Valenciano
Cazaquistanês
Cebuano
Checo
Cheroqui
Chinês simplificado
Chinês tradicional
Coreano
Corso
Croata
Curdo Central
Dinamarquês
Divehi
Dzongkha
Equações matemáticas
Eslovaco
Esloveno
Espanhol
Esperanto
Estónio
Feroês
Filipino
Finlandês
Francês
Frísico Ocidental
Galego
Galês
Galês da Escócia
Georgiano
Grego
Guzarate
Haitian
Hebraico
Hindi
Húngaro
Indonésio
Inglês
Inuktitut (Latim)
Irlandês
Islandês
Italiano
Javanês
Japonês
Kiswahili
Kurdo do norte
Laosiano
Latim
Letão
Lituano
Luxemburguês
Macedónio
Malaio
Malayalam
Maltês
Maori
Marati
Mongol
Neerlandês
Nepalês 
Norueguês
Ocitano
Odia
Pastó
Persa
Polaco
Português
Punjabi
Quechua
Quirguize
Romeno / Moldavo
Russo
Sânscrito
Sérvio (Latino)
Sindhi
Sinhala
Sudanês
Sueco
Siriaque
Tailandês
Tajique (Cirílico)
Tamil
Tatar
Télego
Tibetano
Tigrínia
Tonganês
Turco
Ucraniano
Uigur
Urdu
Usbeque (Latim)
Vietnamita
Yiddish
Yoruba

 
## Tipos de imagens suportados

Este extra suporta os seguintes tipos de ficheiros:
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
