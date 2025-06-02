from app.database.setup import engine, Base, get_db_context
from app.models import Patient, Appointment
from datetime import datetime
from sqlalchemy import Date

def main_menu():
    while True:
        print("\n--- ClinicMate ---")
        print("1. Add Patient")
        print("2. View Patients")
        print("3. Search Patient by Name")
        print("4. Update Patient")
        print("5. Delete Patient")
        print("6. Add Appointment")
        print("7. View Appointments")
        print("8. Filter Appointments by Patient")
        print("9. Search Appointments by Date")
        print("10. Reschedule Appointment")
        print("11. Delete Appointment")
        print("12. Exit")
        
        choice = input("Choose an option: ")
        
        # Get a new session for each operation
        with get_db_context() as session:
            if choice == "1":
                name = input("Enter patient name: ")
                age = int(input("Enter age: "))
                contact = input("Enter contact: ")
                patient = Patient(name=name, age=age, contact=contact)
                session.add(patient)
                session.commit()
                print(f"Patient added successfully!\nID: {patient.id}\nName: {patient.name}\nAge: {patient.age}\nContact: {patient.contact}")

            elif choice == "2":
                patients = session.query(Patient).all()
                if patients:
                    print("\nCurrent Patients:")
                    for p in patients:
                        print(f"ID: {p.id}, Name: {p.name}, Age: {p.age}, Contact: {p.contact}")
                else:
                    print("No patients found.")

            elif choice == "3":
                search_name = input("Enter name to search: ")
                patients = session.query(Patient).filter(Patient.name.ilike(f"%{search_name}%"))
                if patients:
                    print("\nSearch Results:")
                    for p in patients:
                        print(f"ID: {p.id}, Name: {p.name}, Age: {p.age}, Contact: {p.contact}")
                else:
                    print("No matching patients found.")

            elif choice == "4":
                pid = int(input("Enter patient ID to update: "))
                patient = session.query(Patient).get(pid)
                if patient:
                    print(f"Updating patient: {patient.name}")
                    name = input(f"Enter new name [{patient.name}]: ") or patient.name
                    age = input(f"Enter new age [{patient.age}]: ") or patient.age
                    contact = input(f"Enter new contact [{patient.contact}]: ") or patient.contact
                    
                    patient.name = name
                    patient.age = int(age)
                    patient.contact = contact
                    session.commit()
                    print("Patient updated successfully!")
                else:
                    print("Patient not found.")

            elif choice == "5":
                pid = int(input("Enter patient ID to delete: "))
                patient = session.query(Patient).get(pid)
                if patient:
                    session.delete(patient)
                    session.commit()
                    print("Patient deleted.")
                else:
                    print("Patient not found.")

            elif choice == "6":
                pid = int(input("Enter patient ID: "))
                date_str = input("Enter appointment date & time (YYYY-MM-DD HH:MM): ")
                reason = input("Enter reason for visit: ")
                date_time = datetime.strptime(date_str, "%Y-%m-%d %H:%M")
                
                # Get patient
                patient = session.query(Patient).get(pid)
                if not patient:
                    print("Patient not found.")
                    continue
                    
                # Create appointment and link to patient
                appt = Appointment(date_time=date_time, reason=reason, patient_id=pid)
                session.add(appt)
                session.commit()
                
                print("Appointment scheduled!")

            elif choice == "7":
                appointments = session.query(Appointment).all()
                if appointments:
                    print("\nAll Appointments:")
                    for a in appointments:
                        patient = a.patient
                        print(f"ID: {a.id}")
                        print(f"Date: {a.date_time.strftime('%Y-%m-%d %H:%M')}")
                        print(f"Reason: {a.reason}")
                        print(f"Patient: {patient.name}")
                        print("-" * 50)
                else:
                    print("No appointments found.")

            elif choice == "8":
                pid = int(input("Enter patient ID: "))
                patient = session.query(Patient).get(pid)
                if patient:
                    print(f"\nAppointments for Patient: {patient.name}")
                    for appt in patient.appointments:
                        print(f"ID: {appt.id}")
                        print(f"Date: {appt.date_time.strftime('%Y-%m-%d %H:%M')}")
                        print(f"Reason: {appt.reason}")
                        print("-" * 50)
                else:
                    print("Patient not found.")

            elif choice == "9":
                date_str = input("Enter date to search (YYYY-MM-DD): ")
                date = datetime.strptime(date_str, "%Y-%m-%d")
                appointments = session.query(Appointment).filter(Appointment.date_time.cast(Date) == date).all()
                if appointments:
                    print("\nAppointments on", date_str)
                    for a in appointments:
                        print(f"ID: {a.id}")
                        print(f"Time: {a.date_time.strftime('%H:%M')}")
                        print(f"Reason: {a.reason}")
                        print("-" * 50)
                else:
                    print("No appointments found on that date.")

            elif choice == "10":
                aid = int(input("Enter appointment ID to reschedule: "))
                appt = session.query(Appointment).get(aid)
                if appt:
                    date_str = input("Enter appointment date & time (YYYY-MM-DD HH:MM) or just date (YYYY-MM-DD): ")
                    try:
                        # Try parsing as datetime
                        new_date = datetime.strptime(date_str, "%Y-%m-%d %H:%M")
                    except ValueError:
                        # If that fails, try parsing as date only
                        date_only = datetime.strptime(date_str, "%Y-%m-%d")
                        # Set a default time of 10:00 AM
                        new_date = datetime.combine(date_only.date(), datetime.strptime("10:00", "%H:%M").time())
                    appt.date_time = new_date
                    session.commit()
                    print("Appointment rescheduled!")
                else:
                    print("Appointment not found.")

            elif choice == "11":
                aid = int(input("Enter appointment ID to delete: "))
                appt = session.query(Appointment).get(aid)
                if appt:
                    session.delete(appt)
                    session.commit()
                    print("Appointment deleted.")
                else:
                    print("Appointment not found.")

            elif choice == "12":
                print("Goodbye!")
                break

            else:
                print("Invalid option. Please try again.")