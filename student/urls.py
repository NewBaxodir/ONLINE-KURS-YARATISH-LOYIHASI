
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
from student import views

urlpatterns = [
    
    # STUDENT DATES

    path('home/page/', views.h_s_page, name='h_s_page'),
    path('home/profile/', views.h_s_profile, name='h_s_profile'),
    path('profile/update/', views.h_s_p_update, name='h_s_p_update'),

    path('home/news/', views.h_s_news, name='h_s_news'),
    path('home/tasks/', views.h_s_tasks, name='h_s_tasks'),
    path('home/task/<int:pk>/', views.h_s_t_open, name='h_s_t_open'),
    path('home/articles/', views.h_s_articles, name='h_s_articles'),
    path('home/article/<int:pk>/', views.h_s_a_open, name='h_s_a_open'),
    path('home/write/', views.h_s_write, name='h_s_write'),
    path('home/write/<int:pk>/', views.h_s_w_open, name='h_s_w_open'),

    path('home/courses/', views.h_s_courses, name='h_s_courses'),
    path('home/course/open/<int:pk>/', views.h_s_c_lessons, name='h_s_c_lessons'),
    path('home/lesson/<int:pk>/', views.h_s_c_l_open, name='h_s_c_l_open'),

]