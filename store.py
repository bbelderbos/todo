from abc import ABC, abstractmethod
from dataclasses import dataclass

from decouple import config
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from models import Base, Task as TaskTable


@dataclass
class Task:
    description: str
    done: bool = False


class TodoException(Exception):
    pass


class BaseDb(ABC):

    @abstractmethod
    def add_todo(self, description):
        pass

    @abstractmethod
    def get_todos(self, task_id=None):
        pass

    @abstractmethod
    def remove_todo(self, task_id):
        pass

    @abstractmethod
    def mark_complete(self, task_id):
        pass


class InMemoryDb(BaseDb):

    def __init__(self, tasks=None):
        self.tasks = dict(tasks or {})

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

    def remove_todo(self, task_id):
        del self.tasks[task_id]

    def mark_complete(self, task_id):
        self.tasks[task_id].done = True


class PersistentDb(BaseDb):

    def __init__(self, db_env_var):
        self.db_url = config(db_env_var)
        self.session = self._create_session()

    def _create_session(self):
        engine = create_engine(self.db_url)
        Base.metadata.create_all(engine)
        create_session = sessionmaker(bind=engine)
        return create_session()

    def add_todo(self, description):
        task = TaskTable(description=description)
        self.session.add(task)
        self.session.commit()

    def get_todos(self, task_id=None):
        query = self.session.query(TaskTable)
        if task_id is not None:
            query = query.filter(TaskTable.id == task_id)
        return query.all()

    def remove_todo(self, task_id):
        self.session.query(TaskTable).filter(
            TaskTable.id == task_id).delete()
        self.session.commit()

    def mark_complete(self, task_id):
        self.session.query(TaskTable).filter(
            TaskTable.id == task_id).update({"done": True})
        self.session.commit()
