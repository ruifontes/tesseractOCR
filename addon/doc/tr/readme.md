# TesseractOCR


* Yazarlar: Rui Fontes, Ângelo Abrantes and Abel Passos do Nascimento Jr.
* 22/07/2023'de güncellendi
* [Kararlı sürümü indirin][1]
* Uyumluluk: NVDA sürüm 2019.3 ve sonrası


## bilgiler:

Bu eklenti, bir görüntü dosyası, PDF, JPG, TIF veya diğerleri üzerinde açmaya gerek kalmadan optik karakter tanıma gerçekleştirmek için ücretsiz ve açık kaynaklı Tesseract OCR motorunu kullanır.  
Ayrıca, WIA özellikli tarayıcılara erişebilmek ve bir kağıt belgeye OCR yapabilmek için wia-cmd-Tarayıcı'sı kullanır.  
NVDA menüsü, Tercihler, Ayarlar içerisinde tanımada kullanılacak dilleri ve tanınacak belge türlerini yapılandırabileceğiniz bir TesseractOCR bölümü eklenmiştir.  
Bu iletişim kutusunda, parola korumalı PDF dosyalarına OCR yapabilmek için parola sorulmasını işaretleyebilirsiniz.  
Bu seçeneği işaretlediyseniz ve PDF'nin bir parolası yoksa, parola soran iletişim kutusunda Enter'a basmanız yeterlidir.  
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
* Afrikaner Dili
* Arnavutça
* Amharca
* Arapça
* Ermenice
* Assam dili
* Azerice (Latin)
* Bask
* Belarusça
* Bengalce
* Boşnakça
* Bretonca
* Bulgarca
* Burnese
* Katalanca/Valensiya Dili
* Cebuano
* Çeroki
* Çince Basitleştirilmiş
* Çince Geleneksel
* Korsika dili
* Hırvatça
* Çekçe
* Danca
* Almanca
* Dhivehi
* Felemenkçe (Flamanca)
* Dzongkha
* İngilizce
* Esperanto
* Estonyaca
* Faroece
* Filipince
* Fince
* Fransızca
* Galiçyaca
* Gürcüce
* Yunanca
* Gujarati
* Haitice
* İbranice
* Hintçe
* Macarca
* İzlandaca
* Endonezya dili
* İnuitçe
* İrlandaca
* İtalyanca
* Cava dili
* Japonca
* Kannada
* Kazakça
* Khmer (Merkezi)
* Kırgızca
* Korece
* Kürtçe Kurmanci
* Lao
* Latince
* Letonya
* Litvanyaca
* Lüksemburgca
* makedonca
* Malayca
* Malayalam
* Malta
* Maori
* Marathi
* Matematik / denklem algılama modülü
* Moğolca
* Nepalce
* Norveççe
* Oksitanca
* Ortaca
* panjabi
* Peştuca
* Farsça
* Lehçe
* Portekizce
* keçuva
* Romence/Moldavca
* Rusça
* Sanskritçe
* İskoç Galcesi
* Sırpça (Latin)
* Slovakça
* Slovence)
* Sintçe
* Sinhalese
* İspanyolca
* Sundan dili
* Svahili
* İsveççe
* Süryanice
* Tacikçe
* Tamilce
* Tatarca
* Telugu
* Taylandça
* Tibet dili
* Tigrinya
* Tonga
* Türkçe
* Uygurca
* Ukraynaca
* Urduca
* Özbekçe (Latin)
* Vietnamca
* Galce
* Batı Frizce
* Yidiş
* Yoruba


## Desteklenen resim türleri:

Bu eklenti aşağıdaki dosya türlerini destekler:
* PDF,  
* jpg,  
* tif,  
* png,  
* bmp,  
* pnm,  
* pbm,  
* pgm,  
* jp2,  
* gif,  
* jfif,  
* jpeg,  
* tiff,  
* spix,  
* webp,  


[1]: https://github.com/ruifontes/tesseractOCR/releases/download/2023.07.22/tesseractOCR-2023.07.22.nvda-addon
