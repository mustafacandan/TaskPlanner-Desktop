from tkinter import messagebox as msg
import sqlite3
from models import Task

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

    # user
    def add_user(self, user):
        if all([user.name, user.email, user.pwd]):
            raise ValueError()
            # TODO: Show Error
        try:
            conn = self.get_db_connection()
            cur = conn.cursor()
            cur.execute("insert into User(name, email, password) VALUES (?, ?, ?)", (user.name, user.email, user.pwd))
            conn.commit()
            query = """SELECT id from User where email = ?"""
            cur.execute(query, (user.email,))
            user_id = cur.fetchone()
            conn.close()
            return user_id
        except Exception as exc:
            print('ERRORR', str(exc))
            # msg.showerror("Error", "Error: " + str(exc))

    def check_user_pwd(self, email, password):
        pass

    # project
    def get_projects(self, user):
        try:
            conn = self.get_db_connection()
            cur = conn.cursor()
            query = """SELECT project.id, project.name from Project where project.user_id = ?"""
            cur.execute(query, (user.id,))
            projects = cur.fetchall()
            conn.close()
            return projects
        except Exception as exc:
            print('ERRORR', str(exc))
            # msg.showerror("Error", "Error: " + str(exc))        

    # # tag
    # def get_tags(self, user):
    #     try:
    #         conn = self.get_db_connection()
    #         cur = conn.cursor()
    #         query = """SELECT tag.id, tag.name from Tag"""
    #         cur.execute(query, (user.id,))
    #         tags = cur.fetchall()
    #         conn.close()
    #         return tags
    #     except Exception as exc:
    #         print('ERRORR', str(exc))
    #         # msg.showerror("Error", "Error: " + str(exc))   

    # task
    def get_tasks(self, user, filters=None):
        # date_range = filters['date'] 
        # project = filters['project']
        project_id = 1 # TODO: parametre ekle
        try:
            conn = self.get_db_connection()
            cur = conn.cursor()
            query = """
            SELECT *
            from Task, Project
            left join Project P on Task.project_id = P.id
            where project.user_id = 1 and Project.id = ?"""
            cur.execute(query, (project_id,))
            tasks = []
            for task in cur.fetchall():
                task_id, user_id, project_id, date_created, due_date, desc, title, status, _, project_name, _,_,_,_ = task
                t = Task(user, project=project_name, title=title, desc=desc, date_created=date_created, due_date=due_date, id=task_id)
                tasks.append(t)
            conn.close()
            return tasks
        except Exception as exc:
            print('ERRORR', str(exc))
            # msg.showerror("Error", "Error: " + str(exc))   

    def add_task(self, task):
        try:
            conn = self.get_db_connection()
            cur = conn.cursor()
            cur.execute("insert into Task(user_id, project_id, date_created, due_date, desc, title, status) VALUES (?, ?, ?, ?, ?, ?, ?)", 
                            (task.user.id, task.project, task.date_created, task.due_date, task.desc, task.title, 'no status'))
            conn.commit()
            conn.close()
        except Exception as exc:
            print('ERRORR', str(exc))
            # msg.showerror("Error", "Error: " + str(exc))


    def set_task_done(self, task):
        # UPDATE Task SET status = 'done' WHERE id = 1
        try:
            conn = self.get_db_connection()
            cur = conn.cursor()
            cur.execute("UPDATE Task SET status = 'done' WHERE id = ?)", (task.id, ))
            conn.commit()
            conn.close()
        except Exception as exc:
            print('ERRORR', str(exc))
            # msg.showerror("Error", "Error: " + str(exc))

    # session
    def get_last_user(self):
        try:
            conn = self.get_db_connection()
            cur = conn.cursor()
            query = """
            SELECT id, last_user
            from Session"""
            cur.execute(query)
            _, last_user = cur.fetchone()
            conn.close()
            return last_user
        except Exception as exc:
            print('ERRORR', str(exc))

    def get_last_language(self):
        try:
            conn = self.get_db_connection()
            cur = conn.cursor()
            query = """
            SELECT last_language
            from Session"""
            cur.execute(query)
            last_language = cur.fetchone()
            conn.close()
            return last_language
        except Exception as exc:
            print('ERRORR', str(exc))