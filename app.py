from fastapi import FastAPI, HTTPException, status
import uvicorn
import asyncio
import click

from api.schemas import BuildRequest, TasksResponse
from api.services import load_files
from api.handleTasks import get_build

app = FastAPI()


@app.post("/", response_model=TasksResponse)
async def get_task(request: BuildRequest):
    """
    Получаем на вход имя билда и возвращаем список тасков
    """
    tasks = await get_build(request.build)
    if tasks == []:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Билд с таким именем не найден",
        )
    return TasksResponse(tasks=tasks)


@click.group()
def cli():
    pass


@cli.command()
def initdb():
    """
    Инициализирует базу данных, используется при первом запуске.
    """
    click.echo("Попытка инициализации базы данных")
    asyncio.run(load_files())
    click.echo("Успешно!")


@cli.command()
def run():
    """
    Запускает сервер FastAPI
    """
    click.echo("Запуск сервера uvicorn")
    uvicorn.run(app, host="0.0.0.0", port=8000)


if __name__ == "__main__":
    cli()
