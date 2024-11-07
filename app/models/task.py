from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import ForeignKey
from datetime import datetime
from typing import Optional
from ..db import db

class Task(db.Model):
    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    title: Mapped[str]
    description: Mapped[str]
    completed_at: Mapped[Optional[datetime]]

    def to_dict(self):
        task_as_dict ={
            "id": self.id,
            "title": self.title,
            "description": self.description,
            "is_complete": bool(self.completed_at)
        }
        return task_as_dict

# @classmethod
# def from_dict(cls, task_data):
#     new_task = cls(
#         title=task_data["title"],
#         description=task_data["description"],
#         completed_at=task_data.get("completed_at")
#         )
#     return new_task