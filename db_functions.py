from tkinter import messagebox as msg
import sqlite3

# import yaml

# credentials = yaml.safe_load(open('./credentials.yml'))
# db_path = credentials['database']['path']

class Database:
    def get_db_connection(self):
        return sqlite3.connect('planner.db')

    def create_db_table(self):
        try:
            conn = self.get_db_connection()
            cur = conn.cursor()
            cur.execute("""
            CREATE TABLE IF NOT EXISTS ConversionHistory (
                cid   INTEGER PRIMARY KEY AUTOINCREMENT,
                conversion_text TEXT
            );
            """)
            conn.commit()
            conn.close()
        except Exception as exc:
            print('ERRORR', str(exc))
            # msg.showerror("Error", "Error: " + str(exc))

       
    def clear_history(self):
        try:
            conn = self.get_db_connection()
            cur = conn.cursor()
            cur.execute("""delete from ConversionHistory;""")
            conn.commit()
            conn.close()
            msg.showinfo("Clear History", "Clear History")
        except Exception as exc:
            print('ERRORR', str(exc))
            # msg.showerror("Error", "Error: " + str(exc))

    
    def add_to_database(self, result):
        try:
            conn = self.get_db_connection()
            cur = conn.cursor()
            cur.execute("insert into ConversionHistory(conversion_text) VALUES (?)", (result,))
            conn.commit()
            conn.close()
        except Exception as exc:
            print('ERRORR', str(exc))
            # msg.showerror("Error", "Error: " + str(exc))

