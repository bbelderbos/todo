import typer

from todo import Todo

app = typer.Typer()
todo = Todo()


@app.command()
def add(description: str):
    todo.add_todo(description)
    print("task added")


@app.command()
def show():
    tasks = todo.get_todos()
    print(tasks)


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
