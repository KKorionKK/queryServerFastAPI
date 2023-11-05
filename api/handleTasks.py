from api.redis import r


async def get_build(build_name: str) -> list:
    tasks = await r.lrange("build:{}".format(build_name), 0, -1)
    tasks.reverse()
    completed = []
    for task in tasks:
        await get_dependencies(task, completed)

    return completed


async def get_dependencies(task_name: bytes | str, completed_tasks: list):
    if isinstance(task_name, bytes):
        task_name = task_name.decode("utf-8")
    deps = await r.lrange("task:{}".format(task_name), 0, -1)
    deps.reverse()
    for task in deps:
        await get_dependencies(task, completed_tasks)

    completed_tasks.append(task_name)
