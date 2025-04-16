import os
import psycopg2
from contextlib import contextmanager


@contextmanager
def get_cursor():
    # crea la conexión
    connection = psycopg2.connect(
        host=os.environ.get("DB_HOST"),
        port=os.environ.get("DB_PORT"),
        user=os.environ.get("DB_USER"),
        password=os.environ.get("DB_PASSWORD"),
        database=os.environ.get("DB_DATABASE"))

    try:
        with connection.cursor() as cursor:
            yield cursor  # retonar el cursor cuando se llame a get_cursor()
            connection.commit()  # si todo sale bien, guarda los cambios en la bd
    except:
        connection.rollback()  # si ocurre un error , deshace cambios no confirmados
        raise
    finally:
        connection.close()  # Cierra la conexión
