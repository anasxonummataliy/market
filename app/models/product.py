from datetime import datetime
from typing import TYPE_CHECKING

from sqlalchemy import DateTime, Float, ForeignKey, String, BigInteger, Boolean
from sqlalchemy.orm import Mapped, mapped_column, relationship


from app.models import db

if TYPE_CHECKING:
    from models import User, Category, CartItem


class Product(db.Model):
    __tablename__ = "products"

    id: Mapped[int] = mapped_column(BigInteger(), primary_key=True)
    title: Mapped[str] = mapped_column(String(255), nullable=False)
    description: Mapped[str] = mapped_column(String(), nullable=False)
    price: Mapped[float] = mapped_column(Float(), nullable=False)
    image_url: Mapped[str] = mapped_column(String(), nullable=True)
    is_approved: Mapped[bool] = mapped_column(Boolean(), default=False)
    created_at: Mapped[datetime] = mapped_column(DateTime(), default=datetime.now())

    user_id: Mapped[int] = mapped_column(BigInteger(), ForeignKey("users.id"))
    category_id: Mapped[int] = mapped_column(
        BigInteger(), ForeignKey("categories.id"), nullable=False
    )

    owner: Mapped["User"] = relationship("User", back_populates="products")
    category: Mapped["Category"] = relationship("Category", back_populates="products")
    cart_items: Mapped["CartItem"] = relationship("CartItem", back_populates="product")
