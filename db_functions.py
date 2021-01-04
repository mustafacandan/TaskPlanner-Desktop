from tkinter import messagebox as msg
import sqlite3

DB_NAME = 'planner.db'

class Database:
    def get_db_connection(self):
        return sqlite3.connect(DB_NAME)

    def create_tables(self):
        try:
            conn = self.get_db_connection()
            cur = conn.cursor()
            
            # Projects Table
            cur.execute("""
            create table if not exists Project
            (
                id      integer
                    constraint Project_pk
                        primary key autoincrement,
                name    varchar,
                user_id integer not null
            );
            """)
            conn.commit()
            
            # Tags Table
            cur.execute("""
            create table if not exists Tag
            (
                id   integer
                    constraint Tag_pk
                        primary key autoincrement,
                name varchar
            );
            """)

            # Users Table
            cur.execute("""
            create table if not exists User
            (
                id       integer
                    constraint User_pk
                        primary key autoincrement,
                name     varchar,
                email    varchar,
                password varchar not null
            );
            """)
            conn.commit()

            # Tasks Table
            cur.execute("""
            create table if not exists Task
            (
                id           integer
                    constraint Task_pk
                        primary key autoincrement,
                user_id      integer  not null
                    references User,
                project_id   integer
                    references Project,
                date_created Datetime not null,
                due_date     Datetime
            );
            """)
            conn.commit()


            # Tasks and Tags Mapping Table 
            cur.execute("""
            create table if not exists Task_Tag
            (
                id      integer
                    constraint Task_Tag_pk
                        primary key autoincrement,
                task_id integer not null
                    references Task,
                tag_id  integer not null
                    references Tag
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

