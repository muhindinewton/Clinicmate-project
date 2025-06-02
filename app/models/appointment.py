from app.models.models import Base
from sqlalchemy import Column, Integer, DateTime, String, ForeignKey
from sqlalchemy.orm import relationship
from datetime import datetime
from app.models.patient_appointment import PatientAppointment

class Appointment(Base):
    __tablename__ = 'appointments'
    
    id = Column(Integer, primary_key=True)
    date_time = Column(DateTime)
    reason = Column(String)
    
    # Many-to-many relationship through junction table
    patient_appointments = relationship("PatientAppointment", back_populates="appointment", cascade="all, delete-orphan")
    
    @property
    def patients(self):
        """Get all patients associated with this appointment."""
        return [pa.patient for pa in self.patient_appointments]
    
    def add_patient(self, patient, status='confirmed', role=None):
        """Add a patient to this appointment."""
        pa = PatientAppointment(
            patient_id=patient.id,
            appointment_id=self.id,
            status=status,
            role=role
        )
        return pa
    
    def __repr__(self):
        return f"<Appointment(id={self.id}, date_time={self.date_time}, reason={self.reason})>"