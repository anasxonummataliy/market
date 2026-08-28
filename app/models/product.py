from datetime import datetime

from sqlalchemy import DateTime, Float, ForeignKey, String, BigInteger, Boolean
from sqlalchemy.orm import Mapped, mapped_column


from models import db


class Product(db.Model):
    __tablename__ = "products"

    id: Mapped[int] = mapped_column(BigInteger(), primary_key=True)
    title: Mapped[str] = mapped_column(String(255), nullable=False)
    description: Mapped[str] = mapped_column(String(), nullable=False)
    price: Mapped[float] = mapped_column(Float(), nullable=False)
    image_url: Mapped[str] = mapped_column(String(), nullable=True)
    is_approved: Mapped[bool] = mapped_column(Boolean(), default=False)
    created_at: Mapped[datetime] = mapped_column(DateTime(), default=datetime.now())

    user_id: Mapped[int] = mapped_column(BigInteger(), ForeignKey('users.id'))
    category_id: Mapped[int] = mapped_column(BigInteger(), ForeignKey('categories.id'), nullable=False)
