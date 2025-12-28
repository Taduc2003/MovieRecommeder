# Movie Recommender System

A Django-based recommendation engine using Collaborative Filtering (SVD) with Celery task queue for asynchronous ML operations.

## Stack

- **Backend**: Django 4.0.7
- **ML Algorithm**: Surprise (scikit-surprise) - SVD Collaborative Filtering
- **Task Queue**: Celery + Redis
- **Database**: PostgreSQL 13
- **Containerization**: Docker & Docker Compose

## Quick Start

### 1. Clone and Setup
```bash
git clone https://github.com/Taduc2003/MovieRecommeder
cd MovieRecommeder
```

### 2. Create Virtual Environment
```bash
python -m venv venv
.\venv\Scripts\activate  # Windows
source venv/bin/activate  # Linux/Mac
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
pip install scikit-surprise --no-build-isolation
```

### 4. Setup Environment
Create `src/.env`:
```
CELERY_BROKER_REDIS_URL='redis://localhost:6380'
DJANGO_DEBUG='1'
SECRET_KEY='your-secret-key-here'
```

Generate SECRET_KEY:
```bash
python -c 'from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())'
```

### 5. Start Services
```bash
docker compose up -d
```

### 6. Database Setup
```bash
cd src
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```

## Documentation

For detailed documentation on:
- ML model and training pipeline
- Deployment architecture
- Setup and configuration
- Monitoring and evaluation

Visit: [https://Taduc2003.github.io/MovieRecommeder/](https://Taduc2003.github.io/MovieRecommeder/)

Or see [docs/mkdocs_project/README.md](docs/mkdocs_project/README.md) for local documentation setup.

## Project Structure

- `src/` - Django application code
- `docs/mkdocs_project/` - Technical documentation (MkDocs)
- `docker-compose.yaml` - Service orchestration
- `requirements.txt` - Python dependencies
Run migrations if needed:
```
python manage.py makemigrations
python manage.py migrate
```
Then:
```
python manage.py loader 200_000 --movies
```

10. Load in Rating Data 
```
python manage.py dataset_ratings
```

11. Train your ML Model
```
python manage.py train --epochs 20
```
When your worker is running, you can also do `python manage.py train --async --epochs 20`

12. Run the Worker
```
celery -A cfehome worker -l info --beat
```

13. Rate some movies
With the server running (`python manage.py runserver`) open up [http://localhost:8000/accounts/login](http://localhost:8000/login) and rate some movies.

14. Create recommendation predictions

```
python manage.py recommend
```
> This can also be done as a periodic task

15. Review Predictions on Dashboard

16. Celebrate!

## Helpful Guides
- [Using a Cloud-based Redis Server](https://www.codingforentrepreneurs.com/blog/remote-redis-servers-for-development/)
- [Install Redis on Windows](https://www.codingforentrepreneurs.com/blog/redis-on-windows/)
- [Install Redis on macOS](https://www.codingforentrepreneurs.com/blog/install-redis-mac-and-linux)
- [Celery + Redis + Django Setup Guide](https://www.codingforentrepreneurs.com/blog/celery-redis-django/)

## References

- **Original Recommender Project:** https://github.com/codingforentrepreneurs/recommender
