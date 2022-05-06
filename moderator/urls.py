
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
from moderator import views
from django.contrib.auth.decorators import login_required

urlpatterns = [
    
    # MODERATOR DATES
    path('moderator/', views.moderator, name='moderator'),
    path('moderator/database/', views.moderator_database, name='moderator_database'),
    path('moderator/create/', login_required(views.moderator_create.as_view(),login_url='kirish'), name='moderator_create'),

    path('moderator/delete/<int:pk>/', views.m_m_delete, name='m_m_delete'),
    path('moderator/profile/<int:pk>/', views.moderator_profile, name='moderator_profile'),
    # MODERATOR DATES


    # TEACHER DATES
    path('', views.m_teach_database, name='m_teach_database'),
    path('teacher/create/', login_required(views.m_teach_create.as_view(),login_url='kirish'), name='m_teach_create'),
    path('teacher/profile/<int:pk>/', views.m_teach_profile, name='m_teach_profile'),
    path('teacher/delete/<int:pk>/', views.m_teach_delete, name='m_teach_delete'),
    # TEACHER DATES


    # STUDENT DATES
    path('student/', views.m_student_database, name='m_student_database'),
    path('student/profile/<int:pk>/', views.m_student_profile, name='m_student_profile'),
    path('student/create/', login_required(views.m_student_create.as_view(),login_url='kirish'), name='m_student_create'),
    path('student/delete/<int:pk>/', views.m_student_delete, name='m_student_delete'),
    # path('student/create/')


    # COURSE DATES
    path('course/database/', views.m_c_database, name='m_c_database'),
    path('course/create/', views.m_c_create, name='m_c_create'),
    path('course/update/<int:pk>/', views.m_c_update, name='m_c_update'),
    path('course/delete/<int:pk>/', views.m_c_delete, name='m_c_delete'),
    # COURSE DATES


    # TEACHER COURSES
    path('teachers/courses/', views.m_t_courses, name="m_t_courses"),
    path('teachers/course/create/', views.m_t_c_create, name="m_t_c_create"),
    path('teachers/course/update/<int:pk>/', views.m_t_c_update, name="m_t_c_update"),
    path('teachers/course/delete/<int:pk>/', views.m_t_c_delete, name='m_t_c_delete'),

    path('teachers/course/lessons/<int:pk>/', views.m_t_c_lessons, name='m_t_c_lessons'),
    path('teachers/course/lessons/create/<int:pk>/add/', views.m_t_c_l_create, name='m_t_c_l_create'),
    # TEACHER COURSES


    # TASKS DATES
    path('tasks/', views.m_tasks, name='m_tasks'),
    path('task/create/', views.m_t_create, name='m_t_create'),
    path('task/update/<int:pk>/', views.m_t_update, name='m_t_update'),
    path('task/delete/<int:pk>/', views.m_t_delete, name='m_t_delete'),
    # TASKS DATES


    # ARTICLES DATES
    path('articles/', views.m_articles, name='m_articles'),
    path('articles/create/', views.m_a_create, name='m_a_create'),
    path('articles/update/<int:pk>/', views.m_a_update, name='m_a_update'),
    path('articles/delete/<int:pk>/', views.m_a_delete, name='m_a_delete'),
    # ARTICLES DATES


    # WRITE DATES
    path('writes/', views.m_write, name='m_write'),
    path('write/create/', views.m_w_create, name='m_w_create'),
    path('write/update/<int:pk>/', views.m_w_update, name='m_w_update'),
    path('write/delete/<int:pk>/', views.m_w_delete, name='m_w_delete'),
    # WRITE DATES

    path('teacher/application/', views.m_t_application, name='m_t_application'),
    path('teacher/application/open/<int:pk>/', views.m_t_a_open, name='m_t_a_open'),
    path('teacher/application/delete/<int:pk>/', views.m_t_a_delete, name='m_t_a_delete'),


    # logout
    path('logout_view', views.logout_view, name='logout_view')

]