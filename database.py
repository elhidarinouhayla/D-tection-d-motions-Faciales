from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
import os
from config import USER, PASSWORD, HOST, PORT, DATABASE

# Mode test activé dans GitHub Actions
TESTING = os.getenv("TESTING", "0") == "1"

# Choix de la base selon le mode
if TESTING:
    print(">>> USING SQLITE TEST DATABASE <<<")
    DATABASE_URL = "sqlite:///./test.db"
else:
    DATABASE_URL = f"postgresql+psycopg2://{USER}:{PASSWORD}@{HOST}:{PORT}/{DATABASE}"

# Création du moteur
engine = create_engine(
    DATABASE_URL,
    connect_args={"check_same_thread": False} if TESTING else {},
    isolation_level="AUTOCOMMIT" if not TESTING else None
)

# Initialisation ORM
Base = declarative_base()
SessionLocal = sessionmaker(bind=engine, autocommit=False, autoflush=False)


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
