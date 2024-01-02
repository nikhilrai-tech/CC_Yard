## Prerequisites

Before you begin, ensure you have the following installed:

- Python (version 3.9.13)
- Django (version 4.1.13)
- Djongo (version 1.3.6)
- PyMongo (version 3.12.3)
- IDE (VSCode recommended)
- Virtualenv

## Getting Started

1. **Clone the repository:**

    ```bash
    git clone https://github.com/nikhilrai-tech/CC_Yard.git
    ```

2. **Create and activate a virtual environment:**

    ```bash
    python -m venv venv
    source venv/bin/activate   # On Windows, use 'venv\Scripts\activate'
    ```

3. **Install dependencies:**

    ```bash
    pip install -r requirements.txt
    ```

4. **Manually update the settings.py file for connecting to Mongo DB:**

    Open the `settings.py` file and update the `DATABASES` section:

    ```python
    DATABASES = {
    'default': {
        'ENGINE': 'djongo',
        'NAME': 'your-database-name',
    }
}

import pymongo

client = pymongo.MongoClient("mongodb://localhost:27017/")
db = client['your-database-name']
    ```

    Replace 'your-database-name' with your actual your schema name.

5. **Apply migrations:**

    Apply migrations using the following commands:

    ```bash
    python manage.py makemigrations
    python manage.py migrate
    ```

6. **Run the development server:**

    ```bash
    python manage.py runserver
    ```

    The project will be accessible at http://localhost:8000/
