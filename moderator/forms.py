from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.db import transaction
from django.dispatch import receiver
from django.contrib.auth.models import Group
from django.forms.widgets import ClearableFileInput


from moderator.models import User, Usermoderator, Tasks, Articles, Write, Teacher_Application
from teacher.models import Createcourse



# MODERATOR BOSHQARISHI UCHUN FORMA 
# MODERATORLARNI O'ZGARTIRISH UCHUN FORMA


class UserForm(forms.ModelForm):
    last_name = forms.CharField(required=False, label="Familya", widget=forms.TextInput(
        attrs = {'class':'form-control rounded-1', 'autofocus': 'autofocus', 'placeholder': 'Familya'}
        ))
    first_name = forms.CharField(required=False, label="Ism", widget=forms.TextInput(
        attrs = {'class':'form-control rounded-1', 'placeholder': 'Ism'}
        ))   
    email = forms.CharField(required=False, widget=forms.TextInput(
        attrs = {'class':'form-control rounded-1', 'placeholder': 'Email'}
        ))
    username = forms.CharField(required=False, widget=forms.TextInput(
        attrs = {'class':'form-control rounded-1', 'placeholder': 'Логин'}
        ))

    class Meta:
        model = User
        fields = ('last_name', 'first_name', 'email', 'username')


# MODERATOR BOSHQARISHI UCHUN FORMA 
# MODERATORLARNI O'ZGARTIRISH UCHUN FORMA




# MODERATOR BOSHQARISHI UCHUN FORMA 
# MODERATORLARNI RO'YHATDAN O'TKAZISH


SEX_CHOICES = (
  ('Erkak', 'Erkak'),
  ('Ayol', 'Ayol'),
  )
class UsermoderatorForm(UserCreationForm):
  last_name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'familya'}))
  first_name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'ism'}))
  email = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': "baxodirdavirov97@gmail.com"}))
  sex = forms.ChoiceField(choices = SEX_CHOICES)
  phone_number = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'type': 'number', 'placeholder': "+998(93)998-45-92"}))
  staff_image = forms.ImageField(required=False)

  class Meta(UserCreationForm.Meta):
    model = User

  @transaction.atomic
  def save(self, commit=True):
    user = super().save(commit=False)
    user.is_active = True
    user.is_staff = True
    user.is_superuser = True

    if commit:
      user.save()
      group = Group.objects.get(name="moderator")
      user.groups.add(group)

    user.first_name = self.cleaned_data.get('first_name')
    user.last_name = self.cleaned_data.get('last_name')
    user.email = self.cleaned_data.get('email')
    user.save()
    usermoderator = Usermoderator.objects.create(user=user)
    usermoderator.sex = self.cleaned_data.get('sex')
    usermoderator.phone_number = self.cleaned_data.get('phone_number')
    usermoderator.staff_image = self.cleaned_data.get('staff_image')
    usermoderator.save()
    return user
  def __init__(self, *args, **kwargs):
    super().__init__(*args, **kwargs)
    self.fields['username'].widget.attrs.update({'class': 'form-control'})
    self.fields['password1'].widget.attrs.update({'class': 'form-control'})
    self.fields['password2'].widget.attrs.update({'class': 'form-control'})
    self.fields['sex'].widget.attrs.update({'class': 'form-control custom-select'})
    # self.fields['staff_image'].widget.attrs.update({'class': 'form-control'})


# MODERATOR BOSHQARISHI UCHUN FORMA 
# MODERATORLARNI RO'YHATDAN O'TKAZISH


 




# MODERATOR BOSHQARISHI UCHUN FORMA 
# KURSNI O'QITUVCHIGA BIRIKTIRISH

class MCreatecourseForm(forms.ModelForm):
  about = forms.CharField(label='', widget=forms.Textarea(attrs={'class': 'form-control', 'rows': '3', 'placeholder': 'Yozing ...', "style": "height: 200px;"}))
  class Meta:
    model = Createcourse
    fields = ('user', 'coursen', 'about')

  def __init__(self, *args, **kwargs):
    super().__init__(*args, **kwargs)
    self.fields['user'].widget.attrs.update({'class': 'form-control'})
    self.fields['coursen'].widget.attrs.update({'class': 'form-control'})


# MODERATOR BOSHQARISHI UCHUN FORMA 
# KURSNI O'QITUVCHIGA BIRIKTIRISH




# MODERATOR BOSHQARISHI UCHUN FORMA 
# TOPSHIRIQ YARATISH

class TasksForm(forms.ModelForm):
  title = forms.CharField(max_length=300, widget = forms.TextInput(attrs = {'class': 'form-control', 'placeholder': 'Yozing ...'}))
  description = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control', 'rows': '3', 'placeholder': 'Yozing ...'}))
  image = forms.ImageField(label='Select Profile Image',required = False, widget=ClearableFileInput)


  class Meta:
    model = Tasks
    fields = ('image', 'title', 'description', 'text')

  def __init__(self, *args, **kwargs):
    super().__init__(*args, **kwargs)
    self.fields['image'].widget.attrs.update({'class': 'form-control', 'type': 'file' })
    self.fields['text'].widget.attrs.update({'class': 'form-control', 'style': 'with:100%'})
    self.fields['image'].widget.attrs.update({'class': 'form-control'})

# MODERATOR BOSHQARISHI UCHUN FORMA 
# TOPSHIRIQ YARATISH




# MODERATOR BOSHQARISHI UCHUN FORMA 
# MAQOLALAR YARATISH

class ArticlesForm(forms.ModelForm):
  title = forms.CharField(max_length=300, widget = forms.TextInput(attrs = {'class': 'form-control', 'placeholder': 'Yozing ...'}))
  description = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control', 'rows': '3', 'placeholder': 'Yozing ...'}))


  class Meta:
    model = Articles
    fields = ('image', 'title', 'description', 'text')

  def __init__(self, *args, **kwargs):
    super().__init__(*args, **kwargs)
    self.fields['text'].widget.attrs.update({'class': 'form-control'})

# MODERATOR BOSHQARISHI UCHUN FORMA 
# MAQOLALAR YARATISH




# MODERATOR BOSHQARISHI UCHUN FORMA 
# DASTUR KODLARI YARATISH

class WriteForm(forms.ModelForm):
  title = forms.CharField(max_length=300, widget = forms.TextInput(attrs = {'class': 'form-control', 'placeholder': 'Yozing ...'}))
  description = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control', 'rows': '3', 'placeholder': 'Yozing ...'}))


  class Meta:
    model = Write
    fields = ('image', 'title', 'description', 'text')

  def __init__(self, *args, **kwargs):
    super().__init__(*args, **kwargs)
    self.fields['text'].widget.attrs.update({'class': 'form-control', 'style': 'with:100%'})


# MODERATOR BOSHQARISHI UCHUN FORMA 
# DASTUR KODLARI YARATISH


class Teacher_ApplicationForm(forms.ModelForm):
  last_name = forms.CharField(max_length=200, label='Familya',  widget = forms.TextInput(attrs = {'class': 'form-control', 'placeholder': 'Familya'}))
  first_name = forms.CharField(max_length=200, label='Ism', widget = forms.TextInput(attrs = {'class': 'form-control', 'placeholder': 'Ism'}))
  phone_number = forms.CharField(max_length=200, label='Tel nomer', widget = forms.TextInput(attrs = {'class': 'form-control', 'placeholder': 'Tel nomer'}))
  email = forms.CharField(max_length=200, label='Email', widget = forms.TextInput(attrs = {'class': 'form-control', 'placeholder': 'Email'}))
  about = forms.CharField(label='Kurs haqida', widget=forms.Textarea(attrs={'class': 'form-control', 'style': 'height: 150px;', 'rows': '3', 'placeholder': 'IT sohasi boyicha qanday kurs ochmoqchisiz? shu haqda bizga yozing ...'}))
  upload = forms.FileField(label='Tarjimai holingizni yuklang', required=False, widget=forms.ClearableFileInput(attrs={'class': 'form-control'}))

  class Meta:
    model = Teacher_Application
    fields = ('last_name', 'first_name', 'phone_number', 'email', 'about', 'upload')
