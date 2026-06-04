This is a Django-based healthcare web application that analyze health parameters such as glucose, haemoglobin , cholesterol and generate AI-powered health remarks.

Features

1. User Authentication and User Creation (Login / Signup)
2. CRUD operations
3. Secure record management none can access before login
4. AI-generated health remarks
5. Record history for each user
6. Database management

Tech Stack
1. Backend : Python and Django
2. Frontend : HTML , CSS
3. Database : SQLite3
4. AI API : Gemini API

Project Structure

1. `MIRA/` : Main Django application
2. ` templates/` : HTML templates
3. `static/` : CSS and image files
4. `models.py` : Database models
5. `views.py` : Application logic
6. `forms.py` : Django forms

Installation

Clone the repository:

```bash
git clone https://github.com/YOUR_USERNAME/MIRA-Repo.git
```

Navigate to project directory:

```bash
cd django_1
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Run migrations:

```bash
python manage.py migrate
```

Start server:

```bash
python manage.py runserver
```

Open browser:

```text
http://127.0.0.1:8000/
```

## Environment Variables

Create a `.env` file and add:

```text
GEMINI_API_KEY=your_api_key_here
```
Aditi Jain
