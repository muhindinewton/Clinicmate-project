from app.models.models import Base
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from app.models.patient_appointment import PatientAppointment

class Patient(Base):
    __tablename__ = 'patients'
    
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    age = Column(Integer)
    contact = Column(String)
    
    # Many-to-many relationship through junction table
    patient_appointments = relationship("PatientAppointment", back_populates="patient", cascade="all, delete-orphan")
    
    @property
    def appointments(self):
        """Get all appointments associated with this patient."""
        return [pa.appointment for pa in self.patient_appointments]
    
    def add_appointment(self, appointment, status='confirmed', role=None):
        """Add an appointment for this patient."""
        pa = PatientAppointment(
            patient_id=self.id,
            appointment_id=appointment.id,
            status=status,
            role=role
        )
        return pa
    
    def __repr__(self):
        return f"<Patient(id={self.id}, name={self.name})>"