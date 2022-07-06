import pytest

from todo import Todo, Task


@pytest.fixture
def todo():
    return Todo()


def test_add_todo(todo):
    assert todo.add_todo("gym") == Task("gym")


def test_get_todos(todo):
    todo.add_todo("read")
    assert todo.get_todos() == {1: Task("read")}


def test_get_todos_with_two_items(todo):
    todo.add_todo("read")
    todo.add_todo("gym")
    assert todo.get_todos() == {
        1: Task("read"), 2: Task("gym")
    }


def test_remove_todo(todo):
    todo.add_todo("read")
    todo.add_todo("gym")
    todo.remove_todo(2)
    assert todo.get_todos() == {1: Task("read")}


def test_mark_todo_complete(todo):
    todo.add_todo("read")
    todo.mark_complete(1)
    assert todo.tasks[1].done is True


def test_cannot_remove_non_existing_task(todo):
    todo.add_todo("read")
    with pytest.raises(KeyError):
        todo.remove_todo(2)


def test_cannot_mark_non_existing_task_complete(todo):
    todo.add_todo("read")
    with pytest.raises(KeyError):
        todo.mark_complete(2)


def test_increases_count_to_next_available_id(todo):
    todo.add_todo("read")
    todo.add_todo("gym")
    todo.add_todo("sleep")
    todo.remove_todo(3)
    todo.add_todo("sleep")
    assert list(todo.get_todos().keys()) == [1, 2, 3]
