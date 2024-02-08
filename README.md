# Flask Cafe Management System

This Flask application serves as a management system for cafes, allowing users to view cafes, add new cafes, and manage cafe information. Below is an overview of the functionality and structure of the application.

## Features

- **User Authentication**: Users can register as administrators and login to access administrative features.
- **Cafe Management**: Administrators can add new cafes, view existing cafes, and delete cafes.
- **User Interface**: The application provides a user-friendly interface for users to interact with.

## File Structure

- **`app.py`**: Main Flask application file containing route definitions and configuration.
- **`forms.py`**: Defines forms using Flask-WTF for user input validation.
- **`templates/`**: Directory containing HTML templates for rendering pages.
- **`static/`**: Directory for static files like CSS, JavaScript, and images.
- **`cafes.db`**: SQLite database file for storing cafe and admin data.

## Dependencies

- **Flask**: Micro web framework for Python.
- **Flask-SQLAlchemy**: Flask extension for database integration using SQLAlchemy.
- **Flask-Bootstrap5**: Integration of Bootstrap 5 with Flask for styling.
- **Flask-Login**: Provides user session management for Flask applications.
- **Werkzeug**: A utility library for WSGI, including password hashing.

## Setup and Usage

1. Install dependencies: `pip install Flask Flask-SQLAlchemy Flask-Bootstrap5 Flask-Login`
2. Clone the repository: `git clone https://github.com/your_username/your_repo.git`
3. Navigate to the project directory: `cd your_repo`
4. Run the application: `python app.py`
5. Access the application in your web browser at `http://localhost:5000`

## Usage

- Visit the homepage to view a list of cafes.
- Register as an administrator or log in with existing credentials.
- Add new cafes by filling out the form in the "Add Cafe" section.
- View details of a cafe by clicking on its name.
- Administrators can delete cafes by clicking on the delete button next to each cafe.

## Contributors

- Hemant Raj
