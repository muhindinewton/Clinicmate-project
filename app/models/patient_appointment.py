from app.models.models import Base
from sqlalchemy import Column, Integer, String, ForeignKey, UniqueConstraint, DateTime
from sqlalchemy.orm import relationship
from datetime import datetime

class PatientAppointment(Base):
    __tablename__ = 'patient_appointments'
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    patient_id = Column(Integer, ForeignKey('patients.id'), nullable=False)
    appointment_id = Column(Integer, ForeignKey('appointments.id'), nullable=False)
    status = Column(String(50))  # e.g., confirmed, canceled, no-show
    role = Column(String(50))    # e.g., primary, dependent
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    
    __table_args__ = (
        UniqueConstraint('patient_id', 'appointment_id', name='uq_patient_appointment'),
    )
    
    # Relationships
    patient = relationship("Patient", back_populates="patient_appointments")
    appointment = relationship("Appointment", back_populates="patient_appointments")
    
    def __repr__(self):
        return f"<PatientAppointment(patient_id={self.patient_id}, appointment_id={self.appointment_id}, status={self.status})>"
