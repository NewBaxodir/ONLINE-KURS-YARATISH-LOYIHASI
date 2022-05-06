from django.db import models
from ckeditor.fields import RichTextField
# Create your models here.

# /////////////////////////////////////////////////////

class Course(models.Model):
	name = models.CharField(max_length=500, verbose_name="Kursning nomi")

	def __str__(self):
		return '%s' %(self.name)

	class Meta:
		verbose_name = "2. Kurslar bazasi"

# /////////////////////////////////////////////////////



# /////////////////////////////////////////////////////

class Userstaff(models.Model):
	user = models.OneToOneField(to='moderator.User', on_delete = models.CASCADE, primary_key = True)
	SEX_CHOICES = (
		('Erkak', 'Erkak'),
		('Ayol', 'Ayol'),
		)
	sex = models.CharField(max_length=100, verbose_name="Jinsi", null=True, blank=True, choices= SEX_CHOICES)
	about = models.CharField(max_length=100, verbose_name="O'qtuvchi bilish doirasi", null=True, blank=True)
	address = models.CharField(max_length=300, verbose_name="O'quv joyi manzili", null=True, blank=True)
	phone_number = models.CharField(max_length=17, null=True, blank=True, verbose_name='telefon nomer')
	staff_image = models.ImageField(null=True, blank=True, upload_to='staff_images')

	def __str__(self):
		return '%s %s' %(self.user.id, self.user)

	class Meta:
		verbose_name = '1. Hodimlar bazasi'

# /////////////////////////////////////////////////////




# /////////////////////////////////////////////////////

class Createcourse(models.Model):
	# title0 = "Foydalanuvchi bilan o'zaro ko'pga bir modeli"
    user = models.ForeignKey(Userstaff, on_delete = models.CASCADE)
    coursen = models.ForeignKey(Course, on_delete=models.CASCADE, null=True, blank=True)
    about = models.TextField(verbose_name="Kursingiz haqida batafsil yozing")
    icon = models.ImageField(null=True, blank=True, upload_to='course/')
    datetime = models.DateTimeField(auto_now=True)

    def __str__(self):
    	return '%s %s' %(self.user, self.coursen)

    class Meta:
    	verbose_name = '3. Oqtuvchiga kurs biriktrish'

# /////////////////////////////////////////////////////




# /////////////////////////////////////////////////////

class Createlesson(models.Model):
	user = models.ForeignKey(Createcourse, on_delete = models.CASCADE)
	title = models.CharField(max_length=200, verbose_name="Sarlavha matni", null=True, blank=True)
	description = models.TextField(verbose_name="Qisqacha malumot")
	text = RichTextField()
	datetime = models.DateTimeField(auto_now=True)

	def __str__(self):
		return '%s' %(self.user)

	class Meta:
		verbose_name = '4. Darsliklarni ishlab chiqish'

	def num_id(self):
		return self.id.all().count()

# /////////////////////////////////////////////////////