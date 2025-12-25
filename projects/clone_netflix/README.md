# Flask Netflix Clone

A simple web application built with Flask that implements user authentication and rate limiting. This project serves as a foundation for a Netflix clone, focusing on secure user management and basic dashboard functionality.

## Features

- **User Authentication**: Secure registration and login flows.
- **Data Security**: Password hashing using `Flask-Bcrypt`.
- **Rate Limiting**: Brute-force protection on login routes (limit: 5 attempts per minute) using `Flask-Limiter` and Redis.
- **Database Management**: SQLAlchemy ORM with Migrations support.
- **Protected Routes**: Dashboard access is restricted to logged-in users.

## Tech Stack

- **Backend**: Python, Flask
- **Database**: SQLite (default), SQLAlchemy
- **Caching/Rate Limiting**: Redis
- **Frontend**: HTML5, CSS3, Jinja2 Templates
- **Authentication**: Flask-Login

## Prerequisites

- Python 3.8+
- [Redis](https://redis.io/) server running locally (default: `localhost:6379`).

## Installation

1. **Clone the repository**
   ```bash
   # If you haven't already
   cd projects/clone_netflix
   ```

2. **Install Dependencies**:
   Navigate to the specific project directory and install the required packages (if a `requirements.txt` is present) or install specific libraries as noted in the project README.
   ```bash
   pip install -r requirements.txt
   ```

3. **Initialize the Database**
   Since migrations are included, upgrade the database to the latest schema:
   ```bash
   flask db upgrade
   ```

4. **Start Redis**
   Ensure your Redis server is running, as it is required for rate limiting.
   ```bash
   redis-server
   ```

5. **Run the Application**
   ```bash
   python app.py
   ```
   The app will be accessible at `http://127.0.0.1:5000`.

## Project Structure

- `app.py`: Main application entry point, route definitions, and configuration.
- `instance/`: Contains the SQLite database file.
- `migrations/`: Database migration scripts.
- `templates/`: HTML templates for pages (Login, Register, Dashboard).
- `static/`: Static assets (CSS).
