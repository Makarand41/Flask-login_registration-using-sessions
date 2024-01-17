# Login-Register using flask session

A simple web application for user authentication using Flask and SQLAlchemy.

## Getting Started

These instructions will help you set up and run the project on your local machine.

### Prerequisites

- Python (3.x recommended)
- Flask
- Flask-SQLAlchemy
- MySQL (or any other relational database)

### Installing

1. Clone the repository:

    ```bash
    git clone https://github.com/Makarand41/Flask-login_registration-using-sessions.git
    ```

2. Create a virtual environment (optional but recommended):

    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
    ```

3. Install dependencies:

    ```bash
    pip install -r requirements.txt
    ```

4. Set up the database:

    - Create a MySQL database named `flask` (or update `SQLALCHEMY_DATABASE_URI` in `app.py` accordingly).
    - Update database configurations in `app.py` if necessary.

5. Run the application:

    ```bash
    python app.py
    ```

6. Open your browser and go to [http://localhost:7081/](http://localhost:7081/) to access the application.

## Features

- User registration
- User login
- Session-based authentication
- Welcome page for authenticated users

## ScreenShots

![image](https://github.com/Makarand41/Flask-login_registration-using-sessions/assets/90332486/ee1ca8c1-84ae-40f5-b042-605e3f0e6d8a)

![image](https://github.com/Makarand41/Flask-login_registration-using-sessions/assets/90332486/493bc8dd-62f9-4cae-bb50-a90659c5e2be)

