# API with FastAPI

This is a simple API built with FastAPI using MongoDB and Firebase Authentication (optional).

## Prerequisites

- Python (v3.10 or higher recommended)
- MongoDB Atlas account (or local MongoDB)
- Firebase project (optional, for authentication)

## Technology Stack

- **Framework**: FastAPI
- **Database**: MongoDB
- **Authentication**: Firebase Admin SDK (optional)
- **Documentation**: Swagger

## Installation

1. Clone the repository:

```bash
git clone <repository-url>
cd FastAPI-backend
```

2. Create your environment

```bash
python -m venv .venv
source .venv/bin/activate
```

3. Add your Firebase Admin SDK JSON to the project root as service-account.json (optional)

4. Configure environment variables in .env

```bash
# Database Configuration
MONGODB_URI=mongodb+srv://username:password@cluster.mongodb.net/
DB_NAME=database

# Optional
GOOGLE_APPLICATION_CREDENTIALS="./service-account.json"
```

5. Install dependencies:

```bash
pip install -r requirements.txt
```

6. Run the server:

```bash
uvicorn app.main:app --reload
```

## API Documentation

Once the application is running, access the interactive API documentation:

- **Swagger UI**: http://127.0.0.1:8000/docs
