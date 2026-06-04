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

To ensure API Integration created a `.env` file and added:
```
GEMINI_API_KEY=your_api_key_here
```

Project Structure
1. `MIRA/` : Main Django application
2. ` templates/` : HTML templates
3. `static/` : CSS and image files
4. `models.py` : Database models
5. `views.py` : Application logic
6. `forms.py` : Django forms
7. `gemini.py` : API integration
8. `project_Mira/settings.py` : API key

Preview of Manage_Records View for user Aditi:
<img width="1355" height="627" alt="Screenshot 2026-06-04 141318" src="https://github.com/user-attachments/assets/2f798a3a-4269-4985-9f5d-a8a563520c66" />

Aditi Jain
