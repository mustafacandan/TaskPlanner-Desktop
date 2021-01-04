class User:
    def __init__(self, name=None, email=None, pwd=None, id=None):
        self.id = id
        self.name = name
        self.email = email
        self.pwd = pwd
    
class Task:
    def __init__(self, user, date_created, due_date, id=None, project=None, title='', desc='',):
        self.id = id
        self.user = user
        self.project = project
        self.title = title
        self.desc = desc
        self.date_created = date_created
        self.due_date = due_date

