"""Скрипт для заполнения данными таблиц в БД Postgres."""

import csv
import logging

import psycopg2
from psycopg2.extensions import connection, cursor
from config import PATH_TO_LOG, DB_PASS, DB_TABLES

log = logging.getLogger(__name__)


def upload_data_to_table(cur: cursor, path: str, table_name: str) -> None:
    """
    Загружает данные из CSV-файла в таблицу
    :param cur: :class:`psycopg2.extensions.cursor`
    :param path: путь до CSV-файла
    :param table_name: имя таблицы
    :return: None
    """

    with open(path, 'r', encoding='utf-8') as file:
        reader: csv.reader = csv.reader(file)
        lst = next(reader)
        columns_name = ", ".join(lst)
        values = ", ".join(["%s"] * len(lst))
        query = f'INSERT INTO {table_name} ({columns_name}) VALUES ({values})'
        for row in reader:
            cur.execute(query, row)


def main():
    conn: connection = psycopg2.connect(host='localhost', database='north', user='postgres', password=DB_PASS)
    try:
        with conn:
            with conn.cursor() as cur:
                for table_name, path in DB_TABLES:
                    upload_data_to_table(cur, path, table_name)
    except Exception as e:
        log.error(e)
        print(f'Ошибка записана в лог: {PATH_TO_LOG}')
    finally:
        conn.close()


if __name__ == '__main__':
    logging.basicConfig(level=logging.DEBUG,
                        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                        filename=PATH_TO_LOG,
                        encoding='utf-8')
    main()
