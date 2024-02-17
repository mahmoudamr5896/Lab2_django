from urllib import request
from urllib.request import Request
from django.shortcuts import redirect, render
from django.http import HttpResponse

from Day1.models import users ,Student
# Create your views here.
# def home(req):
#     return HttpResponse('mahmoud amr')

def home(request):
    return render(request, 'Day1/home.html')

def about(request):
    return render(request, 'Day1/About.html')

def Contact(request):
    return render(request, 'Day1/Contact.html')


def Sighnup(request):
    return render(request, 'Day1/sighnup.html')

def Sighnin(request):
    return render(request, 'Day1/signin.html')


def create_user(request):
        if request.method == 'POST':
            first_name = request.POST['fname']
            last_name = request.POST['lname']
            username = request.POST['uname']
            email = request.POST['email']
            password = request.POST['Pass']
            # Create and save the user object
            user = users.objects.create(
                F_name=first_name,
                L_name=last_name,
                User_name=username,
                Email=email,
                Password=password
            )
            return redirect('sighnin')  # Redirect to success page
        else:
            return render(request, 'Day1/sighnup.html')



def Accept_user(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
        
        user = users.objects.filter(Email=email, Password=password).first()
        
        if user is not None:
            return redirect('home')
        else:
            return render(request,'Day1/sighnup.html')


from django.shortcuts import render, redirect
from .models import Student



def create_std(request):
    if request.method == 'POST':
        first_name = request.POST.get('fname')
        Email = request.POST.get('email')
        Age = request.POST.get('age')
        student = Student.objects.create(
            s_name=first_name,
            Age=Age,
            S_Email=Email,
        )
        # Redirect to a URL pattern or view name
        return redirect('showdata')  # Assuming 'show_data' is the URL pattern name for the 'showdata' view
    else:
        return redirect('Contact')  # Redirect to 'Contact' URL pattern or view name

def showdata(request):
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
        return redirect('showdata')  # Assuming 'show_data' is the URL pattern name for the page displaying all students
    return render(request, 'Day1/edit_student.html', {'student': student})