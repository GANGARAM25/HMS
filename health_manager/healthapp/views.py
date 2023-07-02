from django.shortcuts import render
import mysql.connector
from django.contrib import messages
from django.shortcuts import redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.core.mail import EmailMessage
from django.conf import settings
from django.template.loader import render_to_string
import base64

cnx=mysql.connector.connect(user='root', password='20CS30017', host='127.0.0.1', database='HMS')
cursor=cnx.cursor()

def Signup_FDO(request):
    if request.method == 'POST':
        username = request.POST['name']
        email = request.POST['email']
        password = request.POST['password']
        password1 = request.POST['password1']
        number = request.POST['mobile_number']
        if len(password) < 5:
            messages.error(request, 'Password is too short')
            return redirect('Signup_FDO')
        elif password1 == password:
            cursor.execute("SELECT * FROM FDO WHERE Username = %s;",(username,))
            account = cursor.fetchone()
            if account:
                messages.error(request, 'Username already exists')
                return redirect('Signup_FDO')
            else:
                cursor.execute("INSERT INTO FDO (Username,Email,Password,Number) VALUES (%s,%s,%s,%s);", (username,email,password,number))
                cnx.commit()
                messages.success(request, 'Registration successful!')
                data = {'username': username,'password': password}
                user = User.objects.create_user(**data)
                user.save()
                return redirect('Signin')  
        else:
            messages.error(request, 'Passwords doesnot match')
    context = {'messages': messages.get_messages(request)}
    return render(request, 'healthapp/Signup_FDO.html', context)

def Signup_DBA(request):
    if request.method == 'POST':
        username = request.POST['name']
        email = request.POST['email']
        password = request.POST['password']
        password1 = request.POST['password1']
        number = request.POST['mobile_number']
        
        if len(password) < 5:
            messages.error(request, 'Password is too short')
            return redirect('Signup_DBA')
            
        elif password1 == password:
            cursor.execute("SELECT * FROM DBA WHERE Username = %s;",(username,))
            account = cursor.fetchone()
            if account:
                messages.error(request, 'Username already exists')
                return redirect('Signup_DBA')
            else:
                cursor.execute("INSERT INTO DBA (Username,Email,Password,Number) VALUES (%s,%s,%s,%s);", (username,email,password,number))
                cnx.commit()
                messages.success(request, 'Registration successful!')
                data = {'username': username,'password': password}
                user = User.objects.create_user(**data)
                user.save()
                return redirect('Signin')
        else:
            messages.success(request, 'Passwords doesnot match')   
    context = {'messages': messages.get_messages(request)}
    return render(request, 'healthapp/Signup_DBA.html', context)

def Signup_DEO(request):
    if request.method == 'POST':
        username = request.POST['name']
        email = request.POST['email']
        password = request.POST['password']
        password1 = request.POST['password1']
        number = request.POST['mobile_number']
        
        if len(password) < 5:
            messages.error(request, 'Password is too short')
            return redirect('Signup_DEO')
            
        elif password1 == password:
            cursor.execute("SELECT * FROM DEO WHERE Username = %s;",(username,))
            account = cursor.fetchone()
            if account:
                messages.error(request, 'Username already exists')
                return redirect('Signup_DEO')
            else:
                cursor.execute("INSERT INTO DEO (Username,Email,Password,Number) VALUES (%s,%s,%s,%s);", (username,email,password,number))
                cnx.commit()
                messages.success(request, 'Registration successful!')
                data = {'username': username,'password': password}
                user = User.objects.create_user(**data)
                user.save()
                return redirect('Signin')
        else:
            messages.success(request, 'Passwords doesnot match')   
    context = {'messages': messages.get_messages(request)}
    return render(request, 'healthapp/Signup_DEO.html', context)


def Signup_DOC(request):
    if request.method == 'POST':
        username = request.POST['name']
        email = request.POST['email']
        departmentid = request.POST['departmentid']
        password = request.POST['password']
        password1 = request.POST['password1']
        number = request.POST['mobile_number']
        
        if len(password) < 5:
            messages.error(request, 'Password is too short')
            return redirect('Signup_DOC')
            
        elif password1 == password:
            cursor.execute("SELECT * FROM DOC WHERE Username = %s;",(username,))
            account = cursor.fetchone()
            if account:
                messages.error(request, 'Username already exists')
                return redirect('Signup_DOC')
            else:
                cursor.execute("SELECT * FROM Department WHERE DepartmentID = %s;", (departmentid, ))
                account = cursor.fetchone()
                if account:
                    cursor.execute("INSERT INTO DOC (Username,Email,Password,Number,DepartmentID) VALUES (%s,%s,%s,%s,%s);", (username,email,password,number,departmentid))
                    cnx.commit()
                    messages.success(request, 'Registration successful!')
                    data = {'username': username,'password': password}
                    user = User.objects.create_user(**data)
                    user.save()
                    return redirect('Signin')
                else:
                    messages.error(request,'Department Doesnot Exist')
                    return redirect('Signup_DOC')
        else:
            messages.success(request, 'Passwords doesnot match')   
    context = {'messages': messages.get_messages(request)}
    return render(request, 'healthapp/Signup_DOC.html', context)

def Signin(request):
    if request.method == 'POST':
        usertype = request.POST['Usertype']
        username = request.POST['name']
        password = request.POST['password']
        
        if usertype == 'Front-Desk Operator':
            cursor.execute("SELECT * FROM FDO WHERE username = %s AND password = %s;", (username, password))
            account = cursor.fetchone()
            if account:
                request.session['username'] = username
                request.session['usertype'] = usertype
                user = authenticate(request, username=username, password=password)
                login(request, user)
                return redirect('home_fdo')
            else:
                messages.error(request, 'Invalid username or password')
                return redirect('Signin')
        elif usertype == 'Database Administrator':
            cursor.execute("SELECT * FROM DBA WHERE username = %s AND password = %s;", (username, password))
            account = cursor.fetchone()
            if account:
                request.session['username'] = username
                request.session['usertype'] = usertype
                user = authenticate(request, username=username, password=password)
                login(request, user)
                return redirect('home_dba')
            else:
                messages.error(request, 'Invalid username or password')
                return redirect('Signin')
        elif usertype == 'Data-Entry Operator':
            cursor.execute("SELECT * FROM DEO WHERE username = %s AND password = %s;", (username, password))
            account = cursor.fetchone()
            if account:
                request.session['username'] = username
                request.session['usertype'] = usertype
                user = authenticate(request, username=username, password=password)
                login(request, user)
                return redirect('home_deo')
            else:
                messages.error(request, 'Invalid username or password')
                return redirect('Signin')
        elif usertype == 'Doctor':
            cursor.execute("SELECT * FROM DOC WHERE username = %s AND password = %s;", (username, password))
            account = cursor.fetchone()
            if account:
                request.session['username'] = username
                request.session['usertype'] = usertype
                user = authenticate(request, username=username, password=password)
                login(request, user)
                return redirect('home_doc')
            else:
                messages.error(request, 'Invalid username or password')
                return redirect('Signin')
    context = {'messages': messages.get_messages(request)}
    return render(request, 'healthapp/Signin.html', context)

@login_required
def menu_fdo(request):
        if request.method == 'POST':
            if 'name' in request.POST:
                ssn = request.POST['ssn']
                username = request.POST['name']
                address = request.POST['address']
                phone = request.POST['phone']
                insuranceid = request.POST['insuranceid']
                select_query = "SELECT * FROM Patient WHERE SSN = %s;"
                cursor.execute(select_query, (ssn,))
                account = cursor.fetchone()
                if account:
                    messages.error(request, 'Patient already exists')
                    return redirect('menu_fdo')
                else:
                    insert_query = "INSERT INTO Patient (SSN, Name, Address, Phone, InsuranceID) VALUES(%s, %s, %s, %s, %s);"
                    cursor.execute(insert_query, (ssn, username, address, phone, insuranceid))
                    cnx.commit()
                    messages.success(request, 'Patient registered successfully')
                    return redirect('menu_fdo')

            elif 'department' in request.POST:
                ssn = request.POST['ssn']
                department = request.POST['department']
                date = request.POST['date']
                slot = request.POST['slot']
                s_query = "SELECT * FROM Patient WHERE SSN = %s;"
                cursor.execute(s_query, (ssn,))
                account = cursor.fetchone()
                select_query = "SELECT Number FROM Room WHERE Unavailable = 0 LIMIT 1;"
                cursor.execute(select_query)
                room = cursor.fetchone()
                if room and account:
                    select_query5 = "SELECT * FROM Appointment_1 WHERE Slot = %s AND Date = %s;"
                    cursor.execute(select_query5, (slot,date))
                    count = cursor.fetchone()
                    if count:
                        messages.error(request, 'Slot Clash')
                        return redirect('menu_fdo')
                    else:
                        select_query1 = '''SELECT DOC.Username
                                            FROM DOC
                                            JOIN Department ON DOC.DepartmentID = Department.DepartmentID AND Department.DepartmentID = %s
                                            LEFT JOIN Appointment_1 ON Appointment_1.Physician = DOC.Username 
                                            GROUP BY DOC.Username
                                            ORDER BY COUNT(Appointment_1.AppointmentID) ASC
                                            LIMIT 1;'''
                        cursor.execute(select_query1, (department,))
                        account1 = cursor.fetchone()
                        if account1:
                            update_query = "UPDATE Room SET Unavailable = 1 WHERE Number = %s;"
                            cursor.execute(update_query, (room))
                            cnx.commit()
                            insert_query = "INSERT INTO Stay (Patient, Room) VALUES(%s, %s);"
                            cursor.execute(insert_query, (ssn, room[0]))
                            cnx.commit()
                            insert_query1 = "INSERT INTO Appointment_1 (Patient,Physician,Slot,Date) VALUES (%s,%s,%s,%s);"
                            cursor.execute(insert_query1,(ssn,account1[0],slot,date))
                            cnx.commit()
                            roomnum = room[0]
                            physician_name = account1[0]
                            context = {'room':roomnum , 'physician':physician_name}
                            redirect('menu_fdo')
                            return render(request, 'healthapp/Menu_FDO.html', context)
                        else:
                            messages.error(request, 'Slot Clash')
                            return redirect('menu_fdo')
                else:
                    messages.error(request, 'No rooms available or Patient doesnot Exist')
                    return redirect('menu_fdo')
            
            elif 'report' in request.POST:
                ssn = request.POST['SSN']
                select_query2 = "SELECT * FROM Previous_Patients WHERE SSN = %s;"
                cursor.execute(select_query2, (ssn,))
                account = cursor.fetchone()
                if account:
                    username = account[5]
                    select_query4 = "SELECT Email FROM DOC WHERE Username = %s;"
                    cursor.execute(select_query4, (username,))
                    account5 = cursor.fetchone()
                    select_query6 = "SELECT * FROM Prescribes WHERE Patient = %s;"
                    cursor.execute(select_query6, (ssn,))
                    account6 = cursor.fetchone()
                    image_name = account6[2]
                    cursor.execute("SELECT * FROM Image WHERE Name = %s;", (image_name,))
                    data = cursor.fetchone()[1]
                    base64_image = base64.b64encode(data).decode('utf-8')
                    template = render_to_string('healthapp/Report.html', {'account':account , 'username':username ,'account6':account6 , 'base64_image':base64_image})
                    email = EmailMessage('Report of the Patient', template , settings.EMAIL_HOST_USER, [account5,])
                    image_data = base64.b64decode(base64_image)
                    email.attach('image.jpg', image_data, 'image/jpg')
                    email.fail_silently = False
                    email.send()
                    messages.success(request, 'Report sent successfully')
                    context = {'messages': messages.get_messages(request)}
                    return render(request, 'healthapp/Menu_FDO.html', context)
                else:
                    messages.error(request, 'Patient does not exist or not yet discharged')
                    return redirect('menu_fdo')
            
            elif 'SSN' in request.POST:
                ssn = request.POST['SSN']
                select_query2 = "SELECT * FROM Patient WHERE SSN = %s;"
                cursor.execute(select_query2, (ssn,))
                account = cursor.fetchone()
                if account:
                    select_query3 = "SELECT Room FROM Stay WHERE Patient = %s;"
                    cursor.execute(select_query3, (ssn,))
                    room = cursor.fetchone()
                    if room:
                        update_query1 = "UPDATE Room SET Unavailable = 0 WHERE Number = %s;"
                        cursor.execute(update_query1, (room[0],))
                        cnx.commit()
                        delete_query = "DELETE FROM Stay WHERE Patient = %s;"
                        cursor.execute(delete_query, (ssn,))
                        cnx.commit()
                        delete_query1 = "DELETE FROM Appointment WHERE Patient = %s;"
                        cursor.execute(delete_query1, (ssn,))
                        cnx.commit()
                        insert_query = "INSERT INTO Previous_Patients (SSN, Name, Address, Phone, InsuranceID, PCP, AppointmentStatus) VALUES(%s, %s, %s, %s, %s, %s, %s);"
                        cursor.execute(insert_query, (account[0], account[1], account[2], account[3], account[4], account[5], account[6]))
                        cnx.commit()
                        delete_query = "DELETE FROM Patient WHERE SSN = %s;"
                        cursor.execute(delete_query, (ssn,))
                        cnx.commit()
                        messages.success(request, 'Patient discharged successfully')
                        return redirect('menu_fdo')
                    else:
                        messages.error(request, 'Patient has no room assigned')
                        return redirect('menu_fdo')
                else:
                    messages.error(request, 'Patient does not exist')
                    return redirect('menu_fdo')

            context = {'messages': messages.get_messages(request)}
            return render(request, 'healthapp/Menu_FDO.html', context)
        context = {}
        return render(request, 'healthapp/Menu_FDO.html', context)

@login_required
def menu_dba(request):
    if request.method == 'POST':
        if 'dept_id' in request.POST:
            usertype = request.POST['Usertype']
            username = request.POST['name']
            password = 'password'
            email = request.POST['email']
            number = request.POST['phone']
            dept_id = request.POST['dept_id']
            cursor.execute("SELECT * FROM DOC WHERE Username = %s;", (username,))
            account = cursor.fetchone()
            cursor.execute("SELECT * FROM Department WHERE DepartmentID = %s;", (dept_id,))
            account1 = cursor.fetchone()
            if account:
                messages.error(request, 'User already exists')
                return redirect('menu_dba')
            elif not account1:
                messages.error(request, 'Department does not exist')
                return redirect('menu_dba')
            else:
                cursor.execute("INSERT INTO DOC (Username,Email,Password,Number,DepartmentID) VALUES (%s,%s,%s,%s,%s);", (username,email,password,number,dept_id))
                cnx.commit()
                messages.success(request, 'User registered successfully')
                data = {'username': username,'password': password}
                user = User.objects.create_user(**data)
                user.save()
                return redirect('menu_dba')
        
        elif 'email' in request.POST:
            usertype = request.POST['Usertype']
            username = request.POST['name']
            password = 'password'
            email = request.POST['email']
            number = request.POST['phone']
            if usertype == 'Front-Desk Operator':
                cursor.execute("SELECT * FROM FDO WHERE Username = %s;", (username,))
                account = cursor.fetchone()
                if account:
                    messages.error(request, 'User already exists')
                    return redirect('menu_dba')
                else:
                    cursor.execute("INSERT INTO FDO (Username,Email,Password,Number) VALUES (%s,%s,%s,%s);", (username,email,password,number))
                    cnx.commit()
                    messages.success(request, 'User registered successfully')
                    data = {'username': username,'password': password}
                    user = User.objects.create_user(**data)
                    user.save()
                    return redirect('menu_dba')
            elif usertype == 'Data-Entry Operator':
                cursor.execute("SELECT * FROM DEO WHERE Username = %s;", (username,))
                account = cursor.fetchone()
                if account:
                    messages.error(request, 'User already exists')
                    return redirect('menu_dba')
                else:
                    cursor.execute("INSERT INTO DEO (Username,Email,Password,Number) VALUES (%s,%s,%s,%s);", (username,email,password,number))
                    cnx.commit()
                    messages.success(request, 'User registered successfully')
                    data = {'username': username,'password': password}
                    user = User.objects.create_user(**data)
                    user.save()
                    return redirect('menu_dba')
            elif usertype == 'Database Administrator':
                cursor.execute("SELECT * FROM DBA WHERE Username = %s;", (username,))
                account = cursor.fetchone()
                if account:
                    messages.error(request, 'User already exists')
                    return redirect('menu_dba')
                else:
                    cursor.execute("INSERT INTO DBA (Username,Email,Password,Number) VALUES (%s,%s,%s,%s);", (username,email,password,number))
                    cnx.commit()
                    messages.success(request, 'User registered successfully')
                    data = {'username': username,'password': password}
                    user = User.objects.create_user(**data)
                    user.save()
                    return redirect('menu_dba')

        elif 'name' in request.POST:
            usertype = request.POST['Usertype']
            username = request.POST['name']
            if usertype == 'Front-Desk Operator':
                cursor.execute("SELECT * FROM FDO WHERE Username = %s;", (username,))
                account = cursor.fetchone()
                if account:
                    username = account[0]
                    password = account[1]
                    cursor.execute("DELETE FROM FDO WHERE Username = %s;", (username,))
                    cnx.commit()
                    messages.success(request, 'User deleted successfully')
                    user = User.objects.get(username=username)
                    if user.check_password(password):
                        user.delete()
                    return redirect('menu_dba')
                else:
                    messages.error(request, 'User does not exist')
                    return redirect('menu_dba')
            elif usertype == 'Data-Entry Operator':
                cursor.execute("SELECT * FROM DEO WHERE Username = %s;", (username,))
                account = cursor.fetchone()
                if account:
                    username = account[0]
                    password = account[1]
                    cursor.execute("DELETE FROM DEO WHERE Username = %s;", (username,))
                    cnx.commit()
                    messages.success(request, 'User deleted successfully')
                    user = User.objects.get(username=username)
                    if user.check_password(password):
                        user.delete()
                    return redirect('menu_dba')
                else:
                    messages.error(request, 'User does not exist')
                    return redirect('menu_dba')
            elif usertype == 'Doctor':
                cursor.execute("SELECT * FROM DOC WHERE Username = %s;", (username,))
                account = cursor.fetchone()
                if account:
                    username = account[0]
                    password = account[1]
                    cursor.execute("DELETE FROM DOC WHERE Username = %s;", (username,))
                    cnx.commit()
                    messages.success(request, 'User deleted successfully')
                    user = User.objects.get(username=username)
                    if user.check_password(password):
                        user.delete()
                    return redirect('menu_dba')
                else:
                    messages.error(request, 'User does not exist')
                    return redirect('menu_dba')
            elif usertype == 'Database Administrator':
                cursor.execute("SELECT * FROM DBA WHERE Username = %s;", (username,))
                account = cursor.fetchone()
                if account:
                    username = account[0]
                    password = account[1]
                    cursor.execute("DELETE FROM DBA WHERE Username = %s;", (username,))
                    cnx.commit()
                    messages.success(request, 'User deleted successfully')
                    user = User.objects.get(username=username)
                    if user.check_password(password):
                        user.delete()
                    return redirect('menu_dba')
                else:
                    messages.error(request, 'User does not exist')
                    return redirect('menu_dba')
        context = {'messages': messages.get_messages(request)}
        return render(request, 'healthapp/Menu_DBA.html', context)
    context = {}
    return render(request, 'healthapp/Menu_DBA.html', context)

@login_required
def menu_deo(request):
    if request.method == 'POST':
        if 'description' in request.POST:
            ssn = request.POST['ssn']
            cursor.execute("SELECT * FROM Patient WHERE SSN = %s;", (ssn,))
            account0 = cursor.fetchone()
            if account0:
                image_name = request.POST['image_name']
                description = request.POST['description']
                cursor.execute("SELECT * FROM Image WHERE Name = %s;", (image_name,))
                account = cursor.fetchone()
                if account:
                    cursor.execute("SELECT AppointmentID,Physician FROM Appointment WHERE Patient = %s;", (ssn,))
                    account1 = cursor.fetchone()
                    if account1:
                        cursor.execute("INSERT INTO Prescribes (Physician, Patient, Image, Description, Appointment) VALUES (%s,%s,%s,%s,%s);", (account1[1],ssn,image_name,description,account1[0]))
                        cnx.commit()
                        messages.success(request, 'Prescription added successfully')
                        return redirect('menu_deo')
                    else:
                        messages.error(request, 'Patient has not completed appointment with doctor')
                        return redirect('menu_deo')
            else:
                messages.error(request, 'Patient or Image does not exist')
                return redirect('menu_deo')

        else: 
            image_name = request.POST['image_name']
            image_file = request.FILES['image_file']
            data = image_file.read()
            cursor.execute("SELECT * FROM Image WHERE Name = %s;", (image_name,))
            account = cursor.fetchone()
            if account:
                messages.error(request, 'Image already exists')
                return redirect('menu_deo')
            else:
                cursor.execute("INSERT INTO Image (Name,Data) VALUES (%s,%s);", (image_name,data))
                cnx.commit()
                messages.success(request, 'Image uploaded successfully')
                cursor.execute("SELECT * FROM Image WHERE Name = %s;", (image_name,))
                data = cursor.fetchone()[1]
                base64_image = base64.b64encode(data).decode('utf-8')
                context = {'base64_image':base64_image,'messages': messages.get_messages(request)}
                return render(request, 'healthapp/Menu_DEO.html', context)
        context = {'messages': messages.get_messages(request)}
        return render(request, 'healthapp/Menu_DEO.html', context)
    context = {}
    return render(request, 'healthapp/Menu_DEO.html', context)

@login_required
def menu_doc(request):
    usertype = request.session.get('usertype')
    username = request.session.get('username')
    if usertype == 'Doctor':
        cursor.execute("SELECT * FROM Appointment_1 WHERE Physician = %s;", (username,))
        account0 = cursor.fetchall()
        context = {'account0' : account0}
        if request.method == 'POST':
            if 'email' in request.POST:
                ssn = request.POST['ssn']
                cursor.execute("SELECT * FROM Patient WHERE SSN = %s;", (ssn,))
                account = cursor.fetchone()
                if account:
                    cursor.execute("SELECT * FROM Prescribes WHERE Patient = %s;", (ssn,))
                    account1 = cursor.fetchall()
                    context = {'account1':account1 , 'account0':account0}
                    return render(request, 'healthapp/Menu_DOC.html', context)
                else:
                    messages.error(request, 'Patient does not exist')
                    context = {'account0':account0 , 'messages': messages.get_messages(request)}
                    return render(request, 'healthapp/Menu_DOC.html', context)
                    # return redirect('menu_doc')
                
            elif 'image_1' in request.POST:
                image_1 = request.POST['image_1']
                cursor.execute("SELECT * FROM Image WHERE Name = %s;", (image_1,))
                account = cursor.fetchone()
                if account:
                    data = account[1]
                    base64_image = base64.b64encode(data).decode('utf-8')
                    context = {'base64_image':base64_image, 'account0':account0}
                    return render(request, 'healthapp/Menu_DOC.html', context)
                else:
                    messages.error(request, 'Image does not exist')
                    return redirect('menu_doc')
                
                
            elif 'ssn' in request.POST:
                ssn = request.POST['ssn']
                cursor.execute("SELECT * FROM Patient WHERE SSN = %s;", (ssn,))
                account = cursor.fetchone()
                if account:
                    cursor.execute("SELECT * FROM Patient WHERE SSN = %s;", (ssn,))
                    account2 = cursor.fetchall()
                    context = {'account2':account2, 'account0':account0}
                    return render(request, 'healthapp/Menu_DOC.html', context)
                else:
                    messages.error(request, 'Patient does not exist')
                    return redirect('menu_doc')

            elif 'row_num' in request.POST:
                row_num = request.POST['row_num']
                appointment_id = account0[int(row_num)][0]
                cursor.execute("SELECT * FROM Appointment_1 WHERE AppointmentID = %s;", (appointment_id,))
                account3 = cursor.fetchone()
                insertquery = "INSERT INTO Appointment (AppointmentID, Patient, Physician, Slot , Date) VALUES (%s,%s,%s,%s,%s);"
                cursor.execute(insertquery, (account3[0],account3[1],account3[2],account3[3],account3[4]))
                cnx.commit()
                cursor.execute("DELETE FROM Appointment_1 WHERE AppointmentID = %s;", (appointment_id,))
                cnx.commit()
                updatequery = "UPDATE Patient SET PCP = %s WHERE SSN = %s;"
                updatequery1 = "UPDATE Patient SET AppointmentStatus = '1' WHERE PCP = %s;"
                cursor.execute(updatequery1, (account3[2],))
                cnx.commit()
                cursor.execute(updatequery, (account3[2],account3[1],))
                cnx.commit()
                messages.success(request, 'Appointment confirmed successfully')
                return redirect('menu_doc')
        return render(request, 'healthapp/Menu_DOC.html', context)
    context = {}
    return render(request, 'healthapp/Menu_DOC.html', context)

@login_required
def home_fdo(request):
    username = request.session.get('username')
    context = {'username': username}
    return render(request, 'healthapp/Home_FDO.html', context)

@login_required
def home_deo(request):
    username = request.session.get('username')
    context = {'username': username}
    return render(request, 'healthapp/Home_DEO.html', context)

@login_required
def home_doc(request):
    username = request.session.get('username')
    context = {'username': username}
    return render(request, 'healthapp/Home_DOC.html', context)

@login_required
def home_dba(request):
    username = request.session.get('username')
    context = {'username': username}
    return render(request, 'healthapp/Home_DBA.html', context)

@login_required
def account_fdo(request):
    usertype = request.session.get('usertype')
    username = request.session.get('username')
    if usertype == 'Front-Desk Operator':
        if request.method == 'POST':
            password = request.POST['password']
            password1 = request.POST['password1']
            if password1 == password:
                cursor.execute("SELECT * FROM FDO WHERE username = %s;", (username,))
                account = cursor.fetchone()
                update_query =  "UPDATE FDO SET password = %s WHERE username = %s;"
                cursor.execute(update_query, (password,username,))
                cnx.commit()
                messages.success(request, 'Password changed successfully')
                return redirect('account_fdo')
            else:
                messages.error(request, 'Passwords do not match')
                return redirect('account_fdo')
        cursor.execute("SELECT * FROM FDO WHERE username = %s;", (username,))
        account = cursor.fetchone()
        context = {'account':account, 'messages': messages.get_messages(request)}
        return render(request, 'healthapp/Account_FDO.html', context)

@login_required
def account_deo(request):
    usertype = request.session.get('usertype')
    username = request.session.get('username')
    if usertype == 'Data-Entry Operator':
        if request.method == 'POST':
            password = request.POST['password']
            password1 = request.POST['password1']
            if password1 == password:
                cursor.execute("SELECT * FROM DEO WHERE username = %s;", (username,))
                account = cursor.fetchone()
                update_query =  "UPDATE DEO SET password = %s WHERE username = %s;"
                cursor.execute(update_query, (password,username,))
                cnx.commit()
                messages.success(request, 'Password changed successfully')
                return redirect('account_deo')
            else:
                messages.error(request, 'Passwords do not match')
                return redirect('account_deo')
        cursor.execute("SELECT * FROM DEO WHERE username = %s;", (username,))
        account = cursor.fetchone()
        context = {'account':account, 'messages': messages.get_messages(request)}
        return render(request, 'healthapp/Account_DEO.html', context)

@login_required
def account_doc(request):
    usertype = request.session.get('usertype')
    username = request.session.get('username')
    if usertype == 'Doctor':
        if request.method == 'POST':
            password = request.POST['password']
            password1 = request.POST['password1']
            if password1 == password:
                cursor.execute("SELECT * FROM DOC WHERE username = %s;", (username,))
                account = cursor.fetchone()
                update_query =  "UPDATE DOC SET password = %s WHERE username = %s;"
                cursor.execute(update_query, (password,username,))
                cnx.commit()
                messages.success(request, 'Password changed successfully')
                return redirect('account_doc')
            else:
                messages.error(request, 'Passwords do not match')
                return redirect('account_doc')
        cursor.execute("SELECT * FROM DOC WHERE username = %s;", (username,))
        account = cursor.fetchone()
        if account:
            cursor.execute("SELECT * FROM Previous_Patients WHERE PCP = %s;", (username,))
            account1 = cursor.fetchall()
            context = {'account':account, 'account1':account1}
            return render(request, 'healthapp/Account_DOC.html', context)
    context = {}
    return render(request, 'healthapp/Account_DOC.html', context)

@login_required
def account_dba(request):
    usertype = request.session.get('usertype')
    username = request.session.get('username')
    if usertype == 'Database Administrator':
        if request.method == 'POST':
            password = request.POST['password']
            password1 = request.POST['password1']
            if password1 == password:
                cursor.execute("SELECT * FROM DBA WHERE username = %s;", (username,))
                account = cursor.fetchone()
                update_query =  "UPDATE DBA SET password = %s WHERE username = %s;"
                cursor.execute(update_query, (password,username,))
                cnx.commit()
                messages.success(request, 'Password changed successfully')
                return redirect('account_dba')
            else:
                messages.error(request, 'Passwords do not match')
                return redirect('account_dba')
        cursor.execute("SELECT * FROM DBA WHERE username = %s;", (username,))
        account = cursor.fetchone()
        cursor.execute("SELECT * FROM DOC;")
        account1 = cursor.fetchall()
        cursor.execute("SELECT * FROM DEO;")
        account2 = cursor.fetchall()
        cursor.execute("SELECT * FROM FDO;")
        account3 = cursor.fetchall()
        context = {'account':account , 'account1':account1 , 'account2':account2 , 'account3':account3}
        return render(request, 'healthapp/Account_DBA.html', context)

def logout_(request):
    logout(request)
    return redirect('Signin')
    

    


            



