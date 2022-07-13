import pytest

from store import PersistentDb
from models import Task


@pytest.fixture
def db():
    db_env_var = 'TEST_DATABASE_URL'
    return PersistentDb(db_env_var)


def test_task_repr(db):
    db.add_todo("gym")
    task = db.get_todos(task_id=1)
    assert str(task) == "Task('1', 'gym', 'False')"


def test_add_todo(db):
    db.add_todo("gym")
    tasks = db.get_todos()
    assert len(tasks) == 1
    task = tasks[0]
    assert task.id == 1
    assert task.description == "gym"
    assert task.done is False


def test_get_single_todo(db):
    db.add_todo("gym")
    db.add_todo("sleep")
    task = db.get_todos(task_id=2)
    assert task.id == 2
    assert task.description == "sleep"
    assert task.done is False


def test_remove_todo(db):
    db.add_todo("gym")
    db.add_todo("sleep")
    db.remove_todo(2)
    tasks = db.get_todos()
    assert len(tasks) == 1
    task = tasks[0]
    assert task.id == 1
    assert task.description == "gym"
    assert task.done is False


def test_mark_complete(db):
    db.add_todo("gym")
    db.mark_complete(1)
    tasks = db.get_todos()
    task = tasks[0]
    assert task.done is True
