
STILL UNDER DEVELOPMENT. DO NOT USE THE CODE UNTIL THE PROJECT IS COMPLETED.

# Simple Social Network

A minimal example of a simple social networking website built with Django. Users can register, login, create posts, and view posts on the homepage. This project is intended as a foundation for building more advanced social networking features.

## Features

- User registration and authentication
- Post creation and display

## Installation and Setup

1. Clone the repository or download the source code.

```
git clone https://github.com/allendekoker/simple-social-network.git
```

2. Navigate to the project folder:

```
cd simplesocialnetwork
```

3. Create a virtual environment and activate it:

- Windows:

```
python -m venv myvenv
myvenv\Scripts\activate
```

- macOS/Linux:

```
python3 -m venv myvenv
source myvenv/bin/activate
```

4. Install the required packages:

```
pip install -r requirements.txt
```

5. Run migrations and start the server:

```
python manage.py makemigrations
python manage.py migrate
python manage.py runserver
```

6. Open your web browser and navigate to `http://127.0.0.1:8000/` to access the website.

## Usage

1. Register for an account by clicking "Register" in the navigation bar.
2. Login with your new account credentials.
3. Create a new post by clicking "Create Post" in the navigation bar.
4. View posts on the homepage.

## Technologies Used

- Python
- Django
- django-crispy-forms
- HTML/CSS

## Contributing

Feel free to fork the repository and submit pull requests for additional features, bug fixes, or improvements.