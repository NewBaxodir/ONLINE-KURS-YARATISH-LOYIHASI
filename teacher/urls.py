from django.urls import path, include
from teacher import views

urlpatterns = [

    # TEACHER PROFILE
    path('home/page/', views.h_t_page, name='h_t_page'),
    path('home/profile/', views.h_t_profile, name='h_t_profile'),
    path('home/profile/update/', views.h_t_up_profile, name='h_t_up_profile'),
    
    path('home/my/courses/', views.h_t_mycourses, name='h_t_mycourses'),
    path('home/create/<int:pk>/add/', views.h_t_c_l_create, name='h_t_c_l_create'),
    path('home/course/update/<int:pk>/', views.h_t_c_update, name='h_t_c_update'),
    
    path('home/course/lessons/<int:pk>/', views.h_t_c_lessons, name='h_t_c_lessons'),
    path('home/course/lesson/<int:pk>/view/', views.h_t_c_lesson, name='h_t_c_lesson'),
    path('home/course/lesson/update/<int:user_id>/<int:pk>/', views.h_t_c_l_update, name='h_t_c_l_update'),
    path('home/course/lesson/delete/<int:user_id>/<int:pk>/', views.h_t_c_l_delete, name='h_t_c_l_delete'),
    
    # all news, articles .. .
    path('home/news/', views.h_t_news, name='h_t_news'),
    path('home/tasks/', views.h_t_tasks, name='h_t_tasks'),
    path('home/task/open/<int:pk>/', views.h_t_t_open, name='h_t_t_open'),
    path('home/articles/', views.h_t_articles, name='h_t_articles'),
    path('home/article/open/<int:pk>/', views.h_t_a_open, name='h_t_a_open'),
    path('home/writes/', views.h_t_write, name='h_t_write'),
    path('home/code/open/<int:pk>/', views.h_t_c_open, name='h_t_c_open'),

    path('home/courses/all/', views.h_t_c_all, name='h_t_c_all'),
    path('home/courses/all/lessons/<int:pk>/', views.h_t_c_a_lessons, name='h_t_c_a_lessons'),
    path('home/courses/all/lesson/open/<int:pk>/', views.h_t_c_a_l_open, name='h_t_c_a_l_open'),
]