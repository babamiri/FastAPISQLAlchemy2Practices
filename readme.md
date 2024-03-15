# FastAPI Project with SQLAlchemy 2 and Alembic

This is a FastAPI project utilizing SQLAlchemy 2 for ORM and Alembic for database migrations.

## Setup

1. **Clone the repository:**

    ```bash
    git clone <repository_url>
    cd <project_folder>
    ```

2. **Install dependencies:**

    ```bash
    pip install -r requirements.txt
    ```

3. **Setup environment variables:**

    - Copy the provided `env.example` file to `.env`:

        ```bash
        cp env.example .env
        ```

    - Modify `.env` file according to your environment configuration.

4. **Database Setup:**

    - Ensure your database server is up and running.
    - Modify the SQLAlchemy database URI in the `.env` file to point to your database.

5. **Run Alembic Migrations:**

    ```bash
    alembic revision --autogenerate -m "create models"    
    alembic upgrade head
    ```

    This command will apply all pending migrations to your database.

## Running the FastAPI Application

Ensure that your environment is properly configured and your database is accessible.

```bash
uvicorn app.main:app --host 0.0.0.0 --port 8000
