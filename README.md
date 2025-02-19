# Microservices Architecture for User & Job Management

## Overview
This project follows a microservices architecture using Django Rest Framework (DRF) and PostgreSQL. It consists of two independent services:

- **Users Service (`users_service/`)** - Manages user authentication and profiles.
- **Jobs Service (`jobs_service/`)** - Handles job listings, where each job is associated with a user from the Users Service.

Each service has its own database but communicates via REST APIs.

## Architecture Diagram
```
+------------------+       +----------------+
|  Users Service  | <---> | Jobs Service   |
|  (Port: 8000)  |       | (Port: 8001)   |
+------------------+       +----------------+
| PostgreSQL DB   |       | PostgreSQL DB  |
+------------------+       +----------------+
```

## Project Structure
```
Microservices/
│── users_service/
│   ├── users/
│   ├── manage.py
│   ├── users_service/
│── jobs_service/
│   ├── jobs/
│   ├── manage.py
│   ├── jobs_service/
```

## Setup Instructions

### Prerequisites
- Python 3.10+
- PostgreSQL
- Django & Django Rest Framework

### Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/yourrepo/microservices-project.git
   cd microservices-project
   ```
2. Set up virtual environments:
   ```bash
   python -m venv venv
   source venv/bin/activate  # For Windows: venv\Scripts\activate
   ```
3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

### Database Configuration
Each service has its own PostgreSQL database.

- **Users Service (`users_service/settings.py`)**:
  ```python
  DATABASES = {
      'default': {
          'ENGINE': 'django.db.backends.postgresql',
          'NAME': 'users_db',
          'USER': 'your_db_user',
          'PASSWORD': 'your_db_password',
          'HOST': 'localhost',
          'PORT': '5432',
      }
  }
  ```
- **Jobs Service (`jobs_service/settings.py`)**:
  ```python
  DATABASES = {
      'default': {
          'ENGINE': 'django.db.backends.postgresql',
          'NAME': 'jobs_db',
          'USER': 'your_db_user',
          'PASSWORD': 'your_db_password',
          'HOST': 'localhost',
          'PORT': '5432',
      }
  }
  ```

### Running the Services
#### Start Users Service
```bash
cd users_service
python manage.py runserver 8000
```

#### Start Jobs Service
```bash
cd jobs_service
python manage.py runserver 8001
```

## API Endpoints
### Users Service
| Method | Endpoint | Description |
|--------|---------|-------------|
| POST   | `/api/users/register/` | Register a new user |
| GET    | `/api/users/` | Get all users |
| GET    | `/api/users/{id}/` | Get user details by ID |

### Jobs Service
| Method | Endpoint | Description |
|--------|---------|-------------|
| POST   | `/api/jobs/create/` | Create a new job (requires `created_by_user`) |
| GET    | `/api/jobs/` | Get all jobs |

## Inter-Service Communication
- When a job is created, the Jobs Service verifies the user by making a request to the Users Service.
- If the user exists, the job is created; otherwise, an error is returned.

## Future Enhancements
- Implement JWT authentication
- Add asynchronous messaging using Kafka or Celery
- Deploy using Docker & Kubernetes

