from datetime import datetime
from typing import TYPE_CHECKING

from sqlalchemy import DateTime, Float, ForeignKey, String, BigInteger, Boolean
from sqlalchemy.orm import Mapped, mapped_column, relationship


from models import db, Product


class Cart(db.Model):
    __tablename__ = "carts"

    id: Mapped[int] = mapped_column(BigInteger(), primary_key=True)

    user_id: Mapped[int] = mapped_column(
        BigInteger(), ForeignKey("users.id"), unique=True, nullable=False
    )
    items: Mapped[list["CartItem"]] = relationship(
        "CartItem", back_populates="cart", cascade="all, delete-orphan"
    )


class CartItem(db.Model):
    __tablename__ = "cart_items"

    id: Mapped[int] = mapped_column(BigInteger(), primary_key=True)
    quantity: Mapped[int] = mapped_column(BigInteger(), default=1, nullable=False)

    product_id: Mapped[int] = mapped_column(BigInteger(), ForeignKey('products.id'), nullable=False)
    cart_id: Mapped[int] = mapped_column(BigInteger(), ForeignKey('carts.id'), nullable=False)

    product: Mapped['Product'] = relationship("Product", back_populates='cart_items')
