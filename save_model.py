import joblib
from db_reader import fetch_data_from_db
from preprocessing import split_features_target
from sklearn.linear_model import LinearRegression
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error, r2_score
from logger_config import logger

def train_and_save_best_model():
    df = fetch_data_from_db()
    logger.info(f"Veri çekildi: {df.shape}")

    # TAHMİN EDİLECEK DEĞER
    X, y = split_features_target(df, "writing_score")

    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42
    )

    lr = LinearRegression()
    lr.fit(X_train, y_train)
    lr_pred = lr.predict(X_test)
    lr_r2 = r2_score(y_test, lr_pred)

    rf = RandomForestRegressor(n_estimators=100, random_state=42)
    rf.fit(X_train, y_train)
    rf_pred = rf.predict(X_test)
    rf_r2 = r2_score(y_test, rf_pred)

    if lr_r2 >= rf_r2:
        best_model = lr
        best_name = "LinearRegression"
        best_r2 = lr_r2
    else:
        best_model = rf
        best_name = "RandomForest"
        best_r2 = rf_r2

    joblib.dump(best_model, "student_success_model.pkl")
    joblib.dump(X.columns.tolist(), "model_features.pkl")

    print(f"En iyi model: {best_name} | R2: {best_r2:.4f}")
    print(" model ve feature dosyaları kaydedildi.")

if __name__ == "__main__":
    train_and_save_best_model()
