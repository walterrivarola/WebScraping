from sqlalchemy import Column, Integer, String
from database import Base

class product(Base):
    __tablename__ = "products"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(255), index=True)
    category = Column(String(255), index=True)
    price = Column(Integer, index=True)
    page = Column(Integer)