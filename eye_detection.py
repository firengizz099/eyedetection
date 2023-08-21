"""import os
import cv2
import rawpy
import uuid

# Cascade sınıflandırıcıları indirin (Haar Cascade Classifier)
eye_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_eye.xml')
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

# Klasör yolunu belirleyin
folder_path = '/home/firengiz/Belgeler/proje_eye_detection/goz_resimleri'

# "result" klasörünü oluşturun
result_folder = os.path.join(folder_path, 'result')
os.makedirs(result_folder, exist_ok=True)

# Klasördeki tüm dosyaları alın (sadece .jpg, .jpeg ve .cr2 uzantılı dosyaları alın)
image_files = [f for f in os.listdir(folder_path) if os.path.isfile(os.path.join(folder_path, f)) and f.lower().endswith(('.jpg', '.jpeg', '.cr2'))]

# Sözlük oluşturunuz.
processed_files = {}

for image_file in image_files:
    image_path = os.path.join(folder_path, image_file)
    image_extension = os.path.splitext(image_file)[1].lower()

    print(f"Resim dosya yolu: {image_path}")
    print(f"Resim dosya uzantısı: {image_extension}")

    if image_extension == '.cr2':
        # Canon RAW dosyasını rawpy ile yükleyin ve OpenCV'ye dönüştürün
        with rawpy.imread(image_path) as raw:
            rgb = raw.postprocess()
        image = cv2.cvtColor(rgb, cv2.COLOR_RGB2BGR)
        
    elif image_extension == '.jpg' or image_extension == '.jpeg':
        # .jpg uzantılı dosyaları olduğu gibi kaydedin
        image = cv2.imread(image_path)
        
    else:
        print(f"Geçersiz dosya uzantısı: {image_file}")
        continue

    if image is None:
        print(f"Resim yüklenemedi: {image_file}")
        continue

    # Resmi 640x640 piksel boyutuna dönüştürün
    resized_image = cv2.resize(image, (640, 640))

    gray_image = cv2.cvtColor(resized_image, cv2.COLOR_BGR2GRAY)

    # Yüzleri tespit etmek için Haar sınıflandırıcısını kullanın
    faces = face_cascade.detectMultiScale(gray_image, scaleFactor=1.3, minNeighbors=5, minSize=(30, 30))
    print("Tespit edilen goz sayısı:", len(faces))

    # Her yüz için gözleri tespit edin ve dikdörtgenlerle çevreleyin
    for (x, y, w, h) in faces:
        face_roi = gray_image[y:y+h, x:x+w]
        eyes = eye_cascade.detectMultiScale(face_roi)
        for (ex, ey, ew, eh) in eyes:
            cv2.rectangle(resized_image, (x+ex, y+ey), (x+ex+ew, y+ey+eh), (0, 255, 0), 2)

    # Dosya adını kontrol edin ve eğer aynı dosya adı başka bir resimde varsa değiştirin
    base_filename = os.path.splitext(image_file)[0]
    count = processed_files.get(base_filename, 0)
    processed_files[base_filename] = count + 1

    if count > 0:
        # Dosya adını değiştirin (örn: IMG_0358_2.JPG, IMG_0358_3.JPG, vb.)
        unique_filename = f"{base_filename}_{count}"
    else:
        unique_filename = base_filename

    # Sonuçları kaydedin (dosya uzantısını .jpg olarak değiştirin)
    result_path = os.path.join(result_folder, 'result_' + unique_filename + '.jpg')
    cv2.imwrite(result_path, resized_image)

print("İşlem tamamlandı.")
"""

import cv2
import os
import rawpy

eye_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_eye.xml')
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
folder_path = '/home/firengiz/Belgeler/proje_eye_detection/goz_resimleri'

result_folder = os.path.join(folder_path, 'result')
os.makedirs(result_folder, exist_ok=True)
image_files = [f for f in os.listdir(folder_path) if os.path.isfile(os.path.join(folder_path, f)) and f.lower().endswith(('.jpg', '.jpeg', '.cr2'))]
processed_files = {}

for image_file in image_files:
    image_path = os.path.join(folder_path, image_file)
    image_extension = os.path.splitext(image_file)[1].lower()

    print(f"Resim dosya yolu: {image_path}")
    print(f"Resim dosya uzantısı: {image_extension}")

    if image_extension == '.cr2':
        with rawpy.imread(image_path) as raw:
            rgb = raw.postprocess()
        image = cv2.cvtColor(rgb, cv2.COLOR_RGB2BGR)

    elif image_extension == '.jpg' or image_extension == '.jpeg':
        image = cv2.imread(image_path)

    else:
        print(f"Geçersiz dosya uzantısı: {image_file}")
        continue

    if image is None:
        print(f"Resim yüklenemedi: {image_file}")
        continue

    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    faces = face_cascade.detectMultiScale(gray_image, scaleFactor=1.3, minNeighbors=5, minSize=(30, 30))
    print("Tespit edilen goz sayısı:", len(faces))
    for (x, y, w, h) in faces:
        face_roi = gray_image[y:y+h, x:x+w]
        eyes = eye_cascade.detectMultiScale(face_roi)
        for (ex, ey, ew, eh) in eyes:
            cv2.rectangle(image, (x+ex, y+ey), (x+ex+ew, y+ey+eh), (0, 255, 0), 2)
    base_filename = os.path.splitext(image_file)[0]
    count = processed_files.get(base_filename, 0)
    processed_files[base_filename] = count + 1

    if count > 0:
        unique_filename = f"{base_filename}_{count}"
    else:
        unique_filename = base_filename
    result_path = os.path.join(result_folder, 'result_' + unique_filename + '.jpg')
    cv2.imwrite(result_path, image)

print("İşlem tamamlandı.")

