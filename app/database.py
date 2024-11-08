import os
import sqlite3
import pandas as pd

class Database:
    def __init__(self, db_path):
        self.conn = sqlite3.connect(db_path)
        self.cursor = self.conn.cursor()

    def create_table(self, table_name, columns):
        column_definitions = ', '.join([f'{column} TEXT' for column in columns])
        sql = f'''
            CREATE TABLE IF NOT EXISTS {table_name} (
                {column_definitions}
            )
        '''
        self.cursor.execute(sql)
        self.conn.commit()

    def insert_data(self, df, table_name):
        df.to_sql(table_name, self.conn, if_exists='replace', index=False)
        self.conn.commit()

    def close_connection(self):
        self.conn.close()

def change_cwd():
    abspath = os.path.abspath(__file__)
    d_name = os.path.dirname(abspath)
    os.chdir(d_name)

def get_db_conn():
    change_cwd()
    db_path = os.path.join(os.getcwd(), '../data/app.db')
    conn = sqlite3.connect(db_path)
    conn.row_factory = sqlite3.Row
    return conn

def init_excel_db():
    conn = get_db_conn()
    cursor = conn.cursor()
    # cursor.execute() TAKE THE EXCEL FILE -> WRITE IT INTO THE DB
    conn.commit()
    conn.close()

if __name__ == "__main__":
    init_excel_db()
