# water_labs_ai_task
Instructions for Dependencies

1. Create a python virtual environment 
2. Install python 3.x, django 2.x and django rest framework in it
3. Activate the virtual environment
4. Navigate to user_project and run command 'python manage.py runserver 8001'

Instructions for the task

Task 1: User View for CRUD operation

#1 Create User
Method: Post
URL : http://localhost:8001/account/register/user/
Body : username, password, email

#2 Retrieve User
Method: Get
URL : http://localhost:8001/account/register/user/<username>/
params : username

#3 Update User
Method: Put
URL : http://localhost:8001/account/register/user/
Body : username, password, email

#4 Delete User
Method: Delete
URL : http://localhost:8001/account/register/user/<username>/
params : username

Task 2: Authenticate credentials

Method: Post
URL : http://localhost:8001/account/authenticate/
Body : username, password
