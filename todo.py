class Todo:

    def __init__(self, db):
        self.db = db

    def add_todo(self, description):
        return self.db.add_todo(description)

    def get_todos(self, task_id=None):
        return self.db.get_todos(task_id=task_id)

    def remove_todo(self, task_id):
        self.db.remove_todo(task_id)

    def mark_complete(self, task_id):
        self.db.mark_complete(task_id)
