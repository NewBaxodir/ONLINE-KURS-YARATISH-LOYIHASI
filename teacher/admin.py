from django.contrib import admin

# Register your models here.
from teacher.models import Userstaff, Course, Createcourse, Createlesson



# Hodimlar bazasi 
class CourseAdmin(admin.ModelAdmin):
	list_display = ("id", "name",)

admin.site.register(Course, CourseAdmin)
# /////////////////////////////////////////////////////////




# Hodimlar bazasi 
class UserstaffAdmin(admin.ModelAdmin):
	list_display = ("user", "staff_image", "phone_number", "sex")

admin.site.register(Userstaff, UserstaffAdmin)
# /////////////////////////////////////////////////////////



# Hodimlar bazasi 
class CreatecourseAdmin(admin.ModelAdmin):
	list_display = ("id","user", "coursen", "about", "icon")

admin.site.register(Createcourse, CreatecourseAdmin)

# /////////////////////////////////////////////////////////




# Hodimlar bazasi 
class CreatelessonAdmin(admin.ModelAdmin):
	list_display = ("id", "user", "description", "text")

admin.site.register(Createlesson, CreatelessonAdmin)

# /////////////////////////////////////////////////////////




