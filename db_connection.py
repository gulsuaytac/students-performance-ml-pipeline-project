import psycopg2

def get_connection():
    connection = psycopg2.connect(
        host="localhost",
        database="postgres",
        user="postgres",
        password="Postgres123",
        port="5432"
    )
    return connection
