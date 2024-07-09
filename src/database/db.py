import psycopg2
from psycopg2 import DatabaseError
from decouple import config


def get_connection():
    try:
        return psycopg2.connect(
            host="172.19.0.2",
            user=config('PGSQL_USER'),
            password=config('PGSQL_PASSWORD'),
            database=config('PGSQL_DATABASE')
        )
    except DatabaseError as ex:
        raise ex