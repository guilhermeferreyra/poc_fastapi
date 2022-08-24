"""Importing packages"""
from typing import List, Optional
from pydantic import BaseModel


class User(BaseModel):
    """DB user defined class"""
    email: str
    id: Optional[str] = None
    first_name: str
    last_name: str
    hashed_password: str
    is_active: bool = True
    attendances: List[Attendance]


class Attendance(BaseModel):
    """DB attendance defined class"""
    customer_first_name: str
    customer_flast_name: str
    create_date: str
    testimony: str
    user: User
