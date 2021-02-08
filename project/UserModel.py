from datetime import datetime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, DateTime
from project.SettingPostgres import Base
from project.SettingPostgres import ENGINE

class User(Base):
    """
    UserModel
    """

    __tablename__ = 'users'
    id = Column(Integer, primary_key=True, autoincrement=True)
    username = Column(String(200))
    password = Column(String(200))
    created_at = Column(DateTime, default=datetime.now, nullable=False)
    updated_at = Column(DateTime, default=datetime.now, nullable=False)

    def __init__(self, username):
        self.username = username

if __name__ == "__main__":
    Base.metadata.create_all(bind=ENGINE)