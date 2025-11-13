from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker,declarative_base
from sqlalchemy import text
from config import USER, PASSWORD, HOST, PORT, DATABASE 

# Creer la base
DATABASE_URL = f"postgresql+psycopg2://{USER}:{PASSWORD}@{HOST}:{PORT}"
engine = create_engine(DATABASE_URL, isolation_level="AUTOCOMMIT")

with engine.connect() as conn:
    conn.execute(text(f"CREATE DATABASE {DATABASE}"))
    print('database created')

# Connecter à la base:
DATABASE_URL = f"postgresql+psycopg2://{USER}:{PASSWORD}@{HOST}:{PORT}/{DATABASE}"
engine = create_engine(DATABASE_URL, isolation_level="AUTOCOMMIT")

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