from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base, text

# Definir les parametres de connexion 
USER = "postgres"
PASSWORD = "123456789"
HOST = "localhost"
PORT = "5432"
DATABASE = "database"

# Creer la base
DATABASE_URL = f"postgresql+psycopg2://{USER}:{PASSWORD}@{HOST}:{PORT}/{DATABASE}"
engine = create_engine(DATABASE_URL, isolation_level="AUTOCOMMIT")
with engine.connect() as conn:
    conn.execute(text(f"CREATE DATABASE {DATABASE}"))

# Initialisation de SQLAlchemy et connexion à la base
Base = declarative_base()
SessionLocal = sessionmaker(bind=engine)
session = SessionLocal()



def get_db():
    db= SessionLocal()
    try:
        yield db
    finally:
        db.close()