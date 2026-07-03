
# Criar uma aplicação FastAPI
# 1. Criar as tabelas do banco de dados usando Base.metadata.create_all(bind=engine)
# 2. Criar uma rota POST para "/transacoes" que recebe TransacaoCreate e salva no banco de dados
# 3. Criar uma rota GET para "/transacoes/insights" que busca todas as transações do banco, 
#    instancia o InsightService e retorna o total_receitas, total_despesas e o insight gerado.

from fastapi import FastAPI, Depends, status
import fastapi
from sqlalchemy.orm import Session
from src.services.insights import InsightService
from src.database.database import engine, Base, get_db
from src.models import models
from src.schemas import schemas

app = FastAPI(title="API de Transações", 
              summary="API para gerenciar transações financeiras.", 
              version="1.0.0" 
              )

# Criar as tabelas do banco de dados
Base.metadata.create_all(bind=engine)

#criar uma rota POST para "/transacoes" que recebe TransacaoCreate e salva no banco de dados
@app.post("/transacoes", response_model=schemas.TransacaoBase)
def criar_transacao(transacao: schemas.TransacaoCreate, db: Session = Depends(get_db)):
    db_transacao = models.Transacao(**transacao.model_dump())  # Usando model_dump() para converter o Pydantic model em dicionário
    db.add(db_transacao)    
    db.commit()
    db.refresh(db_transacao)
    return db_transacao

#criar uma rota GET para "/transacoes/insights" que busca todas as transações do banco, instancia o InsightService e retorna o total_receitas, total_despesas e o insight gerado.
@app.get("/transacoes/insights", response_model=schemas.Insight)
def gerar_insights(db: Session = Depends(get_db)):
    transacoes = db.query(models.Transacao).all()
    insight_service = InsightService(transacoes)
    total_receitas = insight_service.calcular_total_receitas()  
    total_despesas = insight_service.calcular_total_despesas()
    insight = insight_service.gerar_insight()
    return schemas.Insight(total_receitas=total_receitas, total_despesas=total_despesas, insight=insight)

#criar uma rota GET para "/transacoes" que busca todas as transações do banco e retorna uma lista de TransacaoResponse
@app.get("/transacoes", response_model=list[schemas.TransacaoResponse])
def listar_transacoes(db: Session = Depends(get_db)):
    return db.query(models.Transacao).all()


#criar uma rota para deletar uma transação pelo id
@app.delete("/transacoes/{transacao_id}")   
def deletar_transacao(transacao_id: int, db: Session = Depends(get_db)):
    transacao = db.query(models.Transacao).filter(models.Transacao.id == transacao_id).first()
    if transacao is None:
        raise fastapi.HTTPException(status_code=404, detail="Transação não encontrada")
    db.delete(transacao)
    db.commit()
    return {"message": "Transação deletada com sucesso"}    