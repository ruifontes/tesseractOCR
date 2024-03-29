# TesseractOCR

TesseractOCR: Дополнение для распознавания текста.

* Авторы: Rui Fontes, Ângelo Abrantes и Abel Passos do Nascimento Jr.
* Скачать [стабильную версию][1]
* Совместимость: NVDA версии 2019.3 и новее
* [Страница дополнения на GitHub](https://github.com/ruifontes/tesseractOCR)


### Информация

Это дополнение использует бесплатный OCR-движок Tesseract с открытым исходным кодом для оптического распознавания символов на файле изображения, PDF, JPG, TIF или другом, без необходимости его открытия.
Оно также может сканировать и распознавать бумажные документы с помощью сканера, совместимого с WIA.
Finally, it also can get the accessible text from an accessible PDF.
В настройках NVDA создана категория TesseractOCR, где можно задать язык, который будет использоваться при распознавании, тип распознаваемых документов и возможность импортировать больше файлов с языками распознавания.
Чтобы не перегружать дополнение, мы включили в него только файлы языков распознавания на английском и португальском языках.


### Клавиатурные команды

По умолчанию используются следующие команды:

* Windows+Control+r - распознать выбранный документ;
Windows+Control+w - для сканирования и распознавания документа через сканер.
Windows+Control+t - To get the text from an accessible PDF;
Windows+Control+c - To cancel the scanning process.
Please note: It must be issued before the dialog asking if you want to scan more pages appear!

Затем просто подождите, пока откроется файл ocr.txt с распознанным текстом.
Если вы хотите сохранить распознанный текст, не забудьте сохранить документ под другим именем и в другом месте, так как все файлы во временном каталоге удаляются при запуске следующего процесса OCR!

Эти команды можно изменить в диалоге "Жесты ввода" в разделе "TesseractOCR".


### Известные проблемы

* Эта версия работает только в 64-битных Windows.
* При выборе опции "Разные" в окне "Тип документов" распознанный текст может отображаться с большим количеством пустых строк.
Это известная проблема Tesseract, и, не затрачивая много времени на обработку, я пока не нашел никакого решения. Но я все еще не сдался!

### Поддерживаемые языки распознания

В этой версии поддерживаются следующие языки:

* Африка́анс
* Амхарский
* Арабский
* Болгарский
* Бурнес
* Каталонский/валенсийский
* Китайский упрощенный
* Китайский традиционный
* Хорватский
* Чешский
* Датский
* Немецкий
* Голландский
* Английский
* Финский
* Французский
* Галисийский
* Грузинский
* Греческий
* Иврит
* Хинди
* Венгерский
* Исландский
* Индонезийский
* Ирландский
* Итальянский
* Японский
* Каннада
* Киргизский
* Корейский
* Латышский
* Литовский
* Македонский
* Непальский
* Норвежский
* Панджаби
* Персидский
* Польский
* Португальский
* Румынский/молдавский
* Русский
* Сербский (латинский)
* Словацкий)
* Словенский)
* Испанский
* Шведский
* Тамильский
* Тайский
* Турецкий
* Украинский
* Урду 
* Вьетнамский
 
### Поддерживаемые типы изображений

Это дополнение поддерживает следующие типы файлов:

* PDF
* JPG
* TIF
* PNG
* BMP
* PNM
* PBM
* PGM
* JP2
* GIF
* JFIF
* JPEG
* TIFF
* SPIX
* WEBP


### Перевод

* Русский язык: Валентин Куприянов.


[1]: https://github.com/ruifontes/tesseractOCR/releases/download/2024.03.24/tesseractOCR-2024.03.24.nvda-addon
