# Importar a Base de src.database.database
# Criar a classe Transacao que herda de Base
# Campos: id (Integer, PK), descricao (String), valor (Float), tipo (String), categoria (String)

from sqlalchemy import Column, Integer, String, Float
from src.database.database import Base

class Transacao(Base):
    __tablename__ = "transacoes"

    id = Column(Integer, primary_key=True, index=True)
    descricao = Column(String, index=True)
    valor = Column(Float)
    tipo = Column(String)
    categoria = Column(String)