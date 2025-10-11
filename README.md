# NationDev Learning Platform

NationDev is a modern e-learning platform built with Django, focusing on providing high-quality programming and development courses. The platform features a responsive design, user authentication, course management, and a blog system.

## Features

- User Authentication
  - Custom user registration with email verification
  - Login/logout functionality
  - Profile management
  - Protected course content for authenticated users

- Course Management
  - Dynamic course listings
  - Detailed course pages
  - Course reviews and ratings
  - Course difficulty levels
  - Progress tracking

- Blog System
  - Article publishing with rich text
  - Categories and tags
  - Author profiles
  - Related posts

- Responsive Design
  - Bootstrap 5 integration
  - Mobile-first approach
  - Custom styling
  - Intuitive navigation

## Installation

1. Clone the repository:
```bash
git clone https://github.com/hnkohla/nationdev.git
cd nationdev
```

2. Create and activate a virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Apply migrations:
```bash
python manage.py migrate
```

5. Create a superuser:
```bash
python manage.py createsuperuser
```

6. Load sample data (optional):
```bash
python manage.py add_sample_data
```

7. Run the development server:
```bash
python manage.py runserver
```

Visit http://127.0.0.1:8000/ to see the application running.

## Project Structure

```
nationdev/
├── core/                   # Main application
│   ├── migrations/        # Database migrations
│   ├── management/        # Custom management commands
│   ├── templates/        # App-specific templates
│   ├── models.py         # Database models
│   ├── views.py         # View logic
│   ├── urls.py          # URL routing
│   └── forms.py         # Form definitions
├── static/               # Static files (CSS, JS, images)
├── media/               # User-uploaded files
├── templates/           # Project-wide templates
└── nationdev_core/      # Project configuration
```

## Configuration

Key settings are in `nationdev_core/settings.py`. For production:

1. Set `DEBUG = False`
2. Update `ALLOWED_HOSTS`
3. Configure your database
4. Set up proper email settings
5. Configure static and media file serving

## Contributing

1. Fork the repository
2. Create a feature branch
3. Commit your changes
4. Push to the branch
5. Create a Pull Request

## License

This project is licensed under the MIT License - see the LICENSE file for details.