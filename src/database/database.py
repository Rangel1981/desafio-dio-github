from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

# 1. Configurar a engine do SQLite
SQLALCHEMY_DATABASE_URL = "sqlite:///./finance.db"
engine = create_engine(
    SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}
)

# 2. Criar a SessionLocal (fábrica de sessões com o banco)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# 3. Criar a classe Base para POO (seus modelos vão herdar dela)
Base = declarative_base()

# 4. Função essencial para o FastAPI injetar o banco nas rotas
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()