from app.db import db
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import String, ForeignKey
from typing import Optional

class Card(db.Model):
    __tablename__ = "cards"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    message: Mapped[str] = mapped_column(String, nullable=False)
    likes_count: Mapped[int] = mapped_column(default=0)

    board_id: Mapped[Optional[int]] = mapped_column(ForeignKey("boards.id"))
    board: Mapped[Optional["Board"]] = relationship("Board", back_populates="cards")


    def to_dict(self):
        return {
            "id": self.id,
            "message": self.message,
            "likes_count": self.likes_count
        }
    
    @classmethod
    def from_dict(cls, data):
        return cls(
            message=data["message"]
        )