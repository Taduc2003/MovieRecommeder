# Môi trường chạy và công cụ sử dụng

## Stack công nghệ

| Thành phần | Công cụ | Phiên bản | Chức năng |
|-----------|---------|----------|----------|
| **Web Framework** | Django | 4.0.7 | Web application & ORM |
| **ML Framework** | scikit-surprise | 1.1.4 | Collaborative Filtering (SVD) |
| **Task Queue** | Celery | 5.0+ | Async task execution |
| **Message Broker** | Redis | 4.3.4 | Task queue backend |
| **Scheduler** | django-celery-beat | 2.3.0 | Cron-like task scheduling |
| **Task Results** | django-celery-results | 2.4.0 | Store task results in DB |
| **Data Processing** | Pandas | 1.5.3 | Data manipulation |
| **NumPy** | NumPy | 1.23.5 | Numerical computing |
| **Database** | PostgreSQL | 13 | Persist data & Celery results |
| **Web Server** | Gunicorn | 21.2.0 | WSGI application server |
| **Containerization** | Docker & Compose | - | Environment orchestration |
| **Utilities** | python-decouple | 3.6 | Environment configuration |

## Môi trường Development

### Setup Virtual Environment

```bash
# Create virtual environment
python3.8 -m venv venv

# Activate (Linux/Mac)
source venv/bin/activate

# Activate (Windows)
.\venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt
pip install scikit-surprise --no-build-isolation
```

### Run Django Development Server

```bash
cd src
python manage.py makemigrations
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```

Access at: http://localhost:8000

### Run Celery Worker

**Terminal 1:**
```bash
cd src
celery -A cfehome worker -l info
```

### Run Celery Beat

**Terminal 2:**
```bash
cd src
celery -A cfehome beat -l info
```

## Môi trường Production (Docker)

### Docker Compose Setup

```bash
# Start all services
docker-compose up -d

# View logs
docker-compose logs -f

# Stop services
docker-compose down
```

### Services

**docker-compose.yaml:**

```yaml
version: '3.8'

services:
  db:
    image: postgres:13
    environment:
      POSTGRES_DB: recommender
      POSTGRES_USER: recommender
      POSTGRES_PASSWORD: recommender
    volumes:
      - postgres_data:/var/lib/postgresql/data
    ports:
      - "5432:5432"

  redis:
    image: redis
    ports:
      - "6380:6379"
    volumes:
      - redis_data:/data
    command: redis-server --appendonly yes

  web:
    build: .
    command: gunicorn cfehome.wsgi:application --bind 0.0.0.0:8000
    volumes:
      - ./src:/app
    ports:
      - "8000:8000"
    depends_on:
      - db
      - redis
    environment:
      - DJANGO_SETTINGS_MODULE=cfehome.settings
      - CELERY_BROKER_URL=redis://redis:6379/0

  worker:
    build: .
    command: celery -A cfehome worker -l info
    volumes:
      - ./src:/app
    depends_on:
      - db
      - redis
    environment:
      - DJANGO_SETTINGS_MODULE=cfehome.settings
      - CELERY_BROKER_URL=redis://redis:6379/0

volumes:
  postgres_data:
  redis_data:
```

## Cơ sở dữ liệu

### PostgreSQL 13

| Thông số | Giá trị |
|----------|--------|
| **Database** | `recommender` |
| **Host** | `db` (Docker) hoặc `localhost:5432` |
| **User** | `recommender` |
| **Password** | `recommender` |

### Main Tables

```
movies_movie                          # Thông tin phim
ratings_rating                        # Xếp hạp từ users
suggestions_suggestion                # Gợi ý được sinh
django_celery_beat_periodictask      # Scheduled tasks
django_celery_results_taskresult     # Task execution results
```

### Redis

| Thông số | Giá trị |
|----------|--------|
| **Host** | `redis:6379` (Docker) hoặc `localhost:6380` |
| **Purpose** | Celery message broker |
| **Data** | Queue tasks (not persistent) |

## Cấu hình Django (settings.py)

### Celery Configuration

```python
CELERY_BROKER_URL = config('CELERY_BROKER_REDIS_URL', 
                           default='redis://localhost:6379')
CELERY_RESULT_BACKEND = 'django-db'
CELERY_BEAT_SCHEDULER = 'django_celery_beat.schedulers.DatabaseScheduler'
```

### Database Configuration

```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'recommender',
        'USER': 'recommender',
        'PASSWORD': 'recommender',
        'HOST': 'db',  # Docker service name
        'PORT': 5432,
    }
}
```

### Installed Apps

```python
INSTALLED_APPS = [
    # Django
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sites',
    
    # External
    'allauth',
    'allauth.account',
    'allauth.socialaccount',
    'django_celery_beat',
    'django_celery_results',
    'django_htmx',
    
    # Internal
    'exports',
    'ml',
    'movies',
    'profiles',
    'ratings',
    'suggestions',
]
```

## Project Directory Structure

```
src/
├── manage.py                          # Django management script
├── cfehome/                           # Project configuration
│   ├── settings.py
│   ├── urls.py
│   ├── celery.py
│   ├── wsgi.py
│   └── asgi.py
├── movies/                            # Movie management app
│   ├── models.py
│   ├── views.py
│   ├── urls.py
│   └── tasks.py
├── ratings/                           # Rating system app
│   ├── models.py
│   ├── views.py
│   └── tasks.py
├── suggestions/                       # Recommendation app
│   ├── models.py
│   ├── views.py                       # API endpoints
│   └── tasks.py
├── ml/                                # ML pipeline app
│   ├── utils.py                       # train_surprise_model(), load_model()
│   ├── tasks.py                       # Celery tasks
│   └── models.py
├── exports/                           # Model storage
│   └── storages.py
├── profiles/                          # User profiles
│   ├── models.py
│   └── utils.py
├── dashboard/                         # Admin dashboard
│   └── views.py
├── templates/                         # HTML templates
│   ├── base.html
│   ├── navbar.html
│   └── ...
├── data/                              # Downloaded datasets
│   ├── movies_metadata.csv
│   ├── ratings_small.csv
│   └── links_small.csv
└── media/                             # Generated files
    └── ml/
        └── models/
            └── surprise/
                ├── latest.pkl
                └── model-85.pkl
```
