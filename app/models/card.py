from app.db import db
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import Integer, String

class Card(db.Model):
    __tablename__ = "cards"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    message: Mapped[str] = mapped_column(String, nullable=False)
    likes_count: Mapped[int] = mapped_column(default=0)

    def to_dict(self):
        return {
            "id": self.id,
            "message": self.message,
            "likes_count": self.likes_count
        }