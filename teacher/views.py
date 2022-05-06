from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login as dj_login, logout, authenticate
from django.db import transaction, IntegrityError
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from moderator.decorators import unauthenticated_user , allowed_users, admin_only
from django.views.generic import CreateView, ListView, View

from moderator.models import User, Usermoderator, Tasks, Articles, Write
from moderator.forms import UserForm

from teacher.models import Userstaff, Course, Createcourse, Createlesson
from teacher.forms import UserUserstaffForm, CourseForm, CreatecourseForm, UpdatecourseForm, CreatelessonForm, UserUserstaffUpdate, UpdatelessonForm




@login_required(login_url='kirish')
@allowed_users(allowed_roles=['teacher'])
def h_t_page(request):
	if request.user.is_authenticated:
		return render(request, 'home_teacher/h_t_page.html')
	else:
		return redirect('kirish')


def h_t_profile(request):
	if request.user.is_authenticated:
		return render(request, 'home_teacher/h_t_profile.html')
	else:
		return redirect('kirish')


def h_t_up_profile(request):
	if request.user.is_authenticated:
		if request.method == 'POST':
			form1 = UserForm(request.POST, instance=request.user)
			form2 = UserUserstaffUpdate(request.POST, instance=request.user.userstaff)
			if form1.is_valid() and form2.is_valid():
				form1.save()
				form2.save()
				messages.info(request, 'Wrong username or password.')
				return redirect('h_t_profile')
			else:
				messages.info(request, 'Wrong username or password.')
		else:
			form1 = UserForm(instance=request.user)
			form2 = UserUserstaffUpdate(instance=request.user.userstaff)
			context = {"form1": form1, "form2": form2}
		return render(request, 'home_teacher/h_t_up_profile.html', context)
	else:
		return redirect('kirish')




def h_t_c_update(request, pk):
	user = get_object_or_404(Createcourse, pk=pk)
	if request.method == 'POST':
		form = UpdatecourseForm(request.POST, request.FILES, instance=user)
		if form.is_valid():
			form.save()
			return redirect('h_t_courses')
	else:
		form = UpdatecourseForm(instance=user)
	name = Createcourse.objects.get(pk=pk)
	context = {"form": form, "name": name}
	return render(request, 'home_teacher/h_t_c_update.html', context)





# O'qituvchining barcha kurslari
def h_t_mycourses(request):
	if request.user.is_authenticated:
		course = Createcourse.objects.filter(user_id=request.user.id).all()
		context = {"course": course}
		return render(request, 'home_teacher/h_t_mycourses.html', context)
	else:
		return redirect('kirish')



# O'qituvchining kursini darslari
def h_t_c_lessons(request, pk):
	if request.user.is_authenticated:
		course = Createcourse.objects.get(pk=pk)
		lessons = Createlesson.objects.filter(user_id=pk).all()
		context = {"lessons": lessons, "course": course}
		return render(request, 'home_teacher/h_t_c_lessons.html', context)
	else:
		return redirect('kirish')




# O'qituvchi kursining darsini yangilash
def h_t_c_l_update(request, user_id, pk):
	if request.user.is_authenticated:
		lesson = get_object_or_404(Createlesson, pk=pk)
		form = UpdatelessonForm(request.POST or None, instance=lesson)
		if form.is_valid():
			form.save()
			return redirect('h_t_c_lessons', user_id)
		context = {"form": form}
		return render(request, 'home_teacher/h_t_c_l_update.html', context)
	else:
		return redirect('kirish')


# O'qituvchi kursining darsini o'chirish
def h_t_c_l_delete(request, user_id, pk):
	if request.user.is_authenticated:
		form = get_object_or_404(Createlesson, pk=pk)
		if request.method == 'POST':
			form.delete()
			return redirect('h_t_c_lessons', user_id)
		context = {"form": form}
		return render(request, 'home_teacher/h_t_c_l_delete.html', context)
	else:
		return redirect('kirish')



def h_t_c_lesson(request, pk):
	if request.user.is_authenticated:
		course = Createlesson.objects.get(pk=pk)
		context = {"course": course}
		return render(request, 'home_teacher/h_t_c_lesson.html', context)
	else:
		return redirect('kirish')


########################################
# O'qituvchiga biriktrilgan kursga dars yaratish
def h_t_c_l_create(request, pk):
	if request.user.is_authenticated:
		pass
		form = CreatelessonForm(request.POST or None)
		if request.method == "POST":
			if form.is_valid():
				try:
					with transaction.atomic():
						cours = form.save(commit=False)
						cours.user = Createcourse.objects.get(id=pk)
						cours.save()
						form.save_m2m()
				except IntegrityError:
					print("Error Encountered")
				return redirect('h_t_c_lessons', pk)
		context = {'form': form}
		return render(request, 'home_teacher/h_t_c_l_create.html', context)
	else:
		return redirect('kirish')










# It maqollalr ichidagi barcha menularni ijro etish
def h_t_news(request):
	if request.user.is_authenticated:
		articles = Articles.objects.all().order_by('-datetime')
		task = Tasks.objects.all().order_by('-datetime')
		context = {"articles": articles, "task": task}
		return render(request, 'home_teacher/h_t_news.html', context)
	else:
		return redirect('kirish')



def h_t_tasks(request):
	if request.user.is_authenticated:
		tasks = Tasks.objects.all().order_by('-datetime')
		context = {"tasks": tasks}
		return render(request, 'home_teacher/h_t_tasks.html', context)
	else:
		return redirect('kirish')


def h_t_t_open(request, pk):
	if request.user.is_authenticated:
		task = Tasks.objects.get(pk=pk)
		context = {"task": task}
		return render(request, 'home_teacher/h_t_t_open.html', context)
	else:
		return redirect('kirish')


def h_t_articles(request):
	if request.user.is_authenticated:
		articles = Articles.objects.all().order_by('-datetime')
		context = {"articles": articles}
		return render(request, 'home_teacher/h_t_articles.html', context)
	else:
		return redirect('kirish')


def h_t_a_open(request, pk):
	if request.user.is_authenticated:
		article = Articles.objects.get(pk=pk)
		context = {"article": article}
		return render(request, 'home_teacher/h_t_a_open.html', context)
	else:
		return redirect('kirish')


def h_t_write(request):
	if request.user.is_authenticated:
		writes = Write.objects.all().order_by('-datetime')
		context = {"writes": writes}
		return render(request, 'home_teacher/h_t_write.html', context)
	else:
		return redirect('kirish')


def h_t_c_open(request, pk):
	if request.user.is_authenticated:
		write = Write.objects.get(pk=pk)
		context = {"write": write}
		return render(request, 'home_teacher/h_t_c_open.html', context)
	else:
		return redirect('kirish')




def h_t_c_all(request):
	if request.user.is_authenticated:
		courses = Createcourse.objects.all().order_by('-datetime')
		context = {"courses": courses}
		return render(request, 'home_teacher/h_t_c_all.html', context)
	else:
		return redirect('kirish')



def h_t_c_a_lessons(request, pk):
	if request.user.is_authenticated:
		lessons = Createlesson.objects.filter(user_id=pk).all()
		context = {"lessons": lessons}
		return render(request, 'home_teacher/h_t_c_a_lessons.html', context)
	else:
		return redirect('kirish')


def h_t_c_a_l_open(request, pk):
	if request.user.is_authenticated:
		lesson = Createlesson.objects.get(pk=pk)
		context = {"lesson": lesson}
		return render(request, 'home_teacher/h_t_c_a_l_open.html', context)
	else:
		return redirect('kirish')
