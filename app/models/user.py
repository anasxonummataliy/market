from datetime import datetime
from typing import TYPE_CHECKING

from sqlalchemy import DateTime, String, BigInteger, Boolean
from sqlalchemy.orm import Mapped, mapped_column, relationship


from app.models import db, login_manager

if TYPE_CHECKING:
    from models.product import Product

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


class User(db.Model):
    __tablename__ = "users"

    id: Mapped[int] = mapped_column(BigInteger(), primary_key=True)
    first_name: Mapped[str] = mapped_column(String(), nullable=False)
    last_name: Mapped[str] = mapped_column(String(), nullable=False)
    username: Mapped[str] = mapped_column(String(), nullable=False, unique=True)
    password_hash: Mapped[str] = mapped_column(String(), nullable=True)
    is_admin: Mapped[bool] = mapped_column(Boolean(), default=False)
    created_at: Mapped[datetime] = mapped_column(DateTime(), default=datetime.now())

    products: Mapped[list["Product"]] = relationship("Product", back_populates="owner")
