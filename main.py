import typer

from todo import Todo
from store import PersistentDb

app = typer.Typer()
db = PersistentDb("DATABASE_URL")
todo = Todo(db)


@app.command()
def add(description: str):
    todo.add_todo(description)
    print("task added")


@app.command()
def show():
    tasks = todo.get_todos()
    for task in tasks:
        done = "V" if task.done else "X"
        print(task.id, task.description, done)


@app.command()
def remove(task_id: int):
    todo.remove_todo(task_id)
    print("task removed")


@app.command()
def complete(task_id: int):
    todo.mark_complete(task_id)
    print("task completed")


if __name__ == "__main__":
    app()
