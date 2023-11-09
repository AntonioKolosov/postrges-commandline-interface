"""
Create client for database.
Server provided by https://render.com/
"""


import ssl

import pg8000.dbapi


def client(user, password, host, port, database):
    """Create client to connect database"""
    ssl_context = ssl.create_default_context()
    ssl_context.check_hostname = True
    ssl_context.verify_mode = ssl.CERT_REQUIRED

    try:
        client = pg8000.dbapi.connect(user=user,
                                      password=password,
                                      host=host,
                                      port=port,
                                      database=database,
                                      ssl_context=ssl_context)
        return client
    except Exception:
        print(f"Client {client} not avaible")


def create_cursor(client):
    """Create cursor for using with database"""
    try:
        cursor = client.cursor()
        return cursor
    except Exception:
        print("Cursor creation error")
        return None


def get_cursor(client):
    """"""
    return create_cursor(client)
