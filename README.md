# NationDev Learning Platform

An African-focused e-learning platform developed by Hlumile Khanyo Nkohla (hnkohla).

## Quick Start

### Using venv
```bash
python -m venv venv
source venv/bin/activate  # or `venv\Scripts\activate` on Windows
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
```

### Using Docker
```bash
docker build -t nationdev .
docker run -p 8000:8000 nationdev
```

## Documentation
```bash
cd docs
make html
```

## Security Notes
- Add your SECRET_KEY to .env file
- Never commit sensitive data
- Keep DEBUG=False in production