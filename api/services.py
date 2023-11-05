from ruamel.yaml import YAML
from api.redis import r
import click


async def load_builds(filepath: str = "./builds/builds.yaml"):
    yaml = YAML()
    with open(filepath, "r") as file:
        builds: dict[list] = yaml.load(file)

    for build in builds.get("builds"):
        tasks = build.get("tasks")
        for task in tasks:
            await r.lpush("build:{}".format(build.get("name")), task)


async def load_tasks(filepath: str = "./builds/tasks.yaml"):
    yaml = YAML()
    with open(filepath, "r") as file:
        tasks: dict[list] = yaml.load(file)

    for task in tasks.get("tasks"):
        deps = task.get("dependencies")
        for dep in deps:
            await r.lpush("task:{}".format(task.get("name")), dep)


async def load_files():
    if await r.get("is_initialized") == b"1":
        click.echo("База данных уже инициализирована")
        return
    await load_tasks()
    await load_builds()
    await r.set("is_initialized", 1)
