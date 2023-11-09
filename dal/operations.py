"""
Utilitties operations
"""

from dal.client import get_cursor


def delete(cl, tb_n, col_n, value):
    """"""
    cursor = get_cursor(cl)
    cursor.execute(f"DELETE FROM {tb_n} WHERE {col_n} = %s;",
                   (value,))
    cl.commit()
    cursor.close()


def upload(cl, tb_n, col_n, value):
    """"""
    cursor = get_cursor(cl)
    cursor.execute(f"INSERT INTO {tb_n} ({col_n}) VALUES (%s);", (value,))
    cl.commit()
    cursor.close()


def download(cl, tb_n, col_n, value):
    """"""
    cursor = get_cursor(cl)
    cursor.execute(f"SELECT * FROM {tb_n} WHERE {col_n} = %s;", (value,))
    result = cursor.fetchone()
    cursor.close()
    return result


def update(cl, tb_n, col_n, value, new_value):
    """"""
    cursor = get_cursor(cl)
    cursor.execute(f"UPDATE {tb_n} SET {col_n} = %s WHERE {col_n} = %s;",
                   (new_value, value))
    cl.commit()
    cursor.close()
