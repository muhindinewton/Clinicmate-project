# ClinicMate

ClinicMate is a modern command-line clinic management system built with Python. It simplifies how clinics manage patient records and appointments using a clean, modular design.

## Features

### Patient Management
- Add, view, update, and delete patient records
- Track medical and appointment history
- Search patients by name or contact

### Appointment Management
- Schedule, view, update, and delete appointments
- Reschedule with ease
- Search by date or patient

## Tech Stack
- Python 3.8
- SQLAlchemy (ORM)
- SQLite database
- Modular and extensible architecture

## Why ClinicMate?
- Easy to Use: Clean command-line interface
- Reliable: Built with robust, well-tested Python libraries
- Scalable: Modular code for easy feature expansion
- Efficient: Fast and responsive operations
- Secure: Ensures data consistency and integrity

## Installation

### Clone the repository:
```bash
git clone [repository-url]
cd Clinicmate-project
```

### Set up a virtual environment:
```bash
python -m venv .venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate
```

### Install dependencies:
```bash
pip install -r requirements.txt
```

## Usage

### Start the app:
```bash
python main.py
```

You’ll see a menu where you can:
- Manage Patients: Add, view, update, delete, search
- Manage Appointments: Schedule, view, filter, reschedule, delete

## Database
- Uses SQLite (clinic.db)
- Created automatically on first run
- Managed via SQLAlchemy ORM

## Project Structure
```
Clinicmate-project/
├── app/
│   ├── cli/                # CLI menus
│   ├── database/           # DB config
│   └── models/             # Data models
├── main.py                 # Entry point
├── requirements.txt        # Dependencies
└── README.md               # Documentation
```

## Contributing

1. Fork the repo
1. Create your branch: `git checkout -b feature-name`
1. Commit and push your changes
1. Open a pull request

## License
Licensed under the MIT License.

