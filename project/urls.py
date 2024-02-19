"""
URL configuration for project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from Day1.views import Accept_user, Sighnin, Sighnup,logout, create_std, create_user, home, logout_, showdata ,delete_student, edit_student
from Day1.views import about ,Contact

urlpatterns = [
    path("admin/", admin.site.urls),
    path("home/",home ,name='home'),
    path("about/",about,name='about'),
    path("Contact/",Contact,name='Contact'),
    path("sighnup/",Sighnup,name='sighnup'),
    path("sighnin/",Sighnin,name='sighnin'),
    path('create_user/', create_user, name='create_user'),
    path('Accept_user/', Accept_user, name='Accept_user'),
    path('create_std/', create_std, name='create_std'),
    path("ShowUsers/",showdata,name='showdata'),
    path('delete_student/<int:student_id>/', delete_student, name='delete_student'),
    path('edit_student/<int:student_id>/', edit_student, name='edit_student'),
    path('logout/', logout_, name='logout'),


]
