from django.contrib import admin
from student.models import Userstudent
# Register your models here.



# Talabalar bazasi
class UserstudentAdmin(admin.ModelAdmin):
	list_display = ("user", "phone_number", "sex", "student_image")

admin.site.register(Userstudent, UserstudentAdmin)

# /////////////////////////////////////////////////////////