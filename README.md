# Doctor Appointment System

This project is a Django-based Doctor Appointment System, developed to manage administrative tasks, user authentication, and basic static file handling.

## Features Implemented/Improved:

*   **User Authentication:**
    *   Admin Login functionality.
    *   User Registration functionality.
*   **Form Validation:**
    *   Enhanced form validation for registration, including unique username/email and password strength checks.
    *   Custom `AdminRegisterForm` and `AdminLoginForm` for tailored field rendering and validation.
*   **Static Files Management:**
    *   Correct configuration of `STATIC_URL`, `STATICFILES_DIRS`, and `STATIC_ROOT` in `settings.py`.
    *   Resolved issues with loading CSS/JS/Image assets in templates.
*   **Template Inheritance:**
    *   Implemented a dedicated `auth_base.html` template for consistent layout across authentication pages (login, register).
    *   `admin_login.html` and `admin_register.html` now extend `auth_base.html`.
*   **Dynamic Alert Messaging:**
    *   Integrated Django's messages framework to display feedback to users (e.g., login success, logout confirmation, validation errors).
    *   Alerts are styled using Bootstrap (`alert-{{ message.tags }}` with `alert-dismissible`) and automatically hide after 10 seconds.
*   **Login Redirection:**
    *   Implemented the `@login_required` decorator for protected views (e.g., dashboard).
    *   Configured `LOGIN_URL` in `settings.py` to ensure unauthenticated users are redirected to the correct login page.

## Getting Started:

1.  **Clone the repository:**
    ```bash
    git clone https://github.com/nirajnagrale7/Doctor_Appointment.git
    cd Doctor_Appointment
    ```
2.  **Set up virtual environment:**
    ```bash
    python3 -m venv .venv
    source .venv/bin/activate
    pip install -r requirements.txt # (Assuming you have a requirements.txt, if not, install Django and psycopg2_binary)
    ```
3.  **Database setup:**
    *   Ensure PostgreSQL is running and you have a database named `doctor_appointment_db` with user `postgres` and password `redwine` (as per `settings.py`).
    *   Run migrations:
        ```bash
        python manage.py migrate
        ```
4.  **Create a superuser:**
    ```bash
    python manage.py createsuperuser
    ```
5.  **Run the development server:**
    ```bash
    python manage.py runserver
    ```

## Usage:

*   Access the admin registration page at `/admin_panel/register/` to create an admin account.
*   Log in at `/admin_panel/login/`.
*   Access the dashboard at `/admin_panel/dashboard/`.

This `README.md` provides an overview of the project and its current state.
