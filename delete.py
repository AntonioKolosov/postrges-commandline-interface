"""
Upload utility to PostgreSQL
"""


import os

from dotenv import load_dotenv

from dal.client import client
from dal.operations import delete


def values():
    """Get values for SQL string"""
    table_name = input("Table name: ").strip()
    column_name = input("Column name: ").strip()
    value = input("Value: ").strip()
    return (table_name, column_name, value)


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

    # Delete from table
    (tb_name, column_name, value) = values()
    try:
        delete(cl, tb_name, column_name, value)
        print("Item was deleted")
    except Exception:
        print("Error! Item not found")


if __name__ == "__main__":
    main()
