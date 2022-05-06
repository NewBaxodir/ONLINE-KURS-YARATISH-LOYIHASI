from django.db import models
from django.contrib.auth.models import AbstractUser
from ckeditor.fields import RichTextField
from teacher.models import Course
from phone_field import PhoneField

class User(AbstractUser):
	last_name = models.CharField(max_length=100)
	first_name = models.CharField(max_length=100)
	email = models.CharField(max_length=100)

	def __str__(self):
		return '%s %s' %(self.last_name, self.first_name)

	class Meta:
		verbose_name = '1. Umumiy foy bazasi'

# /////////////////////////////////////////////////////


# /////////////////////////////////////////////////////

class Usermoderator(models.Model):
	user = models.OneToOneField(to='moderator.User', on_delete = models.CASCADE, primary_key = True)
	SEX_CHOICES = (
		('Erkak', 'Erkak'),
		('Ayol', 'Ayol'),
		)
	sex = models.CharField(max_length=100, verbose_name="Jinsi", null=True, blank=True, choices= SEX_CHOICES)
	phone_number = models.CharField(max_length=17, null=True, blank=True, verbose_name='telefon nomer')
	staff_image = models.ImageField(null=True, blank=True, upload_to='moderator/')


	def __str__(self):
		return '%s' %(self.user)

	class Meta:
		verbose_name = '2. Moderatorlar bazasi'

# /////////////////////////////////////////////////////




# /////////////////////////////////////////////////////
# Saytda topshiriqlar elon qilish
class Tasks(models.Model):
	image = models.ImageField(null=True, blank=True, upload_to='tasks/')
	title = models.CharField(max_length=200, verbose_name="Sarlavha")
	description = models.TextField(verbose_name="Qisqacha malumot")
	text = RichTextField()
	datetime = models.DateTimeField(auto_now=True)

	def __str__(self):
		return '%s' %(self.title)

	class Meta:
		verbose_name = '3. Topshiriqlar'

# /////////////////////////////////////////////////////


# /////////////////////////////////////////////////////
# Saytda Maqolalarni elon qilish
class Articles(models.Model):
	image = models.ImageField(null=True, blank=True, upload_to='articles/')
	title = models.CharField(max_length=200, verbose_name="Sarlavha")
	description = models.TextField(verbose_name="Qisqacha malumot")
	text = RichTextField()
	datetime = models.DateTimeField(auto_now=True)

	
	def __str__(self):
		return '%s' %(self.title)

	class Meta:
		verbose_name = '4. Maqolalar'

# /////////////////////////////////////////////////////


# /////////////////////////////////////////////////////
# Saytda Yangi dasturlarni yozish uchun videolar
class Write(models.Model):
	image = models.ImageField(null=True, blank=True, upload_to='write/')
	title = models.CharField(max_length=200, verbose_name="Sarlavha")
	description = models.TextField(verbose_name="Qisqacha malumot")
	text = RichTextField()
	datetime = models.DateTimeField(auto_now=True)

	def __str__(self):
		return '%s' %(self.title)

	class Meta:
		verbose_name = '5. Eng yaxshi dasturlarni yozish'
# /////////////////////////////////////////////////////




# //////////////////////////////////////////////////////  
class Teacher_Application(models.Model):
	last_name = models.CharField(max_length=200, verbose_name="Familya")
	first_name = models.CharField(max_length=200, verbose_name="Ism")
	phone_number = models.CharField(max_length=30, verbose_name="Tel nomber")
	email = models.EmailField(max_length=200, verbose_name="Email")
	about = models.TextField(verbose_name="Kurs haqida qisqacha malumot")
	upload = models.FileField(upload_to='cv/', null=True, blank=True)
	datetime = models.DateTimeField(auto_now=True)

	def __str__(self):
		return '%s' %(self.last_name)

	class Meta:
		verbose_name = '5. Kurs ochish arizasi'
# /////////////////////////////////////////////////////
