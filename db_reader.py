import pandas as pd
from db_connection import get_connection


def fetch_data_from_db():
    connection = get_connection()

    query = "SELECT * FROM students;"
    df = pd.read_sql(query, connection)

    connection.close()

    return df
