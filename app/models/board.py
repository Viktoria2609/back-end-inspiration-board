from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import String
from ..db import db

class Board(db.Model):
    __tablename__ = "boards"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    title: Mapped[str] = mapped_column(String, nullable=False)
    owner: Mapped[str] = mapped_column(String, nullable=False)

    def to_dict(self):
        return {
            "id": self.id,
            "title": self.title,
            "owner": self.owner
        }