from sqlalchemy import Column, String, Float
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class PostalCode(Base):
    __tablename__ = 'postal_codes'

    post_code = Column(String, primary_key=True)
    country = Column(String)
    longitude = Column(Float)
    latitude = Column(Float)
    state = Column(String)
