from app.database.setup import SessionLocal
from app.models import Patient, Appointment
from datetime import datetime

def main_menu():
    session = SessionLocal()
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

        if choice == "1":
            with SessionLocal() as session:
                try:
                    name = input("Enter patient name: ")
                    age = int(input("Enter age: "))
                    contact = input("Enter contact: ")
                    patient = Patient(name=name, age=age, contact=contact)
                    session.add(patient)
                    session.commit()
                    print("\nPatient added successfully!")
                    print(f"ID: {patient.id}")
                    print(f"Name: {patient.name}")
                    print(f"Age: {patient.age}")
                    print(f"Contact: {patient.contact}")
                except Exception as e:
                    session.rollback()
                    print(f"Error adding patient: {str(e)}")

        elif choice == "2":
            with SessionLocal() as session:
                try:
                    patients = session.query(Patient).all()
                    if patients:
                        print("\nCurrent Patients:")
                        for p in patients:
                            print(f"ID: {p.id}, Name: {p.name}, Age: {p.age}, Contact: {p.contact}")
                    else:
                        click.echo(click.style("\nNo patients found.", fg='yellow'))
                except Exception as e:
                    print(f"Error viewing patients: {str(e)}")

        elif choice == "3":
            keyword = input("Enter name to search: ")
            results = session.query(Patient).filter(Patient.name.ilike(f"%{keyword}%")).all()
            for p in results:
                print(f"{p.id}: {p.name}, {p.age} years, Contact: {p.contact}")

        elif choice == "4":
            pid = int(input("Enter patient ID to update: "))
            patient = session.query(Patient).filter_by(id=pid).first()
            if patient:
                patient.name = input(f"New name (current: {patient.name}): ") or patient.name
                patient.age = int(input(f"New age (current: {patient.age}): ") or patient.age)
                patient.contact = input(f"New contact (current: {patient.contact}): ") or patient.contact
                session.commit()
                print("Patient updated.")
            else:
                click.echo(click.style("Patient not found.", fg='red'))

        elif choice == "5":
            pid = int(input("Enter patient ID to delete: "))
            patient = session.query(Patient).filter_by(id=pid).first()
            if patient:
                session.delete(patient)
                session.commit()
                print("Patient deleted.")
            else:
                click.echo(click.style("Patient not found.", fg='red'))

        elif choice == "6":
            pid = int(input("Enter patient ID: "))
            date_str = input("Enter appointment date & time (YYYY-MM-DD HH:MM): ")
            reason = input("Enter reason for visit: ")
            date_time = datetime.strptime(date_str, "%Y-%m-%d %H:%M")
            appt = Appointment(date_time=date_time, reason=reason, patient_id=pid)
            session.add(appt)
            session.commit()
            print("Appointment scheduled!")

        elif choice == "7":
            appointments = session.query(Appointment).all()
            if appointments:
                print("\nAll Appointments:")
                for a in appointments:
                    print(f"ID: {a.id}, Date: {a.date_time.strftime('%Y-%m-%d %H:%M')}, Reason: {a.reason}, Patient ID: {a.patient_id}")
            else:
                print("No appointments found.")

        elif choice == "8":
            pid = int(input("Enter patient ID: "))
            appointments = session.query(Appointment).filter_by(patient_id=pid).all()
            for a in appointments:
                print(f"{a.id}: {a.date_time} - {a.reason}")

        elif choice == "9":
            date_str = input("Enter date to search (YYYY-MM-DD): ")
            date_obj = datetime.strptime(date_str, "%Y-%m-%d").date()
            appointments = session.query(Appointment).all()
            for a in appointments:
                if a.date_time.date() == date_obj:
                    print(f"{a.id}: {a.date_time} - {a.reason} (Patient ID {a.patient_id})")

        elif choice == "10":
            appt_id = int(input("Enter appointment ID to reschedule: "))
            appointment = session.query(Appointment).filter_by(id=appt_id).first()
            if appointment:
                new_date_str = input("Enter new date & time (YYYY-MM-DD HH:MM): ")
                new_date = datetime.strptime(new_date_str, "%Y-%m-%d %H:%M")
                appointment.date_time = new_date
                session.commit()
                print("Appointment rescheduled.")
            else:
                click.echo(click.style("Appointment not found.", fg='red'))

        elif choice == "11":
            appt_id = int(input("Enter appointment ID to delete: "))
            appointment = session.query(Appointment).filter_by(id=appt_id).first()
            if appointment:
                session.delete(appointment)
                session.commit()
                print("Appointment deleted.")
            else:
                click.echo(click.style("Appointment not found.", fg='red'))

        elif choice == "12":
            session.close()
            print("Goodbye!")
            break
        else:
            print("Invalid input. Try again.")