# Eye Detection

![App Screenshot](https://github.com/firengizz099/eyedetection/blob/main/1_tJPP3eRByPdZSNsDftreMw.jpg?raw=true)

**Python 3.x
OpenCV kütüphanesi (pip install opencv-python)
RawPy kütüphanesi (pip install rawpy)
Kullanım**

eye_cascade ve face_cascade nesneleri, göz ve yüz tespiti için OpenCV'nin önceden eğitilmiş XML dosyalarını kullanır.
folder_path, işlenecek resimlerin bulunduğu dizini belirtir
İşlenmiş resimlerin kaydedileceği result_folder oluşturulur.
İşlenecek resim dosyaları image_files listesine eklenir.

Her resim dosyası için şu adımlar gerçekleştirilir:
Dosya yolu ve uzantısı alınır.
-.cr2 uzantısına sahipse, RawPy ile işlenir ve OpenCV'ye dönüştürülür.
-.jpg veya .jpeg uzantısına sahipse, doğrudan OpenCV ile yüklenir.
Yüz tespiti için face_cascade kullanılır ve yüzler belirlenir.
Her yüzün içinde, göz tespiti için eye_cascade kullanılır.
Tespit edilen gözler çizimlerle işaretlenir.
İşlenmiş resim, result_folder altında kaydedilir.
İşlem tamamlandığında, sonuçlar görüntülenir.

# Not
Eğer resim .cr2 uzantısına sahipse, RawPy kütüphanesi ile işlenir ve OpenCV formatına dönüştürülür.
Eğer resim .jpg veya .jpeg uzantısına sahipse, doğrudan OpenCV ile yüklenir.
Göz ve yüz tespiti için OpenCV'nin önceden eğitilmiş XML dosyaları kullanılır.
**İşlenen resimlerin sonuçları, result_folder altında kaydedilir.**
