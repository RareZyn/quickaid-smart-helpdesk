<div align="center">

# QuickAid — Smart Campus Helpdesk

![Next.js](https://img.shields.io/badge/Next.js-000000?style=for-the-badge&logo=next.js&logoColor=white)
![React](https://img.shields.io/badge/React-20232A?style=for-the-badge&logo=react&logoColor=61DAFB)
![Django](https://img.shields.io/badge/Django-092E20?style=for-the-badge&logo=django&logoColor=white)
![Django REST](https://img.shields.io/badge/Django_REST-ff1709?style=for-the-badge&logo=django&logoColor=white)
![Docker](https://img.shields.io/badge/Docker-2496ED?style=for-the-badge&logo=docker&logoColor=white)
![Python](https://img.shields.io/badge/Python-14354C?style=for-the-badge&logo=python&logoColor=white)

</div>

## Overview

QuickAid is a smart campus helpdesk application designed for university students and staff to submit issues, track requests, and receive timely support. Built with a Next.js frontend and Django REST Framework backend, QuickAid enables ticket submission, status tracking, automated notifications, and secure data management.

This application was developed as a Capstone Project for the MyMahir Microsoft Developer programme.

## Features

- **Issue Submission**: A modern web form interface allowing users to quickly submit helpdesk tickets with categories and priority levels.
- **Ticket Tracking**: Users can retrieve and check the status of their submitted tickets via their email addresses.
- **Role-Based Access**: Three user roles — Student/Staff, Support Agent, and Admin — each with appropriate permissions.
- **Ticket Management**: Support staff can update ticket statuses; admins can assign tickets and add internal notes.
- **Automated Notifications**: Email confirmations on ticket creation, status changes, and ticket assignments via SendGrid.

## Architecture and Technology Stack

The project uses a decoupled client-server architecture with a React frontend and Django REST API backend.

### Frontend

- **Framework**: Next.js 16 with React 19
- **Styling**: Tailwind CSS 4
- **UI Components**: Radix UI, shadcn/ui
- **Hosting**: Azure App Service

### Backend

- **Framework**: Django 6.0 with Django REST Framework
- **Database**: SQLite (development) / Azure Cosmos DB (production)
- **API**: RESTful endpoints with role-based permissions
- **Email**: SendGrid API for transactional emails
- **Security**: Azure Key Vault for secret management
- **Monitoring**: Azure Application Insights (optional)

### DevOps

- **Containerisation**: Docker and Docker Compose
- **Version Control**: Git and GitHub

## Project Structure

```text
QuickSmartAid/
├── docker-compose.yml
├── Project.md
├── README.md
│
├── frontend/                   # Next.js web application
│   ├── Dockerfile
│   ├── app/                    # Next.js App Router
│   │   ├── dashboard/          # Dashboard pages
│   │   ├── login/              # Authentication pages
│   │   ├── layout.tsx          # Root layout
│   │   └── page.tsx            # Landing page
│   ├── components/             # Reusable UI components
│   │   ├── ui/                 # shadcn/ui primitives
│   │   ├── app-sidebar.tsx     # Sidebar navigation
│   │   ├── nav-main.tsx        # Main navigation
│   │   └── ...
│   ├── hooks/                  # Custom React hooks
│   ├── lib/                    # Utility functions
│   └── public/                 # Static assets
│
├── backend/                    # Django REST API
│   ├── Dockerfile
│   ├── Pipfile                 # Python dependencies (pipenv)
│   ├── requirements.txt        # Python dependencies (pip)
│   ├── manage.py
│   ├── config/                 # Django project settings
│   │   ├── settings.py
│   │   ├── urls.py
│   │   ├── wsgi.py
│   │   └── asgi.py
│   ├── users/                  # User management app
│   │   ├── models.py           # Custom User model with roles
│   │   ├── serializers.py
│   │   └── services.py
│   ├── tickets/                # Ticket management app
│   │   ├── models.py           # Ticket, StatusHistory, AdminNote
│   │   ├── serializers.py
│   │   ├── views.py            # API views
│   │   ├── urls.py             # API route definitions
│   │   └── services.py
│   └── notifications/          # Email notification app
│       ├── models.py           # EmailLog
│       ├── serializers.py
│       └── services.py
│
└── docs/                       # Project documentation
```

## API Endpoints

| Method | Endpoint                         | Description                          | Auth      |
|--------|----------------------------------|--------------------------------------|-----------|
| POST   | `/api/tickets`                   | Create a new ticket                  | Public    |
| GET    | `/api/tickets?email={email}`     | Get tickets by email                 | Public    |
| GET    | `/api/tickets/{ticketId}`        | Get ticket details                   | Public    |
| PUT    | `/api/tickets/{ticketId}/status` | Update ticket status                 | Required  |
| PUT    | `/api/tickets/{ticketId}/assign` | Assign ticket to support staff       | Required  |
| POST   | `/api/tickets/{ticketId}/notes`  | Add internal note to ticket          | Required  |
| GET    | `/api/admin/tickets`             | Get all tickets with filters         | Required  |

## System Requirements

- **Node.js** v18+ (frontend)
- **Python** v3.9+ (backend)
- **Docker** and **Docker Compose** (optional, for containerised setup)
- **Microsoft Azure** subscription (for production deployment)
- **SendGrid** account (for email notifications)

## Getting Started

### Option 1: Docker (Recommended)

Run both frontend and backend with a single command:

```bash
docker-compose up --build
```

- Frontend: `http://localhost:3000`
- Backend API: `http://localhost:8000/api/`

### Option 2: Manual Setup

#### Frontend Setup

```bash
cd frontend
npm install
npm run dev
```

The frontend will be available at `http://localhost:3000`.

#### Backend Setup

```bash
cd backend

# Create and activate virtual environment
pipenv install
pipenv shell

# Or use pip directly
pip install -r requirements.txt

# Run migrations
python manage.py migrate

# Start the development server
python manage.py runserver
```

The backend API will be available at `http://localhost:8000/api/`.

## License

This project was created for educational purposes as part of the MyMahir Microsoft Developer programme Capstone.
