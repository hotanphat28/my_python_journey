# CS50 Froshims

A web application for registering users for sports events, based on CS50's "Froshims" example.

## Features

- **User Registration**: Sign up for events (Basketball, Soccer, Swimming).
- **Admin Login**: Secure(ish) login to view registrants (Username: `admin`, Password: `admin`).
- **Registrant Management**: View and delete registrants from the database.
- **Session Management**: Uses `flask_session` for managing user sessions.

## Tech Stack

- **Flask**: Web framework.
- **SQLite**: Database for storing registrants.
- **Flask-Session**: Server-side session support.

## Installation & Usage

1. Navigate to the directory:
   ```bash
   cd tutorials/cs50-froshims
   ```

2. Install Dependencies:
   Navigate to the specific project directory and install the required packages (if a `requirements.txt` is present) or install specific libraries as noted in the project README.
   ```bash
   pip install Flask Flask-Session
   ```

3. Run the application (ensure your virtual environment is active):
   ```bash
   python app.py
   ```

4. Open your browser to `http://127.0.0.1:5000`.

## Notes
- The database `froshims.db` is included (or created via sqlite3 logic in `app.py`).
- This is a tutorial/demo project.
