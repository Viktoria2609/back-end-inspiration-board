from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.models.card import Card
from ..db import db
from typing import List
from sqlalchemy import String

class Board(db.Model):
    __tablename__ = "boards"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    title: Mapped[str] = mapped_column(String, nullable=False)
    owner: Mapped[str] = mapped_column(String, nullable=False)

    cards: Mapped[List["Card"]] = relationship("Card", back_populates="board", cascade="all, delete")

    def to_dict(self):
        return {
            "id": self.id,
            "title": self.title,
            "owner": self.owner
        }
    
    @classmethod
    def from_dict(cls, data):
        return cls(
            title=data["title"]
        )