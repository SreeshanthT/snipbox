# SnipBox Documentation

SnipBox is a short note-saving application where users can save snippets, organize them with tags, and manage them through a set of RESTful APIs. This documentation provides how to setup the application.

---

## **Setup Instructions**

### **Requirements**
- Python
- Django
- Django REST Framework

### **Installation Steps**

1. Clone the Repository:
   ```bash
   git clone https://github.com/your-repo/snipbox.git
   cd snipbox
   ```

2. Set up a Virtual Environment:
   ```bash
   python3 -m venv venv
   source venv/bin/activate
   ```

3. Install Dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Configure Database:
   - Switch keys of `DATABASES` to change your `default` db to postgreSQL
   - Update `DATABASES` in `settings.py` with your PostgreSQL credentials.

5. Apply Migrations:
   ```bash
   python manage.py migrate
   ```

6. Create a Superuser:
   ```bash
   python manage.py createsuperuser
   ```

7. Run the Server:
   ```bash
   python manage.py runserver
   ```

8. Access the Application:
   - Visit `http://127.0.0.1:8000` in your browser.

---
