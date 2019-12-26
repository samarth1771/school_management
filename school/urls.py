# Create this file from project directory

from django.urls import path
from .views import *

urlpatterns = [
    path('index/', index, name='index'),
    path('login/', logins, name='login'),
    path('logout/', log_out, name='logout'),
    path('students/', stud_details, name='students'),
    path('schools/', school_details, name='schools'),
    path('delete_st/<int:id>', delete_student, name='delete_st'),
    path('update_st/<int:id>', update_display, name='update_st'),
    path('update_student/', update_student, name='update_stud')

]
