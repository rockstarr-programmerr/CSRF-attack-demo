# CSRF attack demo
This repo demonstrate a successful CSRF attack when Django's CSRF-protection mechanism is not used properly.

# Setup

## Setup vulnerable site
```
python -m venv .venv
.venv\Scripts\activate
python -m pip install --upgrade pip
cd vulnerable_site/
pip install -r requirements.txt
python manage.py migrate
python manage.py createsuperuser  # Create a user with some email
python manage.py runserver
```

## Set up attacker site
Run `attacker_site/index.html` with some web server. One choice is to use vscode's Live Server extension.

# Execute the attack
- Visit `http://127.0.0.1:8000/login/`, login using `username` and `password` you created in the `createsuperuser` step.
- Visit `attacker_site/index.html`. If you use vscode's Live Server extension, it's usually `http://127.0.0.1:5500`, the attack happens automatically.
- Observe that your email has been changed to "hacker@gmail.com"
```
cd vulnerable_site/
python manage.py shell

# In the shell:
from django.contrib.auth import get_user_model
User = get_user_model()
user = User.objects.get(username=<username you created in createsuperuser step>)
print(user.email)  # Should print "hacker@gmail.com"
```
