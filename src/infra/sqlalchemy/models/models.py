"""Import libs and packages"""
from datetime import datetime
from sqlalchemy import Column, Integer, String, Boolean, ForeignKey
from sqlalchemy.orm import relationship
from database import Base

class User(Base):
    """Class to define User table in DB"""
    __tablename__ = "user"

    id = Column(Integer, primary_key=True, index=True)
    first_name = Column(String(255), nullable=False)
    last_name = Column(String(255), nullable=False)
    email = Column(String(255), unique=True, index=True, nullable=False)
    hashed_password = Column(String(255), nullable=False)
    is_active = Column(Boolean, default=True)

    testimonies = relationship("Attendance", back_populates="user")

class Attendance(Base):
    """Class to define attendance table in DB"""
    __tablename__ = "attendance"

    id = Column(Integer, primary_key=True, index=True)
    first_name = Column(String(255), nullable=False)
    last_name = Column(String(255), nullable=False)
    create_date = Column(String(255), default=datetime.now())
    user_id = Column(Integer, ForeignKey("user.id"), nullable=False)
    testimony = Column(String(255))

    user = relationship("User", back_populates="testimonies")