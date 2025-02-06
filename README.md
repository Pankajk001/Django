# ChaiAurDjango

ChaiAurDjango is a Django-based web application for managing and displaying different varieties of chai (tea). The project includes features such as listing chai varieties, viewing details of each chai, and finding stores that sell specific chai varieties.

## Project Structure
chaiaurDjango/ .gitignore chai/ __init__.py admin.py apps.py forms.py migrations/ models.py templates/ tests.py urls.py views.py chaiaurDjango/ __init__.py asgi.py settings.py urls.py views.py wsgi.py db.sqlite3 manage.py media/ static/ templates/ theme/


## Installation

1. Clone the repository:
    ```sh
    git clone https://github.com/yourusername/chaiaurDjango.git
    cd chaiaurDjango
    ```

2. Create a virtual environment and activate it:
    ```sh
    python -m venv .venv
    source .venv/bin/activate  # On Windows use `.venv\Scripts\activate`
    ```

3. Install the dependencies:
    ```sh
    pip install -r requirements.txt
    ```

4. Apply the migrations:
    ```sh
    python manage.py migrate
    ```

5. Create a superuser:
    ```sh
    python manage.py createsuperuser
    ```

6. Run the development server:
    ```sh
    python manage.py runserver
    ```

## Usage

- Access the admin panel at [http://127.0.0.1:8000/admin/](http://_vscodecontentref_/16) to manage chai varieties, reviews, and stores.
- Visit [http://127.0.0.1:8000/](http://_vscodecontentref_/17) to see the home page.
- Navigate to [http://127.0.0.1:8000/chai/](http://_vscodecontentref_/18) to view all chai varieties.
- Click on a chai variety to see its details.
- Use the form at [http://127.0.0.1:8000/chai/chai_stores/](http://_vscodecontentref_/19) to find stores that sell a specific chai variety.

## Features

- **ChaiVariety**: Model to represent different varieties of chai.
- **ChaiReview**: Model to represent reviews for chai varieties.
- **Store**: Model to represent stores that sell chai varieties.
- **ChaiCertificate**: Model to represent certificates for chai varieties.
- **Admin Interface**: Manage chai varieties, reviews, and stores through the Django admin panel.
- **Tailwind CSS**: Integrated Tailwind CSS for styling.

## Contributing

1. Fork the repository.
2. Create a new branch (`git checkout -b feature-branch`).
3. Make your changes.
4. Commit your changes (`git commit -am 'Add new feature'`).
5. Push to the branch (`git push origin feature-branch`).
6. Create a new Pull Request.

## License

This project is licensed under the MIT License.
