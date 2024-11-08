from sqlalchemy.orm import Mapped, mapped_column, relationship
from ..db import db

class Goal(db.Model):
    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    title:Mapped[str]

    tasks: Mapped[list["Task"]] = relationship("Task", backref="goal", lazy="dynamic")

    def to_dict(self):
        from .task import Task
        goal_as_dict = {
            "id": self.id,
            "title": self.title,
            "tasks": [task.id for task in self.tasks] 
        }
        
        return goal_as_dict
