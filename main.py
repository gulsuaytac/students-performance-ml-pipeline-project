import pandas as pd
import matplotlib.pyplot as plt

from preprocessing import split_features_target
from model import train_models
from db_reader import fetch_data_from_db
from etl import load_csv_to_db
from db_connection import get_connection
from logger_config import logger




if __name__ == "__main__":

    # CSV → DB yükleme
    row_count = load_csv_to_db("dataset/StudentsPerformance.csv")
    print(f"✅ {row_count} satır PostgreSQL'e yüklendi")

    #  DB'den veriyi çek
    df = fetch_data_from_db()
    print("Veri PostgreSQL'den çekildi")

    logger.info("PostgreSQL'den veri başarıyla çekildi.")

    #  Feature - Target ayır
    X, y = split_features_target(df, "writing score")
    logger.info("Model eğitimi başlatıldı.")

    #  Modelleri eğitme
    results = train_models(X, y)

    lr_model, lr_mse, lr_r2, y_test, lr_pred = results["linear"]
    rf_model, rf_mse, rf_r2, _, rf_pred = results["random_forest"]

    # Sonuçları yazdırma
    print("\n📊 MODEL KARŞILAŞTIRMA SONUÇLARI\n")

    print("🔵 Linear Regression")
    print("MSE:", lr_mse)
    print("R2 Score:", lr_r2)
    logger.info(f"Linear Regression - MSE: {lr_mse}, R2: {lr_r2}")

    print("\n🟢 Random Forest")
    print("MSE:", rf_mse)
    print("R2 Score:", rf_r2)
    logger.info(f"Random Forest - MSE: {rf_mse}, R2: {rf_r2}")

    # Grafikler
    plt.figure()
    plt.scatter(y_test, lr_pred)
    plt.xlabel("Gerçek Math Score")
    plt.ylabel("Tahmin Edilen Math Score")
    plt.title("Linear Regression - Gerçek vs Tahmin")
    plt.show()

    plt.figure()
    plt.scatter(y_test, rf_pred)
    plt.xlabel("Gerçek Math Score")
    plt.ylabel("Tahmin Edilen Math Score")
    plt.title("Random Forest - Gerçek vs Tahmin")
    plt.show()

    # bağlantı testi
    connection = get_connection()
    print("\n PostgreSQL bağlantısı alındı")
    connection.close()
    print("Bağlantı kapatıldı")

    print("\n🎯 Program başarıyla tamamlandı.")
    logger.info("Program sorunsuz şekilde tamamlandı.")


