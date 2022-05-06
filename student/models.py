from django.db import models

# Create your models here.

# BARCHA TALABALARNI RO'YXATDAN O'TKAZISH UCHUN MODEL

class Userstudent(models.Model):
	# Umumiy baza bilan bog'lanish 
	user = models.OneToOneField(to='moderator.User', on_delete = models.CASCADE, primary_key = True)
	title = 'Shaxsiy malumotlar'
	SEX_CHOICES = (
		('Erkak', 'Erkak'),
		('Ayol', 'Ayol'),
		)
	sex = models.CharField(max_length=100, null=True, blank=True, verbose_name="Jinsi", choices= SEX_CHOICES)
	phone_number = models.CharField(max_length=30, null=True, blank=True, verbose_name='telefon nomer')
	student_image = models.ImageField(null=True, blank=True, upload_to='student_images')

	def __str__(self):
		return '%s' %(self.user)

	class Meta:
		verbose_name = '1. Talabalar bazasi'


# /////////////////////////////////////////////////////