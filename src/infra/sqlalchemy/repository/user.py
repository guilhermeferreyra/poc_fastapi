"""Importing dependencies"""
from sqlalchemy.orm import Session

class RepositoryUser():
    """Class to perform user database operations"""

    def __init__(self, db: Session):
        self.db = db

    def create(self):
        pass

    def list(self):
        pass

    def update(self):
        pass

    def delete(self):
        pass
