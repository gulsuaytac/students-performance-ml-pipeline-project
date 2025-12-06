import joblib
import pandas as pd
from logger_config import logger
from db_connection import get_connection

# Model ve Feature Yapısını Yükle
model = joblib.load("student_success_model.pkl")
model_features = joblib.load("model_features.pkl")

logger.info("Model ve feature yapısı yüklendi.")

#  Input Al
print("\n🎓 Yeni Öğrenci Bilgileri:")

gender = input("Gender (female/male): ")
race = input("Race (group A-E): ")
parent_edu = input("Parental Level (bachelor/high school/master): ")
lunch = input("Lunch (free/standard): ")
prep = input("Test Course (none/completed): ")
math = int(input("Math Score: "))
reading = int(input("Reading Score: "))

# Ham veriyi dataframe yap
new_data = pd.DataFrame([{
    "gender": gender,
    "race_ethnicity": race,
    "parental_level_of_education": parent_edu,
    "lunch": lunch,
    "test_preparation_course": prep,
    "math_score": math,
    "reading_score": reading
}])

#  One-hot encoding
new_data_encoded = pd.get_dummies(new_data)

# Eğitim feature yapısına zorla uydur
new_data_encoded = new_data_encoded.reindex(columns=model_features, fill_value=0)

#  Tahmin
prediction = model.predict(new_data_encoded)[0]

print("\n🎯 Tahmini Writing Score:", round(prediction, 2))
logger.info(f"Üretim Tahmini Yapıldı → Writing Score: {prediction}")

# TAHMİNİ VERİTABANINA KAYDET
connection = get_connection()
cursor = connection.cursor()

cursor.execute("""
INSERT INTO predictions (
    gender, race_ethnicity, parental_level_of_education,
    lunch, test_preparation_course,
    math_score, reading_score, predicted_writing_score
)
VALUES (%s,%s,%s,%s,%s,%s,%s,%s)
""", (
    gender, race, parent_edu,
    lunch, prep,
    math, reading, prediction
))

connection.commit()
cursor.close()
connection.close()

print("✅ Tahmin PostgreSQL'e başarıyla kaydedildi.")
