# TesseractOCR


* Autoren: Rui Fontes, Ângelo Abrantes und Abel Passos do Nascimento Jr.
* Aktualisiert am 12.11.2023
* Laden Sie die [stabile Version][1] herunter
* Kompatibilität: NVDA-Version 2019.3 und höher


## Informationen

Dieses Add-on verwendet die kostenlose und Open-Source-OCR-Engine Tesseract, um eine optische Zeichenerkennung für eine Bilddatei, PDF, JPG, TIF oder andere durchzuführen, ohne sie öffnen zu müssen.
Es verwendet auch wia-cmd-scanner, um auf WIA-fähige Scanner zuzugreifen und OCR für ein Papierdokument durchzuführen.
Im NVDA-Menü, Einstellungen, wird ein Abschnitt TesseractOCR hinzugefügt, in dem Sie die für die Erkennung zu verwendenden Sprachen und die Art der zu erkennenden Dokumente konfigurieren können.
In diesem Dialog können Sie, um OCR an passwortgeschützten PDF-Dateien durchführen zu können, markieren, dass Sie nach einem Passwort gefragt werden.
Wenn Sie diese Option aktiviert haben und das PDF kein Passwort hat, drücken Sie einfach die Eingabetaste im Dialogfeld, in dem Sie nach dem Passwort gefragt werden.
Mit Ausnahme von Englisch und Portugiesisch, die bereits im Add-on enthalten sind, werden die anderen Sprachen heruntergeladen und installiert, wenn Sie eine Sprache auswählen, die noch nicht im Add-on vorhanden ist.
Beachten Sie, dass der OCR-Vorgang mit zunehmender Anzahl ausgewählter Erkennungssprachen länger dauert.
Wir empfehlen daher, nur die Sprachen zu verwenden, die Sie benötigen.
Beachten Sie auch, dass die Qualität der Erkennung je nach Reihenfolge der Sprachen variieren kann.
Wenn das Erkennungsergebnis nicht zufriedenstellend ist, sollten Sie es daher mit einer anderen Sprachreihenfolge versuchen.


## Abkürzung

Die Standardbefehle sind:
Windows+Strg+r - um das ausgewählte Dokument zu erkennen;
Windows+Strg+w - zum Scannen und Erkennen eines Dokuments über den WIA-Scanner.

Warten Sie dann einfach, bis sich ocr.pdf mit dem erkannten Text öffnet.
Wenn Sie den erkannten Text erhalten möchten, vergessen Sie nicht, das Dokument unter einem anderen Namen und an einem anderen Ort zu speichern, da alle Dateien im temporären Verzeichnis beim Start des nächsten OCR-Vorgangs gelöscht werden!

Diese Befehle können im Dialog "Eingabegesten" im Abschnitt "TesseractOCR" geändert werden.


## Bekannte Probleme

* In einigen Systemen ist es möglich, dass Add-Ons aufgrund eines Comtypes-Fehlers nicht funktionieren ...
Auf manchen Rechnern reicht es aus, in den temporären Ordner zu gehen und den Ordner comtypes_cache zu löschen.
* Bei Auswahl der Option „Verschiedene“ in der Combobox „Dokumententyp“ erscheint der erkannte Text wahrscheinlich mit vielen Leerzeilen
Dies ist ein bekanntes Problem mit Tesseract, und ohne viel Verarbeitungszeit zu verbrauchen, habe ich noch keine Lösung gefunden. Aber ich habe immer noch nicht aufgegeben!


## Unterstützte Sprachen

Die unterstützten Sprachen in dieser Version sind:* Afrikaner
* Albanisch
* Amharik
* Arabisch
* Armenisch
* Assamesisch
* Aserbaidschanisch (Latein)
* Baskisch
* Belarussisch
* Bengalisch
* Bosnisch
* Bretonisch
* Bulgarisch
* Burnesisch
* Katalanisch/Valencianisch
* Cebuano
* Cherokee
* Vereinfachtes Chinesisch
* Chinesische Tradition
* Korsisch
* Kroatisch
* Tschechisch
* Dannisch
* Deutsch
* Divehi
* Niederländisch (Flämisch)
* Dzongkha
* Englisch
* Esperanto
* Estnisch
* Färöisch
* Philippinisch
* Finnisch
* Französisch
* Galizisch
* Georgisch
* Griechisch
* Gujarati
* Haitianisch
* Hebräisch
* Hindi
* Ungarisch
* Isländisch
* Indonesisch
* Inuktitut
* Irisch
* Italienisch
* Javanisch
* Japanisch
* Kanada
* Kasachisch
* Khmer (Zentral)
* Kirgisen
* Koreanisch
* Kurdisches Kurmandschi
* Lao
* Latein
* Lettland
* Litauisch
* Luxemburgisch
* Mazedonisch
* Malaiisch
* Malayalam
* Maltesisch
* Maori
* Marathi
* Math / Gleichungserkennungsmodul
* Mongolisch
* Nepali
* Norwegisch
* Okzitanisch
* Orija
* Pandschabi
* Paschtu
* Persisch
* Polieren
* Portugiesisch
* Quechua
* Rumänisch/Moldave
* Russisch
* Sanskrit
* Schottisch Gälisch
* Serbisch (Latein)
* Slowakisch)
* Slowenisch)
* Sindhi
* Singhalesisch
* Spanisch
* Sundanesisch
* Suaheli
* Schwedisch
* Syrisch
* Tadschikisch
* Tamilisch
* Tatarisch
* Telugu
* Thailändisch
* Tibetisch
* Tigrinja
* Tonga
* Türkisch
* Uiguren
* Ukrainisch
* Urdu
* Usbekisch (Latein)
* Vietnamesisch
* Walisisch
* Westfriesisch
* Jiddisch
* Yoruba


## Unterstützte Bildtypen

Dieses Add-On unterstützt die folgenden Dateitypen:
* Pdf
* jpg
* tif
* png
* bmp
* pnm
* pbm
* pgm
* jp2
* Gif
* jfif
* JPEG
* tiff
* spix
* webp

[1]: https://github.com/ruifontes/tesseractOCR/releases/download/2023.11.12/tesseractOCR-2023.11.12.nvda-addon
