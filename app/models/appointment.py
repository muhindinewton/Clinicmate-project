from app.models.models import Base
from sqlalchemy import Column, Integer, String, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from datetime import datetime

class Appointment(Base):
    __tablename__ = 'appointments'
    
    id = Column(Integer, primary_key=True)
    date_time = Column(DateTime)
    reason = Column(String)
    patient_id = Column(Integer, ForeignKey('patients.id'))
    
    # One-to-many relationship with patient
    patient = relationship("Patient", back_populates="appointments")
    
    def __repr__(self):
        return f"<Appointment(id={self.id}, date_time={self.date_time}, reason={self.reason})>"