from datetime import datetime

from sqlalchemy import DateTime, String, BigInteger, Boolean
from sqlalchemy.orm import Mapped, mapped_column, relationship


from models import db, Product


class Category(db.Model):
    __tablename__ = "categories"

    id: Mapped[int] = mapped_column(BigInteger(), primary_key=True)
    name: Mapped[str] = mapped_column(String(), nullable=False)
    slug: Mapped[str] = mapped_column(String(), nullable=False)

    products: Mapped['Product'] = relationship('Product', back_populates='category')
