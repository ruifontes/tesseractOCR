# TesseractOCR


* Автори: Rui Fontes <rui.fontes@tiflotecnia.com> і  Angelo Abrantes <ampa4374@gmail.com>
* Оновлено 13/07/2022
* Завантажити [стабільну версію][1]
* Сумісність: NVDA версія 2019.3 і вище


## Інформація

Цей додаток використовує безкоштовну систему Tesseract OCR з відкритим джерельним кодом для оптичного розпізнавання символів у файлі зображення, PDF, JPG, TIF чи іншому, без необхідності його відкривати.
Він також використовує wia-cmd-сканер, щоб отримати доступ до сканерів із підтримкою WIA та виконати оптичне розпізнавання для паперового документа.
В налаштуваннях NVDA буде створено категорію TesseractOCR, де можна встановити мови, які будуть використовуватися при розпізнаванні, а також типи документів, що розпізнаються.
Також доступний список вибору кількох мов розпізнавання для завантаження та встановлення. Таким чином, тепер додаток надається початково лише з англійською та португальською мовами розпізнавання.
За винятком англійської й португальської мов, які вже включені в додаток, інші мови буде завантажено та встановлено, коли ви виберете мову, якої ще немає в додатку.
Зауважте, що зі збільшенням кількості вибраних мов, процес розпізнавання триватиме довше.
Тому ми рекомендуємо використовувати лише ті мови, які вам потрібні.
Зауважте також, що якість розпізнавання може відрізнятися залежно від порядку мов.
Тому, якщо результат розпізнавання незадовільний, ви можете спробувати інший порядок мов.


## Гарячі клавіші

Початково використовуються такі команди:
Windows+Control+r — для розпізнавання вибраного документа;
Windows+Control+w — для сканування та розпізнавання документа через сканер.

Потім просто зачекайте, поки ocr.txt відкриється з розпізнаним текстом.
Якщо ви хочете зберегти розпізнаний текст, не забудьте зберегти документ під іншим ім'ям та в іншому місці, тому що всі файли в тимчасовому каталозі видаляються на початку наступного оптичного розпізнавання!

Ці команди можна змінити в діалозі «Жести вводу» в розділі «TesseractOCR».


## Автоматичне оновлення
Цей додаток містить функцію автоматичного оновлення.
Перевірка на наявність нової версії буде виконуватися щоразу під час завантаження NVDA.
Якщо ви хочете її увімкнути, перейдіть до меню NVDA, «Параметри», «Налаштування» та поставте прапорець у категорії додатка.



## Відомі проблеми

* У деяких системах можливо, що додаток не працює через помилку comtypes...
На деяких комп’ютерах достатньо перейти до папки temp і видалити папку comtypes_cache.
* При виборі опції «Різне»» у списку "Тип документів" розпізнаний текст, ймовірно, відображається з великою кількістю порожніх рядків.
Це відома проблема з Tesseract, і не витрачаючи багато часу на обробку, автор поки що не знайшов рішення. Але він ще не здався!


## Підтримувані мови

У цій версії підтримуються такі мови:
Африканська
Албанська
Амхарська
Арабська
Вірменська
Ассамська
Азербайджанська (латиниця)
Баскська
Білоруська
Бенгальська
Боснійська
Бретонська
Болгарська
Бірманська
Каталонська/Валенсія
Себуанська
Черокі
Китайська спрощена
Китайська традиційна
Корсиканська
Хорватська
Чеська
Данська
Німецька
Мальдівська
Голланська (фламандська)
Дзонг-ке
Англійська
Есперанто
Естонська
Фарерська
Філіппінська
Фінська
Французька
Галісійська
Грузинська
Грецька
Гуджараті
Гаїтянська
Іврит
Гінді
Угорська
Ісландська
Індонезійська
Інуктитут
Ірландська
Італійська
Яванська
Японська
Каннада
Казахська
Кхмерська (Central)
Киргизька
Корейська
Курдська Kurmanji
Лаоська
Латинська
Латиська
Литовська
Люксембурзька
Македонська
Малайська
Малаялам
Мальтійська
Маорійська
Маратська
Модуль виявлення математики / рівнянь
Монгольська
Непальська
Норвезька
Окситанська
Орія
Пенджабська
Пушту
Перська
Польська
Португальська
Кечуа
Румунська / Молдавська
Російська
Санскрит
Шотландська гельська
Сербська (латиниця)
Словацька
Словенська
Синдхі
Сингальська
Іспанська
Сунданська
Суахілі
Шведська
Сирійська
Таджицька
Тамільська
Татарська
Телугу
Тайська
Тибетська
Тигринья
Тонганська
Турецька
Уйгурська
Українська
Урду
Узбецька (латиниця)
В'єтнамська
Валлійська
Західнофризька
Їдиш
Йоруба



## Підтримувані типи зображень

Цей додаток підтримує такі типи файлів:
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


[1]: https://github.com/ruifontes/tesseractOCR/releases/download/2022.07.13/tesseractOCR-2022.07.13.nvda-addon