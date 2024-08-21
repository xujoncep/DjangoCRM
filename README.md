# DjangoCRM
A Django-based CRM system designed to manage customer interactions, track sales, and organize customer data. Features include customer and contact management, sales tracking, reporting, and user management. Built with Django and Django REST Framework, and supports customization and extension.

# Django CRM Project

## Overview
A CRM system built with Django to manage customer interactions, track sales, and organize customer data.

## Features
- Customer Management
- Contact Management
- Sales Tracking
- Reports
- User Management
- Search and Filter

## Technologies Used
- Django
- Django REST Framework
- SQLite (default; can be replaced with PostgreSQL or MySQL)
- Bootstrap

## Installation
1. Clone the repository:
   `git clone https://github.com/yourusername/django-crm-project.git`
2. Navigate to the project directory:
   `cd django-crm-project`
3. Create a virtual environment:
   `python -m venv env`
4. Activate the virtual environment:
   - On Windows: `.\env\Scripts\activate`
   - On macOS/Linux: `source env/bin/activate`
5. Install dependencies:
   `pip install -r requirements.txt`
6. Apply migrations:
   `python manage.py migrate`
7. Create a superuser:
   `python manage.py createsuperuser`
8. Run the development server:
   `python manage.py runserver`
   The application will be available at `http://127.0.0.1:8000/`.

## Usage
- Admin Interface: `http://127.0.0.1:8000/admin/`
- Manage customers, track sales, and generate reports.

## Configuration
Settings are in `crm_project/settings.py`. Adjust database settings, secret key, etc.

## Contributing
1. Fork the repository.
2. Create a branch: `git checkout -b feature-branch`
3. Commit changes: `git commit -am 'Add new feature'`
4. Push: `git push origin feature-branch`
5. Create a Pull Request.

## License
MIT License. See the LICENSE file for details.

## Contact
For questions, email [your.email@example.com](mailto:your.email@example.com).
