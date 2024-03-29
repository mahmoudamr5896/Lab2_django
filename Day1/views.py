from urllib import request
from urllib.request import Request
from django.shortcuts import redirect, render
from django.http import HttpResponse

from .models import users ,Student
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login ,logout


# Create your views here.
# def home(req):
#     return HttpResponse('mahmoud amr')

def home(request):
    if not request.session.get('user_email') or not request.session.get('userpass'):
        return render(request,'Day1/sighnup.html')
    
    student = Student.objects.all()

    return render(request, 'Day1/home.html', {'students': student})

def about(request):
    return render(request, 'Day1/About.html')

def Contact(request):
    if not request.session.get('user_email') or not request.session.get('userpass'):
        return render(request,'Day1/sighnup.html')
    return render(request, 'Day1/Contact.html')


def Sighnup(request):
    return render(request, 'Day1/sighnup.html')

def Sighnin(request):
    return render(request, 'Day1/signin.html')


# def create_user(request):
#         if request.method == 'POST':
#             first_name = request.POST['fname']
#             last_name = request.POST['lname']
#             username = request.POST['uname']
#             email = request.POST['email']
#             password = request.POST['Pass']
#             user = users.objects.create(
#                 F_name=first_name,
#                 L_name=last_name,
#                 User_name=username,
#                 Email=email,
#                 Password=password
#             )
#             return redirect('sighnin') 
#         else:
#             return render(request, 'Day1/sighnup.html')



def create_user(request):
    if request.method == 'POST':
        first_name = request.POST['fname']
        last_name = request.POST['lname']
        username = request.POST['uname']
        email = request.POST['email']
        password = request.POST['Pass']     
        # Create the user
        user = users.objects.create_user(
            username=username,
            email=email,
            password=password,
            first_name=first_name,
            last_name=last_name
        )
        # Authenticate the user
        user = authenticate(request, username=username, password=password)
        if user :
            login(request, user)
            return redirect('home')  
        else:
            return HttpResponse("Request failed")
    else:
        return render(request, 'Day1/sighnup.html')


def Accept_user(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
        
        user = users.objects.filter(Email=email, Password=password).first()
        if user is not None:
            request.session['user_email'] = user.Email
            request.session['userpass'] = user.Password
            return redirect('home')
        else:
            return render(request,'Day1/sighnup.html')



def create_std(request):

    if not request.session.get('user_email') or not request.session.get('userpass'):
        return render(request,'Day1/sighnup.html')
    if request.method == 'POST':
        first_name = request.POST.get('fname')
        Email = request.POST.get('email')
        Age = request.POST.get('age')
        student = Student.objects.create(
            s_name=first_name,
            Age=Age,
            S_Email=Email,
        )
        return redirect('showdata') 
    else:
        return redirect('Contact')  
    


def showdata(request):
    if not request.session.get('user_email') or not request.session.get('userpass'):
        return render(request,'Day1/sighnup.html')
    students = Student.objects.all()
    return render(request, 'Day1/ShowUsers.html', {'students': students})

def delete_student(request, student_id):
    student = Student.objects.get(id=student_id).delete()
    return redirect('showdata')


def edit_student(request, student_id):
    student = Student.objects.get(id=student_id)
    if request.method == 'POST':
        student.s_name = request.POST.get('fname')
        student.S_Email = request.POST.get('email')
        student.Age = request.POST.get('age')
        student.save()
        return redirect('showdata') 
    return render(request, 'Day1/edit_student.html', {'student': student})


def logout_(request):
    logout(request)
    # request.session.clear()
    return render(request,'Day1/sighnup.html')