import os
import psycopg
from psycopg.rows import dict_row

DATABASE_URL = os.environ.get(
    "DATABASE_URL", "postgresql://onsite:onsite@localhost:5432/onsite"
)


def get_connection():
    return psycopg.connect(DATABASE_URL, row_factory=dict_row)
