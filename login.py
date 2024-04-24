import psycopg2
from config import load_config

def connect(config):
    """ Connect to the PostgreSQL database server with ini file """
    try:
        # connecting to the PostgreSQL server
        with psycopg2.connect(**config) as conn:
            print('Connected to the PostgreSQL server.')
            return conn
    except (psycopg2.DatabaseError, Exception) as error:
        print(error)

def connect(config, usern, passw):
    """ Connect to PostgreSQL database server with username & password """
    try:
        with psycopg2.connect(
            **config,
            user = usern,
            password = passw
        ) as conn:
            print(f"Welcome {usern}!")
            return conn

    except (psycopg2.DatabaseError, Exception) as error:
        # print(error)
        print("Incorrect username or password")

if __name__ == '__main__':
    config = load_config()
    connect(config)