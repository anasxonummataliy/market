from datetime import datetime
from typing import TYPE_CHECKING

from sqlalchemy import DateTime, String, BigInteger, Boolean
from sqlalchemy.orm import Mapped, mapped_column, relationship


from app.models import db

if TYPE_CHECKING:
    from models.product import Product


class Category(db.Model):
    __tablename__ = "categories"

    id: Mapped[int] = mapped_column(BigInteger(), primary_key=True)
    name: Mapped[str] = mapped_column(String(), nullable=False)
    slug: Mapped[str] = mapped_column(String(), nullable=False)

    products: Mapped["Product"] = relationship("Product", back_populates="category")
