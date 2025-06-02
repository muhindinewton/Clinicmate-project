from app.database.setup import SessionLocal
from app.models import Patient, Appointment, PatientAppointment
from datetime import datetime

def test_database_relationships():
    # Create a session
    session = SessionLocal()
    
    try:
        # Create test patients
        patient1 = Patient(name="John Doe", age=30, contact="john@example.com")
        patient2 = Patient(name="Jane Doe", age=28, contact="jane@example.com")
        
        # Add to session and commit patients first to get their IDs
        session.add(patient1)
        session.add(patient2)
        session.commit()  # Commit to get IDs
        
        # Create a group therapy appointment
        appointment = Appointment(
            date_time=datetime.now(),
            reason="Group Therapy Session"
        )
        
        # Add to session and commit appointment to get its ID
        session.add(appointment)
        session.commit()  # Commit to get ID
        
        # Add patients to the appointment with different roles
        pa1 = PatientAppointment(
            patient_id=patient1.id,
            appointment_id=appointment.id,
            status="confirmed",
            role="primary"
        )
        pa2 = PatientAppointment(
            patient_id=patient2.id,
            appointment_id=appointment.id,
            status="confirmed",
            role="dependent"
        )
        
        # Add to session
        session.add(pa1)
        session.add(pa2)
        
        # Commit the transaction
        session.commit()
        
        # Test the relationships
        print("\nTesting Database Relationships:")
        print("-" * 50)
        
        # Test getting patients from appointment
        print(f"\nAppointment: {appointment.reason}")
        print("Patients in this appointment:")
        for pa in appointment.patient_appointments:
            print(f"- {pa.patient.name} (Role: {pa.role}, Status: {pa.status})")
        
        # Test getting appointments from patient
        print(f"\nPatient: {patient1.name}")
        print("Appointments:")
        for pa in patient1.patient_appointments:
            print(f"- {pa.appointment.reason} (Status: {pa.status})")
        
        # Test updating status
        print("\nUpdating patient status...")
        pa1.status = "rescheduled"
        session.commit()
        print(f"New status: {pa1.status}")
        
    finally:
        # Close the session
        session.close()

if __name__ == "__main__":
    test_database_relationships()
