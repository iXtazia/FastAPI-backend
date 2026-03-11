# API with FastAPI

This is a simple API built with FastAPI using Firebase Authentication.

## Prerequisites

- Python (v3.0.0 or higher)

## Technology Stack

- **Framework**: FastAPI
- **Documentation**: Swagger

## Installation

1. Clone the repository:

```bash
git clone <repository-url>
cd FastAPI-backend
```

2. Create environment

```bash
source .venv/bin/activate
```

3. Configure environment variables in .env

```bash
# Database Configuration
MONGODB_URI=mongodb+srv://username:password@cluster.mongodb.net/
DB_NAME=database
```

4. Install dependencies:

```bash
pip install -r requirements.txt
```

5. Run the server:

```bash
fastapi dev
```

## API Documentation

Once the application is running, access the interactive API documentation:

- **Swagger UI**: http://127.0.0.1:8000/docs
