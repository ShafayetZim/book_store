# book_store
<b>Project Installation in Django Python:</b>

1. Download and install python 

2. Create Virtual Environment<br />
linux & mac os: python3 -m venv environment_name<br />
Windows: python -m venv environment_name
  
3. Activate Environment<br />
  #Linux & mac os<br />
  ->source environment_name/bin/activate<br />
  #Windows<br />
  ->environment_name\Scripts\activate
  
4. Install Django & resr framework<br />
 #linux & mac os & windows<br />
 ->pip install django<br />
 ->pip install djangorestframework<br />
 
5. To Create superuser <br />
->python manage.py createsuperuser
	enter username, Email, password
	enter your password again
  
6. Migration & migrate:<br />
-> Windows: python manage.py makemigrations<br />
-> Linux: python3 manage.py makemigrations<br />
-> Windows: python manage.py migrate<br />
-> Linux: python3 manage.py migrate

7. Run development server: <br />
-> Windows: python manage.py runserver<br />
-> Linux: python3 manage.py runserver

That's it! You now have a Bookstore application. <br />
Remember to run the server using python manage.py runserver and access the application at http://localhost:8000. <br />
The API endpoints will be available at http://localhost:8000/books/api/books/ , http://localhost:8000/books/api/add_book/, <br />
path('api/orders/', views.api_order_list, name='api_order_list') & path('api/add_order/', views.api_add_order, name='api_add_order').

Existing Superuser:
id: admin
pass: 123
