from app.models.models import Base
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship

class Patient(Base):
    __tablename__ = 'patients'
    
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    age = Column(Integer)
    contact = Column(String)
    
    # One-to-many relationship with appointments
    appointments = relationship("Appointment", back_populates="patient", cascade="all, delete-orphan")
    
    def __repr__(self):
        return f"<Patient {self.name}>"
    
    def __repr__(self):
        return f"<Patient(id={self.id}, name={self.name})>"