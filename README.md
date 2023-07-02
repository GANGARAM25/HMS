# HMS
A web application for a hospital management system using Django allowing for patient registration, appointment scheduling, and maintenance of health information.

# Important things to do
1. Install mysql into your system.
2. Then run it as **mysql -u root -p**
3. The password setting for mysql is done while installing
4. create a database say HMS.
5. your username passsword and database name need to be changed in views.py check there once.
6. just copy paste the commands in terminal of mysql as given in queries.txt file

# Commands to run:
1. python3 manage.py makemigrations
2. python3 manage.py migrate
3. python3 manage.py runserver
4. register dba1
5. login the dba1 and add fdo1,deo1
6. doc1 dep 1,doc2 2,doc3 1,doc4 3
7. add patient pat6 ssn 6
8. after registration doctor is assigned to pateint
9. doctor approves the appointment
10. deo add the photos and prescriptions

Now similary whatever needed you can do

Implemented the small messages after registration updation etc,
also security added cannot backnavigate after logout redirect to signin page
