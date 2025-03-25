# Django-rest-API

Django REST API is a powerful tool for building APIs in Python using Django. It allows you to define endpoints, handle requests, and serialize data into JSON format efficiently. 

## Steps to Create a Django REST API Project:
1. Set Up Your Environment:
   Install Python and django on your system.
   Use pip install djangorestframework to include Django REST Framework, which simplifies API development

2. Create a Django Project:
   Run django admin startproject <project_name> to create a project.
   Here I used "mysite" as a project_name.
   Navigate into the project folder: cd <project_name>.

3. Create a Django App:
   Inside the project, create an app where your api logic is live: python manage.py startapp <app_name>.
   In this project, I used api is the app name.

4. Define Models:
   Inside the app, define database models in the models.py file. These represent the structure of your data.

5. Migrate Database Changes:
   If you make any changes in the models.py in your app folder then you need to run python manage.py makemigrations and python manage.py migrate to apply the database structure.

6. Create Serializers:
   Create a serializers.py file in your app and define serializers for your models to convert them to JSON.

7. Build views:
   Define views for your API in views.py using Django REST Framework's APIView, GenericView, or ViewSet. Here I used APIView.

8. Set up URLs:
   Include routes for your API endpoints in urls.py.

9. Test your API:
   Run the development server using python manage.py runserver.
   
   
