from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import *


# Create your views here.

def index(request):
    return HttpResponse("<h1>Index Page</h1>")


def logins(request):
    # If user is already logged in then directly redirect it to student page
    if request.user.is_authenticated:
        return redirect('students')

    # If the request contains some parameters(POST method) then validate it to django admin's credentials
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        # This method returns userID if successfully validate
        user = authenticate(request, username=username, password=password)

        if user:  # if user is logged in successfully, redirect to student page
            login(request, user)
            return redirect('students')
        else:  # otherwise say Login failed
            return HttpResponse("Login Failed")

    return render(request, 'school/login.html', {})


def log_out(request):  # Uses logout method of auth class to log out and redirects to login page
    logout(request)
    return redirect('login')


# The view 'stud_details' will only open if user is logged in (@login_required decorator used)
@login_required
def stud_details(request):
    std = Student.objects.all()  # for fetching all objects
    schools = School.objects.all()

    if request.method == "POST":
        name = request.POST.get('name')
        roll_no = request.POST.get('roll_no')
        gender = request.POST.get('gender')
        city = request.POST.get('city')
        school_id = School.objects.get(pk=request.POST.get('school_id'))
        bday = request.POST.get('bday')

        # return HttpResponse(name)

        sts = Student(roll_no=roll_no, name=name, school_id=school_id, city=city, gender=gender, bday=bday)
        sts.save()

    return render(request, 'school/std_data.html', {'std': std, 'schools': schools})


# This will delete the entry of a student
def delete_student(request, id):
    st = Student.objects.get(pk=int(id))
    st.delete()

    return redirect('students')


def update_display(request, id):
    schools = School.objects.all()
    std = Student.objects.get(pk=int(id))

    return render(request, 'school/update_student.html', {'schools': schools, 'std': std})


def update_student(request):
    if request.method == "POST":
        st = Student.objects.get(pk=request.POST.get('roll_no'))
        st.name = request.POST.get('name')
        st.roll_no = request.POST.get('roll_no')
        st.gender = request.POST.get('gender')
        st.city = request.POST.get('city')
        st.school = request.POST.get('school')
        st.bdate = request.POST.get('bdate')

        st.save()

        return redirect('students')


def school_details(request):
    schools = School.objects.all()

    return render(request, 'school/school_data.html', {'schools': schools})


def insert_data(request):
    if request.method == "POST":
        name = request.POST.get('name')
        roll_no = request.POST.get('roll_no')
        gender = request.POST.get('gender')
        city = request.POST.get('city')
        school = request.POST.get('school')
        bdate = request.POST.get('bdate')

        sts = Student(roll_no=roll_no, name=name, school_id=school, city=city, gender=gender, bdate=bdate)
        sts.save()
