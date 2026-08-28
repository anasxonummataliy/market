from datetime import datetime

from sqlalchemy import DateTime, String, BigInteger, Boolean
from sqlalchemy.orm import Mapped, mapped_column, relationship


from models import db, Product


class User(db.Model):
    __tablename__ = "users"

    id: Mapped[int] = mapped_column(BigInteger(), primary_key=True)
    first_name: Mapped[str] = mapped_column(String(), nullable=False)
    last_name: Mapped[str] = mapped_column(String(), nullable=False)
    username: Mapped[str] = mapped_column(String(), nullable=False, unique=True)
    password_hash: Mapped[str] = mapped_column(String(), nullable=True)
    is_admin: Mapped[bool] = mapped_column(Boolean(), default=False)
    created_at: Mapped[datetime] = mapped_column(DateTime(), default=datetime.now())

    products: Mapped[list['Product']] = relationship('Product', back_populates='owner')
