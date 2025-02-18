from src.model.configs.base import Base
from sqlalchemy import Column, String, Integer

class Eventos(Base):
    __tablename__ = "eventos"
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)
    