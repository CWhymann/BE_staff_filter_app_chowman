# BE Staff Filter App

## Quick Start

Clone the repository:

```bash
git clone <repository-url>
cd BE_staff_filter_app
```

Create a virtual environment:

```bash
python -m venv .venv
```

Activate the virtual environment:

**Windows**

```bash
.venv\Scripts\activate
```

**macOS / Linux**

```bash
source .venv/bin/activate
```

Install the required dependencies:

```bash
pip install -r requirements.txt
```

Apply the database migrations:

```bash
python manage.py migrate
```

Start the development server:

```bash
python manage.py runserver
```

Open your browser and navigate to:

```text
http://127.0.0.1:8000/
```

---

## Project Overview

I developed this Django application as part of a backend development task.

The goal of the task was to create an application that manages employee data and provides a filtering functionality to search and display employee records based on specific criteria.

In this project, I implemented the data structure, backend logic, filtering functionality, and the connection between the Django backend and the user interface.

---

## Task Requirements

For this task, I implemented the following requirements:

- I created a structured employee data model.
- I implemented the storage and management of employee information.
- I developed a web interface to display employee records.
- I added filtering functionality to search employee data.
- I created a clear presentation of the filtered results.

---

## My Implementation

### Project Setup

I created and configured the Django project structure as the foundation of the application.

I prepared the required components, including:

- Django project configuration
- Application setup
- Database configuration
- URL routing
- Template integration

---

### Data Model

I created an employee model to represent the required employee information.

With this model, I implemented the database structure needed to store and retrieve employee records using Django's ORM.

I created and applied migrations to connect the model with the database.

---

### Backend Development

I implemented the backend logic using Django.

This includes:

- Retrieving employee data from the database
- Processing user requests
- Implementing the filtering functionality
- Connecting backend logic with the templates

---

### User Interface

I created the user interface to display employee information and provide the filtering options.

Users can view employee records and filter the displayed results based on the implemented criteria.

---

## Testing

I tested the application locally to verify that:

- The Django project starts correctly.
- Employee data is displayed correctly.
- Database operations work as expected.
- The filtering functionality returns the correct results.

---

## Result

I created a functional Django web application that allows employee data to be managed and filtered.

This repository contains my complete implementation of the backend task, including the project structure, database model, backend logic, and user interface integration.
