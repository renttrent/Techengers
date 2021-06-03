# Steps

To login to Django Admin you need to create super user.

``
python manage.py createsuperuser
``

After super user creation you can control all models in admin dashboard.

## Requirements

``
pip install django-crispy-forms
``

## Login App

Login is functional.
#### Todo:
1. Extend User Auth functionality
2. Design a better logout page 

## Dashboard App

After login user is automatically redirected to dashboard.

#### Todo:
1. Design dashboard as described [here](https://www.figma.com/file/kFRuANO5RHqiH37KIobKSP/Draft-1?node-id=0%3A1).
2. Add dummy data to be loaded
3. Make Exercises / Routines / Events.

# Important

**Never** commit not working or unnessary changes.