# TesseractOCR


* Yazarlar: Rui Fontes <rui.fontes@tiflotecnia.com> and  Angelo Abrantes <ampa4374@gmail.com>
* 13/07/2022'de güncellendi
* [Kararlı sürümü indirin][1]
* Uyumluluk: NVDA sürüm 2019.3 ve sonrası


## bilgiler:

Bu eklenti, bir görüntü dosyası, PDF, JPG, TIF veya diğerleri üzerinde açmaya gerek kalmadan optik karakter tanıma gerçekleştirmek için ücretsiz ve açık kaynaklı Tesseract OCR motorunu kullanır.  
Ayrıca, WIA özellikli tarayıcılara erişebilmek ve bir kağıt belgeye OCR yapabilmek için wia-cmd-Tarayıcı'sı kullanır.  
NVDA menüsü, Tercihler, Ayarlar içerisinde tanımada kullanılacak dilleri ve tanınacak belge türlerini yapılandırabileceğiniz bir TesseractOCR bölümü eklenmiştir.  
Eklentide zaten bulunan İngilizce ve Portekizce dışında, mevcut olmayan bir dili seçtiğinizde diller indirilir ve kurulur.  
Seçilen tanıma dillerinin sayısı arttıkça OCR işleminin daha uzun süreceğini unutmayın.  
Bu nedenle, yalnızca ihtiyacınız olan dilleri kullanmanızı öneririz.  
Ayrıca tanıma kalitesinin dillerin sırasına göre değişebileceğini unutmayın.  
Bu nedenle, tanıma sonucu tatmin edici değilse, başka bir dil sıralaması denemek isteyebilirsiniz.  


## Kısayollar:

Varsayılan komutlar şunlardır:  
Windows+Control+r - seçilen belgeyi tanımak için;  
Windows+Control+w - tarayıcı aracılığıyla bir belgeyi taramak ve OCR yapmak için.  

Ardından, tanınan metinle ocr.txt dosyasının açılmasını bekleyin.  
Tanınan metni korumak istiyorsanız, geçici dizindeki tüm dosyalar bir sonraki OCR işleminin başlangıcında silineceğinden, belgeyi başka bir ad altında ve başka bir konuma kaydetmeyi unutmayın!  

Bu komutlar, "Girdi hareketleri" "TesseractOCR" bölümündeki  iletişim kutusunda değiştirilebilir.  


## Otomatik güncelleme:

Bu eklenti bir otomatik güncelleme özelliği içerir.  
NVDA her açıldığında yeni bir sürüm kontrolü gerçekleştirilecektir.  
Bunu istiyorsanız, NVDA, Tercihler, Ayarlar'a gidin ve eklenti kategorisinde onay kutusunu işaretleyin.  


## Bilinen sorunlar:

* Bazı sistemlerde, bir comtypes hatası nedeniyle eklentinin çalışmaması mümkündür...
Bazı makinelerde temp klasörüne gitmek ve comtypes_cache klasörünü silmek yeterlidir.
* "Belge türü" açılır kutusunda "Çeşitli" seçeneği seçildiğinde, tanınan metin muhtemelen birçok boş satırla görünür.
Bu Tesseract ile ilgili bilinen bir sorundur ve çok fazla işlem süresi tüketmeden henüz bir çözüm bulamadım. Ama yine de vazgeçmedim!


## Desteklenen diller:

Bu sürümde desteklenen diller şunlardır:
Afrikaner dili,  
Arnavutça,  
Amharca,  
Arapça,  
Ermenice,  
Assam dili,  
Azerice (Latin),  
Bask dili,  
belarusça,  
Bengalce,  
Boşnakça,  
Bretonca,  
Bulgarca,  
Burnese,  
Katalanca/Valensiyaca,  
Cebuano,  
Cherokee,  
Çince basitleştirilmiş,  
Çince geleneksel,  
Korsikaca,  
Hırvatça,  
Çekçe,  
Danimarkaca,  
Almanca,  
Dhivehi,  
Hollandaca (Flamanca),  
Dzongkha,  
İngilizce,  
Esperanto,  
estonyaca,  
Faroe dili,  
Filipin dili,  
Fince,  
Fransızca,  
Galiçyaca,  
Gürcüce,  
Yunanca,  
Gujarati,  
Haiti,  
İbranice,  
Hintçe,  
Macarca,  
İzlandaca,  
Endonezya dili,  
İnuitçe,  
İrlandaca,  
İtalyanca,  
Cava,  
Japonca,  
Kannada,  
Kazakça,  
Khmer (Merkezi),  
Kırgızca,  
Korece,  
Kürtçe Kurmanci,  
Lao,  
Latince,  
Letonyaca,  
litvanyaca,  
Lüksemburgca,  
Makedonca,  
Malayca,  
Malayalamca,  
Maltaca,  
Maori,  
Marathi,  
Matematik / denklem algılama modülü,  
Moğolca,  
Nepalce,  
Norveççe,  
Oksitanca,  
Ortaca,  
Panjabi,  
Peştuca,  
Farsça,  
Lehçe,  
Portekizce,  
Keçua,  
Rumence / Moldavya,  
Rusça
Sanskritçe,  
İskoç Galcesi,  
Sırpça (Latin),  
Slovakça),  
Slovence),  
Sindhi,  
Sinhalese,  
İspanyolca,  
Sunda dili,  
Swahili,  
İsveççe,  
Süryanice,  
Tacik,  
Tamilce,  
Tatarca,  
Telugu,  
Tay,  
Tibetçe,  
Tigrinya,  
Tonga,  
Türkçe,  
Uygurca,  
Ukraynaca,  
Urduca,  
Özbekçe (Latin),  
Vietnamca,  
Galce,  
Batı Frizcesi,  
Yidiş,  
Yoruba.  


## Desteklenen resim türleri:

Bu eklenti aşağıdaki dosya türlerini destekler:
PDF,  
jpg,  
tif,  
png,  
bmp,  
pnm,  
pbm,  
pgm,  
jp2,  
gif,  
jfif,  
jpeg,  
tiff,  
spix,  
webp,  


[1]: https://github.com/ruifontes/tesseractOCR/releases/download/2022.07.13/tesseractOCR-2022.07.13.nvda-addon
