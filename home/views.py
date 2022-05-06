from django.shortcuts import render, redirect
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login as dj_login, logout, authenticate
from django.contrib.auth import authenticate, login
from django.contrib import messages
from django.views.generic import CreateView, ListView, View


from moderator.models import User, Tasks, Articles, Write, Teacher_Application
from moderator.forms import Teacher_ApplicationForm
from teacher.models import Createcourse, Createlesson

from student.models import Userstudent
from student.forms import RegUserstudentForm


# Home Folder
def home(request):
	return render(request, 'home/home.html')


def kirish(request):
	if request.method == 'POST':
		username = request.POST.get('username')
		password = request.POST.get('password')
		user = authenticate(request, username=username, password=password)
		if user is not None:
			dj_login(request, user)
			return redirect('moderator')
		else:
			messages.info(request, 'Login yoki parol xato')
	return render(request, 'home/kirish.html')



def registration(request):
	return render(request, 'home/registration.html')




class reg_student(CreateView):
	model = User
	form_class = RegUserstudentForm
	template_name = 'home/reg_student.html'
	success_url = '/student/home/page/'

	def form_valid(self, form):
		to_return = super().form_valid(form)
		user = authenticate(
			username=form.cleaned_data["username"],
			password=form.cleaned_data["password1"],
			)
		login(self.request, user)
		return to_return


# news barchasini birdan ko'rsatish
def h_news(request):
	articles = Articles.objects.all().order_by('-datetime')
	task = Tasks.objects.all().order_by('-datetime')
	context = {"articles": articles, "task": task}
	return render(request, 'home/h_news.html', context)



# Topshiriqlar
def h_tasks(request):
	task = Tasks.objects.all().order_by('-datetime')
	context = {"task": task}
	return render(request, 'home/h_tasks.html', context)


# Bitta topshiriqni ochish
def h_t_open(request, pk):
	task = Tasks.objects.get(id=pk)
	context = {"task": task}
	return render(request, 'home/h_t_open.html', context)



# Maqolalar
def h_articles(request):
	articles = Articles.objects.all().order_by('-datetime')
	context = {"articles": articles}
	return render(request, 'home/h_articles.html', context)

def h_a_open(request, pk):
	article = Articles.objects.get(id=pk)
	context = {"article": article}
	return render(request, 'home/h_a_open.html', context)


# Eng yaxshi dasturlarni yozish video va textlar 
def h_codes(request):
	codes = Write.objects.all().order_by('-datetime')
	context = {"codes": codes}
	return render(request, 'home/h_codes.html', context)


def h_c_open(request, pk):
	code = Write.objects.get(id=pk)
	context = {"code": code}
	return render(request, 'home/h_c_open.html', context)


def h_courses(request):
	courses = Createcourse.objects.all().order_by('-datetime')
	context = {"courses": courses}
	return render(request, 'home/h_courses.html', context)


def h_c_lessons(request, pk):
	lessons = Createlesson.objects.filter(user_id=pk).all()
	context = {"lessons": lessons}
	return render(request, 'home/h_c_lessons.html', context)


def h_c_l_open(request, pk):
	lesson = Createlesson.objects.get(pk=pk)
	context = {"lesson": lesson}
	return render(request, 'home/h_c_l_open.html', context)




def h_t_a_create(request):
	if request.method == "POST":
		form = Teacher_ApplicationForm(request.POST, request.FILES)
		if form.is_valid():
			form.save()
			return redirect('h_t_a_successful')
		else:
			messages.info(request, 'toldiring formani')
	else:
		form = Teacher_ApplicationForm()
	context = {'form': form}
	return render(request, 'home/h_t_a_create.html', context)




def h_t_a_successful(request):
	return render(request, 'home/h_t_a_successful.html')

