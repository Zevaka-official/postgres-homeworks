import os

DB_PASS = os.getenv('DB_PASS')
PATH_TO_LOG = os.path.join(os.path.dirname(__file__), 'error.log')

CUSTOMERS_PATH = os.path.join(os.path.dirname(__file__), 'north_data', 'customers_data.csv')
EMPLOYEES_PATH = os.path.join(os.path.dirname(__file__), 'north_data', 'employees_data.csv')
ORDERS_PATH = os.path.join(os.path.dirname(__file__), 'north_data', 'orders_data.csv')

DB_TABLES = [
    ('employees', EMPLOYEES_PATH),
    ('customers', CUSTOMERS_PATH),
    ('orders', ORDERS_PATH),
]

