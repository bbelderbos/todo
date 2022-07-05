from dataclasses import dataclass


@dataclass
class Task:
    description: str
    done: bool = False


class Todo:

    def __init__(self, tasks=None):
        self.tasks = tasks or {}
        self.count = 0

    def add_todo(self, description):
        task = Task(description)
        self.count += 1
        self.tasks[self.count] = task
        return task

    def get_todos(self):
        return self.tasks

    def remove_todo(self, idx):
        del self.tasks[idx]

    def mark_complete(self, idx):
        self.tasks[idx].done = True
