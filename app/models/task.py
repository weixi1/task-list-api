from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import ForeignKey
from datetime import datetime
from typing import Optional
from .goal import Goal
from ..db import db

class Task(db.Model):
    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    title: Mapped[str]
    description: Mapped[str]
    completed_at: Mapped[Optional[datetime]]

    goal_id: Mapped[Optional[int]] = mapped_column(ForeignKey("goal.id"), nullable=True)

    goal: Mapped[Optional["Goal"]] = relationship("Goal", backref="tasks", lazy="joined")

    def to_dict(self):
        task_as_dict ={
            "id": self.id,
            "title": self.title,
            "description": self.description,
            "is_complete": bool(self.completed_at),
            "goal_id": self.goal_id
        }
        return task_as_dict