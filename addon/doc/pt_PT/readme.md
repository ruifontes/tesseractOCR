# TesseractOCR

* Autores: Rui Fontes <rui.fontes@tiflotecnia.com>, Ângelo Abrantes <ampa4374@gmail.com> e Abel Passos do Nascimento Jr. <abel.passos@gmail.com>
* Actualizado em 28/05/2022
* Descarregar a [versão estável][1]
* Compatibilidade: NVDA 2019.3 e seguintes


## Informações

Este extra utiliza o motor de OCR Tesseract, de código aberto e gratuito, para executar o reconhecimento óptico de caracteres a um documento de imagem, seja PDF, JPG, TIF ou outro, sem necessidade de abrir o documento.
Também pode digitalizar e reconhecer um documento em papel através do scanner.
No menu do NVDA, Preferências é adicionada uma secção TesseractOCR, onde poderá configurar o idioma a utilizar no reconhecimento e o tipo de documentos a reconhecer.

## Comandos

Os comandos predefinidos são:
Windows+Control+r - Para reconhecer o ficheiro seleccionado;
Windows+Control+Shift+r - Para digitalizar e reconhecer um documento através do scanner.

Depois é só esperar que se abra o ficheiro ocr.txt.
Se pretender preservar o texto reconhecido, não se esqueça de guardar o documento com outro nome e noutro local, pois todos os ficheiros da pasta temporária são eliminados no início do próximo processo de OCR!


## Problemas conhecidos

* Esta versão apenas funciona em sistemas de 64-bits.
* Quando se selecciona a opção "Documentos variados" na caixa combinada "Tipo de documento", é provável que o texto reconhecido fique com demasiadas linhas em branco.


## Idiomas suportados

Os idiomas suportados nesta versão são:
Africânder
Alemão
Amárico
Árabe
búlgaro
Burnês
Canarim
Castelhano (Espanhol)
Catalão/Valenciano
Checo
Chinês simplificado
Chinês tradicional
Coreano
Croata
Dinamarquês
Eslovaco
Esloveno
Finlandês
Francês
Galego
Georgiano
Grego
Hebreu
Hindi
Húngaro
Indonésio
Inglês
Irlandês
Islandês
Italiano
Japonês
Letão
Lituano
Macedónio
Neerlandês
Nepalês 
Norueguês
Persa
Polaco
Português
Punjabi
Quirguize
Romeno / Moldavo
Russo
Sérvio (Latino)
Sueco
Tailandês
Tamil
Turco
Ucraniano
Urdu 
Vietnamês

 
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


[1]: https://github.com/ruifontes/tesseractOCR/releases/download/2022.05/tesseractOCR-2022.05.nvda-addon
