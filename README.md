# Student Task Manager

A beginner-friendly Django web application inspired by the **To-Do Web App** idea in the GeeksforGeeks Django Projects list. This repository is an independent implementation with its own models, views, templates, styling, and sample-data command.

## Features

- Create, edit, delete, and complete tasks
- Set a priority and optional due date
- Search tasks by title or description
- Filter tasks by all, pending, or completed
- Dashboard counters for total, pending, and completed tasks
- Django Admin support
- SQLite database (created locally by Django migrations)
- Responsive dark-themed interface

> This is a learning/demo project. It does not include user accounts, so do not use it to store private information.

## Requirements

- Python 3.10 or newer
- VS Code (recommended)
- Internet access for the first-time Django installation

## Run on Windows with VS Code

1. Download or clone this repository and open the `student-task-manager` folder in VS Code.
2. Open **Terminal → New Terminal**.
3. Create a virtual environment:

   ```powershell
   py -m venv venv
   ```

4. Activate it:

   ```powershell
   .\venv\Scripts\Activate.ps1
   ```

   If PowerShell blocks activation, use Command Prompt and run `venv\\Scripts\\activate.bat`, or run `Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass` in the current PowerShell terminal and activate again.

5. Install the dependency:

   ```powershell
   python -m pip install -r requirements.txt
   ```

6. Create the database tables:

   ```powershell
   python manage.py migrate
   ```

7. Add demonstration/sample tasks:

   ```powershell
   python manage.py seed_tasks
   ```

8. Start the local development server:

   ```powershell
   python manage.py runserver
   ```

9. Open **http://127.0.0.1:8000/** in your browser.

Stop the server with `Ctrl+C`.

## Optional: Django Admin

Create an admin account:

```powershell
python manage.py createsuperuser
```

Then visit **http://127.0.0.1:8000/admin/** and sign in.

## Project structure

```text
student-task-manager/
├── manage.py
├── requirements.txt
├── README.md
├── .gitignore
├── student_task_manager/
│   ├── settings.py
│   ├── urls.py
│   ├── asgi.py
│   └── wsgi.py
└── tasks/
    ├── management/commands/seed_tasks.py
    ├── migrations/0001_initial.py
    ├── templates/tasks/
    │   ├── base.html
    │   ├── dashboard.html
    │   └── task_form.html
    ├── static/tasks/style.css
    ├── admin.py
    ├── apps.py
    ├── forms.py
    ├── models.py
    ├── urls.py
    ├── views.py
    └── tests.py
```

## How it works (useful for your viva)

- **Model (`tasks/models.py`)**: defines the `Task` fields stored in SQLite.
- **Form (`tasks/forms.py`)**: validates task input before saving.
- **View (`tasks/views.py`)**: handles requests and decides what data/templates to return.
- **URL configuration (`tasks/urls.py`)**: maps browser paths to views.
- **Templates (`tasks/templates/`)**: render the HTML pages.
- **CSS (`tasks/static/`)**: controls the page styling.
- **Migration (`tasks/migrations/`)**: creates the database table from the model.
- **Management command (`seed_tasks`)**: inserts sample data for the demonstration.

The app follows Django's **MVT** pattern: Model, View, Template.

## Upload to GitHub

### Option A — upload using Git in VS Code

1. Create a **new empty repository** on GitHub named `student-task-manager`. Do not initialize it with a README if you plan to push this folder as-is.
2. In the VS Code terminal, ensure you are in this folder and your virtual environment is active.
3. Run:

   ```powershell
   git init
   git add .
   git commit -m "Build Student Task Manager with Django"
   git branch -M main
   git remote add origin https://github.com/YOUR-USERNAME/student-task-manager.git
   git push -u origin main
   ```

4. Replace `YOUR-USERNAME` with your GitHub username. GitHub may ask you to authenticate in the browser.

If Git says `remote origin already exists`, run `git remote set-url origin https://github.com/YOUR-USERNAME/student-task-manager.git` and then push again.

### Option B — upload through the GitHub website

You can create the repository on GitHub, choose **Add file → Upload files**, and upload the project files/folders. Git is recommended because it makes later updates easier.

## Before the class demonstration

- Run `python manage.py check`
- Run `python manage.py test`
- Run `python manage.py seed_tasks`
- Start the server and demonstrate add, edit, complete, delete, search, and filter actions.
- Explain the model, form, view, URL, template, and database flow in your own words.

## Reference

Project idea: GeeksforGeeks — [Django Projects](https://www.geeksforgeeks.org/python/django-projects/) and [Python ToDo WebApp using Django](https://www.geeksforgeeks.org/python/python-todo-webapp-using-django/).

This repository is an educational implementation based on the general project idea, not a copy of the reference source code.
