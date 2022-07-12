# TesseractOCR


* Auteurs: Rui Fontes <rui.fontes@tiflotecnia.com>, Ângelo Abrantes <ampa4374@gmail.com> y Abel Passos do Nascimento Jr. <abel.passos@gmail.com>
* Mis à jour le 08/07/2022
* Télécharger [version stable][1]
* Compatibilité NVDA: version 2019.3 et ultérieure


## Informations

Cette extension utilise le moteur gratuit et à source ouverte Tesseract OCR pour effectuer une reconnaissance de caractères optiques dans un fichier d'image, PDF, JPG, TIF ou autre type, sans qu'il soit nécessaire de l'ouvrir.
Elle peut également numériser et reconnaître un document papier à partir  d'un scanner compatible WIA.
Dans les Préférences de NVDA, la catégorie TesseractOCR est ajoutée, où vous pouvez configurer les langues à utiliser pendant la reconnaissance et les types de documents à reconnaître.
À l'exception de l'anglais et du portugais, qui sont déjà inclus dans l'extension, les autres langues seront téléchargées et installées lors de la sélection d'une langue qui n'existe toujours pas dans l'extension.
Gardez à l'esprit que à fur et à mesure que le nombre de langues  de reconnaissance sélectionnés augmente, le processus OCR prendra plus de temps.
Par conséquent, nous vous recommandons d'utiliser uniquement les langues dont vous avez besoin.
Gardez également à l'esprit que la qualité de la reconnaissance peut varier en fonction de l'ordre des langues.
Par conséquent, si le résultat de reconnaissance n'est pas satisfaisant, Vous voudrez peut-être prouver un autre ordre dans les langues.


## Commandes clavier

Les commandes clavier par défaut sont:
Windows+Contrôle+r - Pour reconnaître le document sélectionné;
Windows+Contrôle+w - Pour numériser et reconnaître un document à partir du scanner.

Ensuite, attendez que le fichier ocr.txt s'ouvre avec le texte reconnu.
Si vous souhaitez conserver le texte reconnu, n'oubliez pas d'enregistrer le document avec un autre nom et dans un autre endroit, car tous les fichiers du dossier temporaire sont éliminés au début du processus OCR suivant!

Vous pouvez modifier ces commandes dans la boîte de dialogue Gestes de commandes, dans la catégorie "TesseractOCR".


## Mise à jour automatique
Cette extension comprend une fonction de mise à jour automatique.
La vérification d'une nouvelle version sera effectuée chaque fois que NVDA est chargé.
Si vous voulez que cela se produise, aller dans le menu NVDA, Préférences, Paramètres et dans la catégorie de l'extension, cochez la case à cocher.


## Problèmes connus

* Dans certains systèmes, il est possible que l'extension ne fonctionne pas en raison d'une erreur de comtypes...
Dans certaines machines, il suffit d'aller dans le dossier temp et supprimer le dossier comtypes_cache.
* Lors du choix de l'option "Divers" dans la zone de liste déroulante "Type de document", le texte reconnu peut apparaître avec de nombreuses lignes vierges.
Il s'agit d'un problème connu de Tesseract et, sans consommer beaucoup de temps de traitement, je n'ai pas encore trouvé de solution. Mais je n'ai pas encore abandonné!


## Langues supportées

Les langues supportées dans cette version sont:
Afrikaans
Albanais
Amharique
Arabe
Arménien
Assamais
Azerbaïdjanais (Latin)
Basque
Biélorusse
Bengali
Bosniaque
Breton
Bulgare
Burmais
Catalan / Valence
Cébouano
Cherokee
Chinois simplifié
Chinois traditionnel
Corse
Croate
Tchèque
Danois
Allemand
Dhivehi
Néerlandais (Flamand)
Dzongkha
Anglais
Esperanto
Estonien
Féroïen
Philippin
Finnois
Français
Galicien
Géorgien
Grec
Gujarati
Haïtien
Hébreu
Hindi
Hongrois
Islandais
Indonésien
Inuktitut
Irlandais
Italien
Javanais
Japonais
Kannada
Kazakh
Khmère (Central)
Kirghiz
Coréen
Kurde Kurmanji
Laotien
Latin
Letton
Lituanien
Luxembourgeois
Macédonien
Malais
Malayalam
Maltais
Maori
Marathi
Équations mathématiques
Mongol
Népalais
Norvégien
Occitan
Oriya
Panjabi
Pashto
Persan
Polonais
Portugais
Quechua
Roumain / Moldave
Russe
Sanskrit
Gaélique écossais
Serbe (Latin)
Slovaque
Slovène
Sindhi
Cingalais
Espagnol
Sundanais
Swahili
Suédois
Syriaque
Tajik
Tamil
Tatar
Telugu
Thaï
Tibetan
Tigrinya
Tongan
Turc
Ouïgour
Ukrainien
Ourdou
Ouzbek (Latin)
Vietnamien
Gallois
Frison Ouest
Yiddish
Yoruba


## Types d'images supportées

Cette extension supporte les types de fichiers suivants:
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


[1]: https://github.com/ruifontes/tesseractOCR/releases/download/2022.07/tesseractOCR-2022.07.nvda-addon
