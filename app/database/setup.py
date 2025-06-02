from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from app.models.models import Base
from app.models import Patient, Appointment
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

DATABASE_URL = "sqlite:///clinic.db"

engine = create_engine(DATABASE_URL, echo=False)  # Set to False to disable debug output
SessionLocal = sessionmaker(bind=engine)

# Create tables
logger.info("Creating database tables...")
Base.metadata.create_all(engine)
logger.info("Database tables created successfully")

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()