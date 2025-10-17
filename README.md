# NationDev Learning Platform

An African-focused e-learning platform developed by Hlumile Khanyo Nkohla (hnkohla).

## Prerequisites

- Python 3.11+
- Docker (optional)
- Git

## Installation

### Using Virtual Environment

1. Clone the repository:
```bash
git clone https://github.com/Hnkohla/Nationdev-learning.git
cd Nationdev-learning
```

2. Create and activate virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # Linux/Mac
# OR
venv\Scripts\activate     # Windows
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Environment Setup:
- Create a .env file in the project root with the following variables:
```plaintext
SECRET_KEY=your_secret_key_here
DEBUG=False
ALLOWED_HOSTS=localhost,127.0.0.1
DATABASE_URL=sqlite:///db.sqlite3
```

5. Database Setup:
```bash
python manage.py migrate
```

6. Create superuser (optional):
```bash
python manage.py createsuperuser
```

7. Run Development Server:
```bash
python manage.py runserver
```

### Using Docker

1. Build the image:
```bash
docker build -t nationdev .
```

2. Run the container:
```bash
docker run -p 8000:8000 \
    -e SECRET_KEY=your_secret_key_here \
    -e ALLOWED_HOSTS=localhost,127.0.0.1 \
    nationdev
```

## Documentation

The project documentation is built using Sphinx and can be found in the `docs` directory.

To build the documentation:
```bash
cd docs
make html
```

The generated documentation will be available in `docs/build/html/`.

## Project Structure

```
nationdev/
├── core/           # Main application
├── docs/           # Sphinx documentation
├── media/          # User-uploaded content
├── static/         # Static files
├── templates/      # HTML templates
└── nationdev/      # Project settings
```

## Security Notes

- Never commit the .env file or any sensitive data
- Keep DEBUG=False in production
- Use strong, unique passwords for admin accounts
- Configure proper ALLOWED_HOSTS in production
- Regularly update dependencies
- Use HTTPS in production
- Set up proper database backups

## Contributing

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## Development Branches

- `master` - Main development branch
- `docs` - Documentation updates
- `container` - Docker and deployment configurations

## License

This project is licensed under the MIT License - see the LICENSE file for details.