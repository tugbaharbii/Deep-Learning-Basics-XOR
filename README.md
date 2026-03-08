# 🧠 Deep Learning Basics: Solving the XOR Problem

Bu proje, yapay sinir ağlarının (ANN) tarihsel gelişimindeki en önemli dönüm noktalarından biri olan **XOR (Özel VEYA) Problemi**'ni ele almaktadır. Proje kapsamında, tek katmanlı perceptronların neden başarısız olduğu ve çok katmanlı mimarilerin (MLP) bu sorunu nasıl çözdüğü Python ve NumPy kullanılarak simüle edilmiştir.

## 🚀 Projenin Amacı
Yapay sinir ağlarının doğrusal olmayan (non-linear) problemleri çözme yeteneğini temel matematiksel prensiplerle (Forward & Backpropagation) göstermek.

## 🧐 XOR Problemi Nedir?
XOR, girişler birbirinden farklı olduğunda `1`, aynı olduğunda `0` çıktısını veren mantıksal bir kapıdır. 
- **Tek Katmanlı Perceptron:** Veriyi doğrusal bir çizgiyle ayırmaya çalışır. Ancak XOR noktaları bir düzlemde tek bir çizgiyle ayrılamaz (**Linear Inseparability**).
- **Çok Katmanlı Sinir Ağı:** Gizli katmanlar ve aktivasyon fonksiyonları (Sigmoid) sayesinde veri uzayını büker ve problemi çözülebilir hale getirir.

## 🛠️ Kullanılan Teknolojiler
- **Python 3.x**
- **NumPy** (Matematiksel işlemler ve matris manipülasyonu için)

## 📊 Deney Sonuçları

### 1. Tek Katmanlı Perceptron (Başarısız)
Ağ, veriyi ayıramadığı için çıktıları ortalama bir değerde toplar:
- Beklenen: `[0, 1, 1, 0]`
- Tahmin edilen: `[[0.0], [0.33], [0.33], [0.66]]` (Doğrusal sınırlama nedeniyle başarısız)

### 2. Çok Katmanlı Sinir Ağı (Başarılı)
Gizli katman eklendiğinde ağ mantığı kavrar:
- Beklenen: `[0, 1, 1, 0]`
- Tahmin edilen: `[[0.32], [0.98], [0.98], [0.46]]` (Eşik değeri sonrası %100 doğruluk)

## 📁 Dosya Yapısı
- `single_layer_perceptron.py`: Tek katmanlı ağın başarısızlık deneyi.
- `multi_layer_perceptron.py`: Gizli katman içeren başarılı çözüm kodu.

## 💻 Nasıl Çalıştırılır?
Projeyi yerelinizde çalıştırmak için:
```bash
git clone [https://github.com/KULLANICI_ADIN/Deep-Learning-Basics-XOR.git](https://github.com/KULLANICI_ADIN/Deep-Learning-Basics-XOR.git)
cd Deep-Learning-Basics-XOR
python multi_layer_perceptron.py
