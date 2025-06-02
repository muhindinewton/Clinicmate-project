from app.cli.menu import main_menu
from app.models import Patient, Appointment
from app.database.setup import engine, Base

# Ensure tables are created
Base.metadata.create_all(engine)

if __name__ == "__main__":
    main_menu()