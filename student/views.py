from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login as dj_login, logout, authenticate
from django.db import transaction, IntegrityError
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from moderator.decorators import unauthenticated_user , allowed_users, admin_only
from django.views.generic import CreateView, ListView, View
from moderator.models import User, Usermoderator, Tasks, Articles, Write
from moderator.forms import UserForm
from student.models import Userstudent
from student.forms import UserstudentForm, UserstudentUpdate
from teacher.models import Createcourse, Createlesson






# Create your views here.
@login_required(login_url='kirish')
@allowed_users(allowed_roles=['student'])
def h_s_page(request):
	if request.user.is_authenticated:
		return render(request, 'student/h_s_page.html')
	else:
		return redirect('kirish')


def h_s_profile(request):
	if request.user.is_authenticated:
		return render(request, 'student/h_s_profile.html')
	else:
		return render('kirish')


def h_s_p_update(request):
	if request.user.is_authenticated:
		if request.method == 'POST':
			form1 = UserForm(request.POST, instance=request.user)
			form2 = UserstudentUpdate(request.POST, request.FILES, instance=request.user.userstudent)
			if form1.is_valid() and form2.is_valid():
				form1.save()
				form2.save()
				messages.info(request, 'Wrong username or password.')
				return redirect('h_s_profile')
			else:
				messages.info(request, 'Wrong username or password.')
		else:
			form1 = UserForm(instance=request.user)
			form2 = UserstudentUpdate(instance=request.user.userstudent)
		context = {"form1": form1, "form2": form2}
		return render(request, 'student/h_s_p_update.html', context)
	else:
		return redirect('kirish')




def h_s_news(request):
	if request.user.is_authenticated:
		articles = Articles.objects.all().order_by('-datetime')
		task = Tasks.objects.all().order_by('-datetime')
		context = {"articles": articles, "task": task}
		return render(request, 'student/h_s_news.html', context)
	else:
		return redirect('kirish')



def h_s_tasks(request):
	if request.user.is_authenticated:
		tasks = Tasks.objects.all().order_by('-datetime')
		context = {"tasks": tasks}
		return render(request, 'student/h_s_tasks.html', context)
	else:
		return redirect('kirish')


def h_s_t_open(request, pk):
	if request.user.is_authenticated:
		task = Tasks.objects.get(pk=pk)
		context = {"task": task}
		return render(request, 'student/h_s_t_open.html', context)
	else:
		return redirect('kirish')


def h_s_articles(request):
	if request.user.is_authenticated:
		articles = Articles.objects.all().order_by('-datetime')
		context = {"articles": articles}
		return render(request, 'student/h_s_articles.html', context)
	else:
		return redirect('kirish')


def h_s_a_open(request, pk):
	if request.user.is_authenticated:
		article = Articles.objects.get(pk=pk)
		context = {"article": article}
		return render(request, 'student/h_s_a_open.html', context)
	else:
		return redirect('kirish')



def h_s_write(request):
	if request.user.is_authenticated:
		writes = Write.objects.all().order_by('-datetime')
		context = {"writes": writes}
		return render(request, 'student/h_s_write.html', context)
	else:
		return redirect('kirish')


def h_s_w_open(request, pk):
	if request.user.is_authenticated:
		write = Write.objects.get(pk=pk)
		context = {"write": write}
		return render(request, 'student/h_s_w_open.html', context)
	else:
		return redirect('kirish')



def h_s_courses(request):
	if request.user.is_authenticated:
		courses = Createcourse.objects.all().order_by('-datetime')
		context = {"courses": courses}
		return render(request, 'student/h_s_courses.html', context)
	else:
		return redirect('kirish')


def h_s_c_lessons(request, pk):
	if request.user.is_authenticated:
		lessons = Createlesson.objects.filter(user_id=pk).all()
		context = {"lessons": lessons}
		return render(request, 'student/h_s_c_lessons.html', context)
	else:
		return redirect('kirish')


def h_s_c_l_open(request, pk):
	if request.user.is_authenticated:
		lesson = Createlesson.objects.get(pk=pk)
		context = {"lesson": lesson}
		return render(request, 'student/h_s_c_l_open.html', context)
	else:
		return redirect('kirish')

