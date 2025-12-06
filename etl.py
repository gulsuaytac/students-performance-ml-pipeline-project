import pandas as pd
from db_connection import get_connection


def load_csv_to_db(csv_path):
    df = pd.read_csv(csv_path)

    #  Veritabanı bağlantısı
    connection = get_connection()
    cursor = connection.cursor()

    # Tabloyu garantiye aldık
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS students (
        id SERIAL PRIMARY KEY,
        gender VARCHAR(10),
        race_ethnicity VARCHAR(50),
        parental_level_of_education VARCHAR(100),
        lunch VARCHAR(20),
        test_preparation_course VARCHAR(20),
        math_score INT,
        reading_score INT,
        writing_score INT
    )
    """)

    connection.commit()

    #  Mevcut verileri temizledik
    cursor.execute("TRUNCATE TABLE students;")

    # CSV → PostgreSQL Insert
    for _, row in df.iterrows():
        cursor.execute("""
        INSERT INTO students (
            gender, race_ethnicity, parental_level_of_education,
            lunch, test_preparation_course,
            math_score, reading_score, writing_score
        )
        VALUES (%s,%s,%s,%s,%s,%s,%s,%s)
        """, (
            row["gender"],
            row["race/ethnicity"],
            row["parental level of education"],
            row["lunch"],
            row["test preparation course"],
            int(row["math score"]),
            int(row["reading score"]),
            int(row["writing score"])
        ))

    connection.commit()
    cursor.close()
    connection.close()

    return df.shape[0]

