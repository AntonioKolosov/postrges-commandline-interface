"""
Upload utility to PostgreSQL
"""


import os

from dotenv import load_dotenv

from dal.client import client
from dal.operations import download


def values():
    """Get values for SQL string"""
    table_name = input("Table name: ").strip()
    column_name = input("Column name: ").strip()
    value = input("Value: ").strip()
    return table_name, column_name, value


def main():
    """Main flow"""
    # Create client
    load_dotenv()
    user = os.getenv("USER")
    password = os.getenv("PASS")
    host = os.getenv("HOST")
    port = os.getenv("PORT")
    database = os.getenv("DBNAME")
    cl = client(user, password, host, port, database)

    # Insert into table
    (tb_name, column_name, value) = values()
    try:
        print(download(cl, tb_name, column_name, value))
    except Exception:
        print("Error! Table or column not found")


if __name__ == "__main__":
    main()
