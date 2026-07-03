# Importar BaseModel do pydantic
# Criar um schema TransacaoBase com descricao (str), valor (float), tipo (str) e categoria (str)
# Criar TransacaoCreate que herda de TransacaoBase
# Criar TransacaoResponse que herda de TransacaoBase e adiciona o id (int)

from pydantic import BaseModel 


class TransacaoBase(BaseModel):
    descricao: str
    valor: float
    tipo: str
    categoria: str


class TransacaoCreate(TransacaoBase):
    pass


class TransacaoResponse(TransacaoBase):
    id: int

    class Config:
        from_attributes = True

class Insight(BaseModel):
    total_receitas: float
    total_despesas: float
    insight: str

    class Config:
        from_attributes = True
