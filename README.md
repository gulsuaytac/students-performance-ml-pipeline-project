🎓 Student Performance ML Pipeline Project

Bu proje, öğrencilerin akademik başarılarını tahmin etmek için uçtan uca bir **Makine Öğrenmesi (Machine Learning) veri hattı (pipeline)** geliştirmeyi amaçlamaktadır. Projede veriler veritabanından çekilmekte, ön işleme adımlarından geçirilmektedir, en iyi model otomatik olarak seçilmekte ve gerçek kullanıcı girişlerine göre canlı tahmin yapılmaktadır.

---

 🚀 Projenin Amacı

Bu çalışmanın temel amacı:

* Öğrencilerin demografik ve akademik bilgilerine göre **başarı tahmini yapmak**
* Makine öğrenmesi sürecini **veri çekme → eğitim → model seçimi → kayıt → üretim (production)** aşamalarının tamamını kapsayacak şekilde bütünleşik hale getirmek
* Akademik düzeyde **R² skoru yüksek bir regresyon modeli** elde etmektir

---

 🧠 Kullanılan Modeller

* ✅ Linear Regression
* ✅ Random Forest Regressor

Model performansları karşılaştırılarak **en yüksek R² skoruna sahip model otomatik olarak seçilir ve kaydedilir.**

📌 Son Model Performansı:

```
✅ En iyi model: LinearRegression | R2: 0.9381
```

---

🛠 Kullanılan Teknolojiler

* Python
* Pandas
* Scikit-learn
* SQLite / SQL
* Joblib
* PyCharm
* Git & GitHub

---

 ⚙️ Kurulum

1️⃣ Repoyu klonla:

```bash
git clone https://github.com/gulsuaytac/students-performance-ml-pipeline-project.git
```

2️⃣ Gerekli kütüphaneleri yükle:

```bash
pip install pandas scikit-learn joblib
```

---

## 🧪 Model Eğitimi

Modeli eğitmek ve en iyi modeli kaydetmek için:

```bash
python save_model.py
```

Bu işlem sonunda:

* `student_success_model.pkl`
* `model_features.pkl`
  dosyaları otomatik olarak oluşur.

---

## 🏭 Production (Canlı Tahmin)

Gerçek öğrenci bilgileri girerek writing score tahmini yapmak için:

```bash
python production.py
```

🎓 Örnek Giriş:

```
Gender (female/male): male
Race (group A-E): A
Parental Level (bachelor/high school/master): master
Lunch (free/standard): free
Test Course (none/completed): completed
Math Score: 78
Reading Score: 85
```

🎯 Çıktı:

```
Tahmini Writing Score: 93.10
```

---

## 📊 Veri Seti

Veri seti aşağıdaki özellikleri içermektedir:

* gender
* race_ethnicity
* parental_level_of_education
* lunch
* test_preparation_course
* math_score
* reading_score
* writing_score (hedef değişken)

---

## 📈 Değerlendirme Metrikleri

* ✅ Mean Squared Error (MSE)
* ✅ R² Skoru

---

## 🎯 Projenin Kazanımları

* Gerçek hayat veri hattı simülasyonu
* Veritabanı bağlantısı ile model eğitimi
* Otomatik model seçimi
* Production ortamında canlı tahmin
* GitHub portföyüne güçlü ML projesi

---

## 🧩 Geliştirme Planları (Roadmap)

* 🔹 API ile web entegrasyonu (Flask/FastAPI)
* 🔹 Docker ile konteynerleştirme
* 🔹 Model performans izleme sistemi
* 🔹 Dashboard ile görselleştirme

---

## 👩‍💻 Geliştirici

**Gülsu Aytaç**
🎓 Yazılım Mühendisliği Yüksek Lisans
📌 İlgi Alanları: Yapay Zeka, Veri Bilimi, Doğal Dil İşleme
🔗 GitHub: [https://github.com/gulsuaytac](https://github.com/gulsuaytac)

---

⭐ Eğer projeyi beğendiysen yıldızlamayı unutma!
