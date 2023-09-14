import psycopg
from env_var_selector import get_env_var as _


class DBConnector:
    __conn = None

    def __init__(self):
        DBConnector.__conn = psycopg.connect(dbname=_('DB_NAME'),
                                             user=_('DB_USER'),
                                             password=_('DB_PASSWORD'),
                                             host=_('DB_HOST'),
                                             port=_('DB_PORT'))

    @staticmethod
    def execute(query, values=None):
        if not DBConnector.__conn:
            DBConnector()
        cursor = DBConnector.__conn.cursor()
        if values:
            cursor.execute(query, values)
        else:
            cursor.execute(query)
        return cursor

    @staticmethod
    def execute_commit(query, values=None):
        if not DBConnector.__conn:
            DBConnector()
        __conn = DBConnector.__conn
        if values:
            __conn.cursor().execute(query, values)
        else:
            __conn.cursor().execute(query)
        __conn.commit()
