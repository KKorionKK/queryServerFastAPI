from pydantic import BaseModel


class BuildRequest(BaseModel):
    build: str


class TasksResponse(BaseModel):
    tasks: list[str]
