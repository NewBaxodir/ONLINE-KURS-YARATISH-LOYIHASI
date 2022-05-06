from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login as dj_login, logout, authenticate
from django.db import transaction, IntegrityError
from django.contrib import messages

from django.contrib.auth.decorators import login_required
from django.views.generic import CreateView, ListView, View

from moderator.decorators import unauthenticated_user , allowed_users, admin_only
from moderator.models import User, Usermoderator, Tasks, Articles, Write, Teacher_Application
from moderator.forms import UserForm, UsermoderatorForm, TasksForm, ArticlesForm, WriteForm, MCreatecourseForm

from teacher.models import Course, Userstaff, Createcourse, Createlesson
from teacher.forms import UserUserstaffForm, UserUserstaffUpdate, CourseForm, UpdatecourseForm, CreatelessonForm, UpdatelessonForm

from student.models import Userstudent
from student.forms import UserstudentForm








@login_required(login_url='kirish')
@admin_only
def moderator(request):
	if request.user.is_authenticated:
		return render(request, 'moderator/moderator.html')
	else:
		return redirect('kirish')



@login_required(login_url='kirish')
@admin_only
def moderator_database(request):
	if request.user.is_authenticated:
		name = Usermoderator.objects.all()
		s = Usermoderator.objects.all().count()
		context = {"name": name, "s": s}
		return render(request, 'moderator/moderator_database.html', context)
	else:
		return redirect('kirish')
	
	

class moderator_create(CreateView):
	model = User
	form_class = UsermoderatorForm
	template_name = 'moderator/moderator_create.html'

	def form_valid(self, form):
		user = form.save()
		return redirect('moderator_database')


@login_required(login_url='kirish')
@admin_only
def m_m_delete(request, pk):
	if request.user.is_authenticated:
		user = Usermoderator.objects.get(user_id=pk)
		form = get_object_or_404(User, pk=pk)
		if request.method == 'POST':
			form.delete()
			return redirect('moderator_database')
		context = {"user": user}
		return render(request, 'moderator/m_m_delete.html', context)
	else:
		return redirect('kirish')


@login_required(login_url='kirish')
@admin_only
def moderator_profile(request, pk):
	if request.user.is_authenticated:
		user = Usermoderator.objects.get(user_id=pk)
		context = {"user": user}
		return render(request, 'moderator/moderator_profile.html', context)
	else:
		return redirect('kirish')

# MODERATOR DATES



















# TEACHER DATES

@login_required(login_url='kirish')
@admin_only
def m_teach_database(request):
	if request.user.is_authenticated:
		name = Userstaff.objects.all()
		s = Userstaff.objects.all().count()
		context = {"name": name, "s": s}
		return render(request, 'moderator/m_teach_database.html', context)
	else:
		return redirect('kirish')



class m_teach_create(CreateView):
	model = User
	form_class = UserUserstaffForm
	template_name = 'moderator/m_teach_create.html'

	def form_valid(self, form):
		user = form.save()
		return redirect('m_teach_database')


@login_required(login_url='kirish')
@admin_only
def m_teach_profile(request, pk):
	if request.user.is_authenticated:
		user = Userstaff.objects.get(user_id=pk)
		course = Createcourse.objects.filter(user_id=pk).all()
		context = {"user": user, "course": course}
		return render(request, 'moderator/m_teach_profile.html', context)
	else:
		return redirect('kirish')


@login_required(login_url='kirish')
@admin_only
def m_teach_delete(request, pk):
	if request.user.is_authenticated:
		user = Userstaff.objects.get(user_id=pk)
		course = Createcourse.objects.filter(user_id=pk)
		a = get_object_or_404(User, pk=pk)
		if request.method == 'POST':
			a.delete()
			return redirect('m_teach_database')
		context = {'a': a, "user": user, "course": course}
		return render(request, 'moderator/m_teach_delete.html', context)
	else:
		return redirect('kirish')


# TEACHER DATES





# STUDENT DATES
@login_required(login_url='kirish')
@admin_only
def m_student_database(request):
	name = Userstudent.objects.all()
	context = {"name": name}
	return render(request, 'moderator/m_student_database.html', context)



class m_student_create(CreateView):
	model = User
	form_class = UserstudentForm
	template_name = 'moderator/m_student_create.html'

	def form_valid(self, form):
		user = form.save()
		return redirect('m_student_database')


@login_required(login_url='kirish')
@admin_only
def m_student_profile(request, pk):
	if request.user.is_authenticated:
		user = Userstudent.objects.get(user_id=pk)
		context = {"user": user}
		return render(request, 'moderator/m_student_profile.html', context)
	else:
		return redirect('kirish')


@login_required(login_url='kirish')
@admin_only
def m_student_delete(request):
	user = get_object_or_404(Userstudent, pk=pk)

	return render(request, 'moderator/m_student_delete.html')


@login_required(login_url='kirish')
@admin_only
def m_student_delete(request, pk):
	if request.user.is_authenticated:
		user = Userstudent.objects.get(user_id=pk)
		a = get_object_or_404(User, pk=pk)
		if request.method == 'POST':
			a.delete()
			return redirect('m_student_database')
		context = {'a': a, "user": user}
		return render(request, 'moderator/m_student_delete.html', context)
	else:
		return redirect('kirish')

# STUDENT DATES




# COURSE DATES
@login_required(login_url='kirish')
@admin_only
def m_c_database(request):
	if request.user.is_authenticated:
		name = Course.objects.all()
		context = {"name": name}
		return render(request, 'moderator/m_c_database.html', context)
	else:
		return redirect('kirish')


@login_required(login_url='kirish')
@admin_only
def m_c_create(request):
	if request.user.is_authenticated:
		if request.method == 'POST':
			form = CourseForm(request.POST)
			if form.is_valid():
				form.save()
				return redirect('m_c_database')
		else:
			form = CourseForm()
			context = {'form': form}
			return render(request, 'moderator/m_c_create.html', context)
	else:
		return redirect('kirish')

@login_required(login_url='kirish')
@admin_only
def m_c_update(request, pk):
	if request.user.is_authenticated:
		course = get_object_or_404(Course, pk=pk)
		form = CourseForm(request.POST or None, instance=course)
		if form.is_valid():
			form.save()
			return redirect('m_c_database')
		context = {"form": form}
		return render(request, 'moderator/m_c_update.html', context)
	else:
		return redirect('kirish')


@login_required(login_url='kirish')
@admin_only
def m_c_delete(request, pk):
	if request.user.is_authenticated:
		course = get_object_or_404(Course, pk=pk)
		if request.method == 'POST':
			course.delete()
			return redirect('m_c_database')
		context = {"course": course}
		return render(request, 'moderator/m_c_delete.html', context)
	else:
		return render('kirish')


# COURSE DATES













# TEACHER COURSES
@login_required(login_url='kirish')
@admin_only
def m_t_courses(request):
	if request.user.is_authenticated:
		name = Createcourse.objects.all().order_by('-datetime')
		context = {"name": name}
		return render(request, 'moderator/m_t_courses.html', context)
	else:
		return redirect('kirish')

@login_required(login_url='kirish')
@admin_only
def m_t_c_create(request):
	if request.user.is_authenticated:
		if request.method == 'POST':
			form = MCreatecourseForm(request.POST, request.FILES)
			if form.is_valid():
				form.save()
				return redirect('m_t_courses')
		else:
			form = MCreatecourseForm()
		context = {'form': form}
		return render(request, 'moderator/m_t_c_create.html', context)
	else:
		return render('kirish')


@login_required(login_url='kirish')
@admin_only
def m_t_c_update(request, pk):
	if request.user.is_authenticated:
		course = get_object_or_404(Createcourse, pk=pk)
		form = MCreatecourseForm(request.POST or None, instance=course)
		if request.method == 'POST':
			form.save()
			return redirect('m_t_courses')
		context = {"form": form}
		return render(request, 'moderator/m_t_c_update.html', context)
	else:
		return redirect('kirish')

@login_required(login_url='kirish')
@admin_only
def m_t_c_delete(request, pk):
	if request.user.is_authenticated:
		course = get_object_or_404(Createcourse, pk=pk)
		if request.method == 'POST':
			course.delete()
			return redirect('m_t_courses')
		context = {"course": course}
		return render(request, 'moderator/m_t_c_delete.html', context)
	else:
		return redirect('kirish')



@login_required(login_url='kirish')
@admin_only
def m_t_c_lessons(request, pk):
	if request.user.is_authenticated:
		name = Createlesson.objects.filter(user_id=pk).all()
		course = Createcourse.objects.get(pk=pk)
		# c = Createlesson.objects.count()
		context = {"name": name, "course": course}
		return render(request, 'moderator/m_t_c_lessons.html', context)
	else:
		return redirect('kirish')



@login_required(login_url='kirish')
@admin_only
def m_t_c_l_create(request, pk):
	if request.user.is_authenticated:
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
				return redirect('m_t_c_lessons', pk)
		context = {'form': form}
		return render(request, 'moderator/m_t_c_l_create.html', context)
	else:
		return redirect('kirish')



# TEACHER COURSES












# TASKS DATES
@login_required(login_url='kirish')
@admin_only
def m_tasks(request):
	if request.user.is_authenticated:
		tasks = Tasks.objects.all().order_by('-datetime')
		context = {"tasks": tasks}
		return render(request, 'moderator/m_tasks.html', context)
	else:
		return redirect('kirish')


@login_required(login_url='kirish')
@admin_only
def m_t_create(request):
	if request.user.is_authenticated:
		if request.method == 'POST':
			form = TasksForm(request.POST, request.FILES)
			if form.is_valid():
				form.save()
				return redirect('m_tasks')
		else:
			form = TasksForm()
		context = {'form': form}
		return render(request, 'moderator/m_t_create.html', context)
	else:
		return redirect('kirish')


@login_required(login_url='kirish')
@admin_only
def m_t_update(request, pk):
	if request.user.is_authenticated:
		task = get_object_or_404(Tasks, pk=pk)
		form = TasksForm(request.POST or None, instance=task)
		if form.is_valid():
			form.save()
			return redirect('m_tasks')
		context = {"form": form}
		return render(request, 'moderator/m_t_update.html', context)
	else:
		return redirect('kirish')


@login_required(login_url='kirish')
@admin_only
def m_t_delete(request, pk):
	if request.user.is_authenticated:
		task = get_object_or_404(Tasks, pk=pk)
		if request.method == 'POST':
			task.delete()
			return redirect('m_tasks')
		context = {"task": task}
		return render(request, 'moderator/m_t_delete.html', context)
	else:
		return redirect('kirish')


# TASKS DATES











# ARTICLES DATES

@login_required(login_url='kirish')
@admin_only
def m_articles(request):
	if request.user.is_authenticated:
		articles = Articles.objects.all().order_by('-datetime')
		context = {"articles": articles}
		return render(request, 'moderator/m_articles.html', context)
	else:
		return redirect('kirish')

@login_required(login_url='kirish')
@admin_only
def m_a_create(request):
	if request.user.is_authenticated:
		if request.method == 'POST':
			form = ArticlesForm(request.POST, request.FILES)
			if form.is_valid():
				form.save()
				return redirect('m_articles')
		else:
			form = ArticlesForm()
		context = {"form": form}
		return render(request, 'moderator/m_a_create.html', context)
	else:
		return redirect('kirish')

@login_required(login_url='kirish')
@admin_only
def m_a_update(request, pk):
	if request.user.is_authenticated:
		article = get_object_or_404(Articles, pk=pk)
		form = ArticlesForm(request.POST or None, instance=article)
		if form.is_valid():
			form.save()
			return redirect('m_articles')
		context = {"form": form}
		return render(request, 'moderator/m_a_update.html', context)
	else:
		return redirect('kirish')


@login_required(login_url='kirish')
@admin_only
def m_a_delete(request, pk):
	if request.user.is_authenticated:
		article = get_object_or_404(Articles, pk=pk)
		if request.method == 'POST':
			article.delete()
			return redirect('m_articles')
		context = {"article": article}
		return render(request, 'moderator/m_a_delete.html', context)
	else:
		return redirect('kirish')


# ARTICLES DATES













# WRITE DATES


@login_required(login_url='kirish')
@admin_only
def m_write(request):
	if request.user.is_authenticated:
		write = Write.objects.all().order_by('-datetime')
		context = {"write": write}
		return render(request, 'moderator/m_write.html', context)
	else:
		return redirect('kirish')


@login_required(login_url='kirish')
@admin_only
def m_w_create(request):
	if request.user.is_authenticated:
		if request.method == 'POST':
			form = WriteForm(request.POST, request.FILES)
			if form.is_valid():
				form.save()
				return redirect('m_write')
		else:
			form = WriteForm()
		context = {"form": form}
		return render(request, 'moderator/m_w_create.html', context)
	else:
		return redirect('kirish')


@login_required(login_url='kirish')
@admin_only
def m_w_update(request, pk):
	if request.user.is_authenticated:
		write = get_object_or_404(Write, pk=pk)
		form = WriteForm(request.POST or None, instance=write)
		if form.is_valid():
			form.save()
			return redirect('m_write')
		context = {"form": form}
		return render(request, 'moderator/m_w_update.html', context)
	else:
		return redirect('kirish')

@login_required(login_url='kirish')
@admin_only
def m_w_delete(request, pk):
	if request.user.is_authenticated:
		write = get_object_or_404(Write, pk=pk)
		if request.method == 'POST':
			write.delete()
			return redirect('m_write')
		context = {"write": write}
		return render(request, 'moderator/m_w_delete.html', context)
	else:
		return redirect('kirish')

# WRITE DATES


@login_required(login_url='kirish')
@admin_only
def m_t_application(request):
	if request.user.is_authenticated:
		applica = Teacher_Application.objects.all().order_by('-datetime')
		context = {"applica": applica}
		return render(request, 'moderator/m_t_application.html', context)
	else:
		return redirect('kirish')



@login_required(login_url='kirish')
@admin_only
def m_t_a_open(request, pk):
	if request.user.is_authenticated:
		applica = Teacher_Application.objects.get(id=pk)
		context = {"applica": applica}
		return render(request, 'moderator/m_t_a_open.html', context)
	else:
		return redirect('kirish')


@login_required(login_url='kirish')
@admin_only
def m_t_a_delete(request, pk):
	if request.user.is_authenticated:
		form = get_object_or_404(Teacher_Application, pk=pk)
		if request.method == 'POST':
			form.delete()
			return redirect('m_t_application')
		context = {"form":form}
		return render(request, 'moderator/m_t_a_delete.html', context)
	else:
		return redirect('kirish')

	
# 






# LOGOUT

def logout_view(request):
	logout(request)
	return redirect('kirish')

# LOGOUT



