from django.core.management.base import BaseCommandfrom django.core.management import BaseCommand

from django.contrib.auth.models import Userfrom core.models import Course, BlogPost

from core.models import Course, BlogPostfrom django.utils import timezone

from django.utils import timezone

from django.utils.text import slugifyclass Command(BaseCommand):

    help = 'Adds initial sample data to the database'

class Command(BaseCommand):

    help = 'Adds sample data to the database'    def handle(self, *args, **kwargs):

        # Create Coffee Origins

    def handle(self, *args, **kwargs):        origins = [

        # Create sample users            {

        if not User.objects.filter(username='admin').exists():                'name': 'Yirgacheffe Highland',

            admin_user = User.objects.create_superuser(                'country': 'Ethiopia',

                'admin', 'admin@example.com', 'admin123'                'region': 'Yirgacheffe',

            )                'altitude': '1,800-2,200m',

            self.stdout.write(self.style.SUCCESS('Created admin user'))                'description': 'Known for its floral and citrus notes, these beans are grown in the highlands of Ethiopia.'

            },

        if not User.objects.filter(username='instructor').exists():            {

            instructor = User.objects.create_user(                'name': 'Blue Mountain Estate',

                'instructor', 'instructor@example.com', 'instructor123',                'country': 'Jamaica',

                first_name='John', last_name='Doe'                'region': 'Blue Mountains',

            )                'altitude': '1,500-1,800m',

            self.stdout.write(self.style.SUCCESS('Created instructor user'))                'description': 'Smooth, clean taste with virtually no bitterness and intense aroma.'

            },

        # Create sample courses            {

        course_data = [                'name': 'Tarrazu Valley',

            {                'country': 'Costa Rica',

                'title': 'Python for Beginners',                'region': 'Tarrazu',

                'description': 'Learn Python programming from scratch with this comprehensive course. Perfect for beginners who want to start their programming journey.',                'altitude': '1,200-1,800m',

                'short_description': 'Start your Python journey',                'description': 'Well-balanced acidity with a full body and chocolate notes.'

                'price': 49.99,            }

                'duration_weeks': 4,        ]

                'level': 'BEG',

                'featured': True,        for origin_data in origins:

            },            CoffeeOrigin.objects.get_or_create(**origin_data)

            {

                'title': 'Advanced Web Development',        # Create Roasting Profiles

                'description': 'Master modern web technologies including HTML5, CSS3, JavaScript, and popular frameworks. Build real-world projects.',        profiles = [

                'short_description': 'Become a web expert',            {

                'price': 79.99,                'name': 'Morning Light',

                'duration_weeks': 8,                'roast_level': 'LT',

                'level': 'ADV',                'temperature_curve': 'Start at 180°C, gradually increase to 210°C over 12 minutes',

                'featured': True,                'duration': 12,

            },                'notes': 'Light roast to preserve origin characteristics and bright acidity.'

            {            },

                'title': 'Data Science Fundamentals',            {

                'description': 'Introduction to data science and analysis. Learn Python, pandas, numpy, and basic machine learning concepts.',                'name': 'Sunset Gold',

                'short_description': 'Learn data science basics',                'roast_level': 'MT',

                'price': 69.99,                'temperature_curve': 'Start at 190°C, increase to 220°C over 15 minutes',

                'duration_weeks': 6,                'duration': 15,

                'level': 'INT',                'notes': 'Medium roast for balanced flavor and caramel sweetness.'

                'featured': True,            },

            },            {

        ]                'name': 'Midnight Barrel',

                'roast_level': 'DK',

        for course_info in course_data:                'temperature_curve': 'Start at 200°C, increase to 230°C over 18 minutes',

            Course.objects.get_or_create(                'duration': 18,

                title=course_info['title'],                'notes': 'Dark roast for bold, rich flavors with smoky undertones.'

                defaults=course_info            }

            )        ]

            self.stdout.write(self.style.SUCCESS(f'Created course: {course_info["title"]}'))

        for profile_data in profiles:

        # Create sample blog posts            RoastingProfile.objects.get_or_create(**profile_data)

        blog_data = [

            {        # Create Coffees

                'title': 'Getting Started with Programming',        if Coffee.objects.count() == 0:

                'content': '''Programming is an essential skill in today's digital world. This guide will help you begin your journey into coding with practical tips and resources.            origins = CoffeeOrigin.objects.all()

                            profiles = RoastingProfile.objects.all()

                Key points to get started:            

                1. Choose a programming language            coffees = [

                2. Set up your development environment                {

                3. Practice regularly                    'name': 'Ethiopian Morning Bloom',

                4. Join coding communities                    'origin': origins[0],

                5. Work on personal projects''',                    'roasting_profile': profiles[0],

                'summary': 'Learn why programming is important and how to start.',                    'price': 18.99,

            },                    'description': 'A bright and floral coffee with citrus notes and jasmine aroma.',

            {                    'tasting_notes': 'Lemon, Jasmine, Bergamot',

                'title': 'The Future of Web Development',                    'created_date': timezone.now()

                'content': '''Web development is constantly evolving with new technologies. Stay ahead of the curve by learning about the latest trends and tools in web development.                },

                                {

                Trending technologies:                    'name': 'Blue Mountain Reserve',

                - Next.js and React                    'origin': origins[1],

                - TypeScript                    'roasting_profile': profiles[1],

                - Web Assembly                    'price': 24.99,

                - Progressive Web Apps                    'description': 'Smooth and balanced with subtle chocolate notes.',

                - AI-powered development tools''',                    'tasting_notes': 'Chocolate, Nuts, Honey',

                'summary': 'Explore upcoming trends in web development.',                    'created_date': timezone.now()

            },                },

            {                {

                'title': 'Data Science Career Path',                    'name': 'Costa Rican Dark Barrel',

                'content': '''Data science offers exciting career opportunities. Discover the skills needed to become a successful data scientist and the various career paths available.                    'origin': origins[2],

                                    'roasting_profile': profiles[2],

                Essential skills:                    'price': 16.99,

                - Programming (Python/R)                    'description': 'Bold and rich with a smooth finish.',

                - Statistics                    'tasting_notes': 'Dark Chocolate, Caramel, Walnut',

                - Machine Learning                    'created_date': timezone.now()

                - Data Visualization                }

                - Big Data Technologies''',            ]

                'summary': 'Discover how to become a data scientist.',

            },            for coffee_data in coffees:

        ]                Coffee.objects.create(**coffee_data)



        for blog_info in blog_data:        self.stdout.write(self.style.SUCCESS('Successfully added sample data'))
            if not BlogPost.objects.filter(title=blog_info['title']).exists():
                post = BlogPost.objects.create(
                    title=blog_info['title'],
                    author=User.objects.get(username='instructor'),
                    content=blog_info['content'],
                    summary=blog_info['summary'],
                    slug=slugify(blog_info['title'])
                )
                post.publish()
                self.stdout.write(self.style.SUCCESS(f'Created blog post: {blog_info["title"]}'))

        self.stdout.write(self.style.SUCCESS('Successfully added sample data'))