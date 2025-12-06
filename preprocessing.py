import pandas as pd

def split_features_target(df, target_column):
    #  ID asla modele girmemeli
    df = df.drop("id", axis=1)

    #  One-hot encoding eğitimin içinde yapılmalı
    df_encoded = pd.get_dummies(df)

    X = df_encoded.drop(target_column, axis=1)
    y = df_encoded[target_column]

    return X, y
