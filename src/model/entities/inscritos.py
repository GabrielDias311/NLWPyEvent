from src.model.configs.base import Base
from sqlalchemy import Column, String, Integer, foreigmn_key

class Inscritos(Base):
    __tablename__ = "inscritos"
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)
    email = Column(String, nullable=False)
    link = Column(String, nullable=True)
    evento_id = Column(Integer, foreign_key="eventos.id")
    