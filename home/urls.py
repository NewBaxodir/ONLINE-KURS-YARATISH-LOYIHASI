
"""course URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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


from django.urls import path, include
from home import views
from django.contrib.auth.decorators import login_required


urlpatterns = [
	path('', views.home, name='home'),
	path('kirish/', views.kirish, name='kirish'),
    path('registration/', views.registration, name='registration'),
    path('reg/student/', views.reg_student.as_view(), name='reg_student'),

    # *************
    path('home/news/all/', views.h_news, name='h_news'),
    # *************
    path('home/tasks/', views.h_tasks, name='h_tasks'),
    path('task/open/<int:pk>/', views.h_t_open, name='h_t_open'),
    # *************
    path('home/articles/', views.h_articles, name='h_articles'),
    path('home/article/open/<int:pk>/', views.h_a_open, name='h_a_open'),
	# *************
    path('home/codes/', views.h_codes, name='h_codes'),
    path('home/code/open/<int:pk>/', views.h_c_open, name='h_c_open'),
    # *************
    path('home/courses/', views.h_courses, name='h_courses'),
    path('home/lessons/<int:pk>/', views.h_c_lessons, name='h_c_lessons'),
    path('home/course/lesson/open/<int:pk>/', views.h_c_l_open, name='h_c_l_open'),

    path('home/teacher/application/', views.h_t_a_create, name='h_t_a_create'), 
    path('home/teacher/successful/', views.h_t_a_successful, name='h_t_a_successful'), 

]