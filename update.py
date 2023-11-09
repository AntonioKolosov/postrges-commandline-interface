"""
Upload utility to PostgreSQL
"""


import os

from dotenv import load_dotenv

from dal.client import client
from dal.operations import update


def values():
    """Get values for SQL string"""
    table_name = input("Table name: ").strip()
    column_name = input("Column name: ").strip()
    new_value = input("New value: ").strip()
    value = input("Value: ").strip()
    return (table_name, column_name, value, new_value)


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

    # Update values
    (tb_name, column_name, value, new_value) = values()
    try:
        update(cl, tb_name, column_name, value, new_value)
        print(f"Value {value} changed to {new_value}")
    except Exception:
        print("Error! Table, column or value not found")


if __name__ == "__main__":
    main()
