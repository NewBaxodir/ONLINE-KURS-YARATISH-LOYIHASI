from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from moderator.models import User, Usermoderator, Tasks, Articles, Write, Teacher_Application
# Register your models here.


# Umumiy foydalanuchilar bazasi 
class UserAdmin(UserAdmin):
	list_display = ("id", "last_name", "first_name", "date_joined", "is_superuser", "is_active", "is_staff", "password")

admin.site.register(User, UserAdmin)

# /////////////////////////////////////////////////////////



# Hodimlar bazasi 
class UsermoderatorAdmin(admin.ModelAdmin):
	list_display = ("user_id", "user", "staff_image", "phone_number", "sex")

admin.site.register(Usermoderator, UsermoderatorAdmin)

# /////////////////////////////////////////////////////////


# Topshiriqlar
class TasksAdmin(admin.ModelAdmin):
	list_display = ("id", "title", "description", "text", "image", "datetime")

admin.site.register(Tasks, TasksAdmin)

# /////////////////////////////////////////////////////////


# Maqolalar
class ArticlesAdmin(admin.ModelAdmin):
	list_display = ("id", "title", "description", "text", "image", "datetime")

admin.site.register(Articles, ArticlesAdmin)

# /////////////////////////////////////////////////////////

# Hodimlar bazasi 
class WriteAdmin(admin.ModelAdmin):
	list_display = ("id", "title", "description", "text", "image", "datetime")

admin.site.register(Write, WriteAdmin)

# /////////////////////////////////////////////////////////



# /////////////////////////////////////////////////////////

# Hodimlar bazasi 
class Teacher_ApplicationAdmin(admin.ModelAdmin):
	list_display = ("last_name", "first_name", "phone_number", "email", "about")

admin.site.register(Teacher_Application, Teacher_ApplicationAdmin)

# /////////////////////////////////////////////////////////


