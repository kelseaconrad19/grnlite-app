# GRNLITE: A Manuscript Beta Reading Platform

This repository contains the codebase for GRNLITE, a web application designed to facilitate the beta reading process for authors and readers. The platform provides a streamlined and efficient way for authors to connect with beta readers, manage feedback, and improve their manuscripts.

## Features

### For Authors:
- Submit manuscripts for beta reading.
- Set project budgets and select beta readers based on experience and preferences.
- Communicate directly with beta readers and provide clear expectations.
- Receive and analyze feedback in a structured format.
- Manage payments to beta readers securely.
- Access a resource library with writing tips, templates, and other helpful tools.
- Connect with other authors in community groups.

### For Beta Readers:
- Create detailed profiles showcasing experience, pay scales, and genre preferences.
- Browse available manuscripts and apply for projects that match interests.
- Provide feedback through in-manuscript comments and overall evaluations.
- Receive payments from authors for completed feedback work.
- Access training modules to improve beta reading skills and provide high-quality feedback.
- View performance metrics to track progress and showcase expertise.

## Technologies Used
- **Django/Python**: Backend framework for handling application logic and data management.
- **Django REST Framework**: Provides a RESTful API for frontend interactions.
- **PostgreSQL**: Relational database for storing user data, manuscripts, and feedback.
- **HTML/CSS/JavaScript**: Frontend technologies for user interface design and interactivity.
- **OAuth 2.0**: Enables secure authentication with Google and other providers.
- **Render**: Cloud platform for hosting and deploying the application.

## Installation
1. Clone the repository: `git clone https://github.com/JSander72/GRNLITE.git`
2. Install dependencies: `pip install -r requirements.txt`
3. Set up environment variables:
    - `DATABASE_URL`: Connection string for your PostgreSQL database.
    - `SECRET_KEY`: A unique secret key for your Django application.
    - `DEBUG`: Set to `True` for development mode, `False` for production.
    - `ALLOWED_HOSTS`: A comma-separated list of allowed hostnames.
    - `SOCIAL_AUTH_GOOGLE_OAUTH2_KEY`: Your Google OAuth 2.0 client ID.
    - `SOCIAL_AUTH_GOOGLE_OAUTH2_SECRET`: Your Google OAuth 2.0 client secret.
4. Run migrations: `python manage.py migrate`
5. Start the development server: `python manage.py runserver`

## Deployment
The application is set up to be deployed on Render. The `render.yaml` file contains the necessary configurations for automatic deployment from the GitHub repository.

## Contributing
Contributions are welcome! Please feel free to submit issues or pull requests.

## License
This project is licensed under the MIT License - see the LICENSE file for details.
