from db_connection import get_connection

connection = get_connection()
cursor = connection.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS predictions (
    id SERIAL PRIMARY KEY,
    gender VARCHAR(10),
    race_ethnicity VARCHAR(20),
    parental_level_of_education VARCHAR(50),
    lunch VARCHAR(20),
    test_preparation_course VARCHAR(20),
    math_score INT,
    reading_score INT,
    predicted_writing_score FLOAT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
)
""")

connection.commit()
cursor.close()
connection.close()

print(" predictions tablosu başarıyla oluşturuldu.")
