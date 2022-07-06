from dataclasses import dataclass


@dataclass
class Task:
    description: str
    done: bool = False


class TodoException(Exception):
    pass


class Todo:

    def __init__(self, tasks=None):
        if tasks is None:
            self.tasks = {}
        else:
            self.tasks = tasks

    def _task_exists(self, description):
        return any(t.description == description
                   for t in self.tasks.values())

    def add_todo(self, description):
        task = Task(description)
        next_id = max(self.tasks, default=0) + 1
        if self._task_exists(description):
            error = f"Task '{description}' already exists"
            raise TodoException(error)
        self.tasks[next_id] = task
        return task

    def get_todos(self, task_id=None):
        if task_id is None:
            return self.tasks
        else:
            return self.tasks[task_id]

    def remove_todo(self, idx):
        del self.tasks[idx]

    def mark_complete(self, idx):
        self.tasks[idx].done = True
