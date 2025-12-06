from sklearn.preprocessing import LabelEncoder

def scale_numeric_columns(df):
    df["math score"] = df["math score"] / 100
    df["reading score"] = df["reading score"] / 100
    df["writing score"] = df["writing score"] / 100
    return df


def encode_categorical_columns(df):
    encoder = LabelEncoder()
    categorical_cols = [
        'gender',
        'race/ethnicity',
        'parental level of education',
        'lunch',
        'test preparation course'
    ]

    for col in categorical_cols:
        df[col] = encoder.fit_transform(df[col])

    return df
