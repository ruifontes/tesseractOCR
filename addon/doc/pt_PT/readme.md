# TesseractOCR


* Autores: Rui Fontes, Ângelo Abrantes e Abel Passos do Nascimento Jr.
* Actualizado em 25/02/2024
* Descarregar [versão estável][1]
Compatibilidade: NVDA versão 2019.3 e posteriores


## Informações

Este extra utiliza o motor de OCR Tesseract, de código aberto e gratuito, para executar o reconhecimento óptico de caracteres a um documento de imagem, seja PDF, JPG, TIF ou outro, sem necessidade de abrir o documento.
Também permite o acesso a scanners compatíveis WIA para efectuar OCR a um documento em papel.
Por último, pode obter o texto de um PDF acessível e mostrá-lo no Bloco de notas.
No menu NVDA, Preferências, é adicionada uma secção TesseractOCR, onde pode configurar o seguinte:
- Idiomas a utilizar no reconhecimento;
- o tipo de documentos a reconhecer;
- se deve ou não ser pedida uma palavra-passe para o PDF. Se esta opção estiver seleccionada e o PDF não tiver uma palavra-passe, basta premir Enter na caixa de diálogo que pede a palavra-passe;
- Seleccionar o scanner a ser utilizado;
- definir a resolução do scanner entre 150 e 400PPP .

À excepção dos idiomas português e inglês, que já são incluidos no extra, os restantes idiomas serão descarregados e instalados quando for seleccionado um idioma que ainda não exista no extra.
Note que à medida que aumenta o número de idiomas de reconhecimento seleccionados, o processo de OCR será mais longo.
Por isso, recomendamos a utilização apenas dos idiomas necessários.
Note também que a qualidade do reconhecimento pode variar de acordo com a ordem dos idiomas.
Por conseguinte, se o resultado do reconhecimento não for satisfatório, pode tentar outra ordenação.


## Comandos

Os comandos predefinidos são:
Windows+Control+w - Para digitalizar e reconhecer um documento através do scanner;
Windows+Control+r - Para reconhecer o ficheiro seleccionado;
Windows+Control+t - Para obter o texto de um PDF acessível.
Windows+Control+c - Para cancelar o processo de digitalização.
Nota: Tem de ser executado antes de aparecer a caixa de diálogo que pergunta se pretende digitalizar mais páginas!

Depois é só esperar que o ficheiro ocr.txt apareça com o texto reconhecido.
Se pretender preservar o texto reconhecido, não se esqueça de guardar o documento com outro nome e noutro local, pois todos os ficheiros da pasta temporária são eliminados no início do próximo processo de OCR!

Estes comandos podem ser modificados na caixa de diálogo \"Definir comandos\" na secção \"TesseractOCR\".


## Problemas conhecidos

* Quando se selecciona a opção \"Documentos variados\" na caixa combinada \"Tipo de documento\", é provável que o texto reconhecido fique com demasiadas linhas em branco
Este é um problema conhecido do Tesseract e, sem consumir muito tempo de processamento, ainda não encontrámos nenhuma solução. Mas, ainda assim, não desistimos!


## Idiomas suportados
Os idiomas suportados nesta versão são:
* Africânder
* Albanês
* Amárico
* Árabe
* Arménio
* Assamês
* Azerbaijano (Latim)
* Basco
* Bielorrusso
* Bengalês
* Bósnio
* Bretão
* Búlgaro
* Burnês
* Catalão/Valenciano
* Cebuano
* Cheroqui
* Chinês simplificado
* Chinês tradicional
* Corso
* Croata
* Checo
* Dinamarquês
* Alemão
* Dhivehi
* Neerlandês (flamengo)
* Dzongkha
* Inglês
* Esperanto
* Estónio
* Faroês
* Filipino
* Finlandês
* Francês
* Galego
* Georgiano
* Grego
* Guzarate
* Haitiano
* Hebraico
* Hindi
* Húngaro
* Islandês
* Indonésio
* Inuktitut
* Irlandês
* Italiano
* Javanês
* Japonês
* Kannada
* Cazaque
* Khmer (Central)
* Quirguizistanês
* Coreano
* Curdo Kurmanji
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
* Equações matemáticas
* Mongol
* Nepalês
* Norueguês
* Occitano
* Oriya
* Panjabi
* Afegão
* Persa
* Polaco
* Português
* Quíchua
* Romeno/Moldavo
* Russo
* Sânscrito
* Gaélico escocês
* Sérvio (Latim)
* Eslovaco
* Esloveno
* Sindi
* Cingalês
* Espanhol
* Sundanês
* Swahili
* Sueco
* Siríaco
* Tajique
* Tamil
* Tártaro
* Telugu
* Tailandês
* Tibetano
* Tigrínia
Tonganês
* Turco
* Uigur
* Ucraniano
* Urdu 
* Uzbeque (Latim)
* Vietnamita
* Galês
* Frísico Ocidental
* Iídiche
* Iorubá


## Tipos de imagem suportados

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

[1]: https://github.com/ruifontes/tesseractOCR/releases/download/2024.02.25/tesseractOCR-2024.02.25.nvda-addon
