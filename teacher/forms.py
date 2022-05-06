from django import forms

from moderator.models import User
from teacher.models import Userstaff, Course, Createcourse, Createlesson

from django.contrib.auth.forms import UserCreationForm
from django.db import transaction
from django.dispatch import receiver
from django.contrib.auth.models import Group
from django.forms.widgets import ClearableFileInput




# # CREATE Userstaff

SEX_CHOICES = (
  ('Erkak', 'Erkak'),
  ('Ayol', 'Ayol'),
  )
class UserUserstaffForm(UserCreationForm):
  last_name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'familya'}))
  first_name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'ism'}))
  email = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': "baxodirdavirov97@gmail.com"}))
  sex = forms.ChoiceField(choices = SEX_CHOICES)
  phone_number = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'type': 'number', 'placeholder': "+998(93)998-45-92"}))
  staff_image = forms.ImageField(required=False)
  # coursen = forms.ModelChoiceField(queryset = Course.objects.all(), required=True)


  class Meta(UserCreationForm.Meta):
    model = User

  @transaction.atomic
  def save(self, commit=True):
    user = super().save(commit=False)
    user.is_active = True
    user.is_staff = True

    if commit:
      user.save()
      group = Group.objects.get(name="teacher")
      user.groups.add(group)

    user.first_name = self.cleaned_data.get('first_name')
    user.last_name = self.cleaned_data.get('last_name')
    user.email = self.cleaned_data.get('email')
    user.save()
    userstaff = Userstaff.objects.create(user=user)
    userstaff.sex = self.cleaned_data.get('sex')
    userstaff.phone_number = self.cleaned_data.get('phone_number')
    userstaff.staff_image = self.cleaned_data.get('staff_image')
    userstaff.save()
    return user
  def __init__(self, *args, **kwargs):
    super().__init__(*args, **kwargs)
    self.fields['username'].widget.attrs.update({'class': 'form-control'})
    self.fields['password1'].widget.attrs.update({'class': 'form-control'})
    self.fields['password2'].widget.attrs.update({'class': 'form-control'})
    self.fields['sex'].widget.attrs.update({'class': 'form-control custom-select'})
    # self.fields['coursen'].widget.attrs.update({'class': 'form-control'})



class UserUserstaffUpdate(forms.ModelForm):
    about = forms.CharField(required=False, label="Yo'nalish", widget=forms.TextInput(
        attrs = {'class':'form-control rounded-1', 'autofocus': 'autofocus', 'placeholder': 'Bilish haqida'}
        ))
    address = forms.CharField(required=False, label="Yo'nalish", widget=forms.TextInput(
        attrs = {'class':'form-control rounded-1', 'autofocus': 'autofocus', 'placeholder': 'adress'}
        ))
    phone_number = forms.CharField(required=False, label="Yo'nalish", widget=forms.TextInput(
        attrs = {'class':'form-control rounded-1', 'autofocus': 'autofocus', 'placeholder': 'Tel nomer'}
        ))
    staff_image = forms.ImageField(label='Select Profile Image',required = False, widget=ClearableFileInput)

    class Meta:
        model = Userstaff
        fields = ('sex', 'about', 'address', 'phone_number', 'staff_image')

    def __init__(self, *args, **kwargs):
      super().__init__(*args, **kwargs)
      self.fields['sex'].widget.attrs.update({'class': 'form-control'})
      self.fields['staff_image'].widget.attrs.update({'class': 'form-control'})
      self.fields['staff_image'].widget.clear_checkbox_label = "Rasmni o'chirish"
      self.fields['staff_image'].widget.initial_text = "Rasmni ko'rish"
      self.fields['staff_image'].widget.input_text = "Yangi rasm tanlang"






# $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
# Muassasaning belgisi

class CourseForm(forms.ModelForm):
  name = forms.CharField(max_length=20, label = "", widget = forms.TextInput(attrs = {'class': 'form-control', 'placeholder': 'Yozing ...'}))

  class Meta:
    model = Course
    fields = ('name',)

# $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$




# $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$

class CreatecourseForm(forms.ModelForm):
  about = forms.CharField(label='', widget=forms.Textarea(attrs={'class': 'form-control', 'rows': '3', 'placeholder': 'Yozing ...'}))

  # user = forms.CharField(max_length=20, label = "", widget = forms.TextInput(attrs = {'class': 'form-control'}))
  
  class Meta:
    model = Createcourse
    fields = ('user', 'coursen', 'about', 'icon')

  def __init__(self, *args, **kwargs):
    super().__init__(*args, **kwargs)
    self.fields['user'].widget.attrs.update({'class': 'form-control'})
    self.fields['coursen'].widget.attrs.update({'class': 'form-select'})
    # self.fields['icon'].widget.attrs.update({'class': 'form-control'})


# $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$



# $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$

class UpdatecourseForm(forms.ModelForm):
  about = forms.CharField(label='', widget=forms.Textarea(attrs={'class': 'form-control', 'rows': '3', 'placeholder': 'Yozing ...'}))

  # user = forms.CharField(max_length=20, label = "", widget = forms.TextInput(attrs = {'class': 'form-control'}))
  
  class Meta:
    model = Createcourse
    fields = ('coursen', 'about', 'icon')

  def __init__(self, *args, **kwargs):
    super().__init__(*args, **kwargs)
    self.fields['coursen'].widget.attrs.update({'class': 'form-select'})
    self.fields['icon'].widget.attrs.update({'class': 'form-control'})
    self.fields['icon'].widget.clear_checkbox_label = "Rasmni o'chirish"
    self.fields['icon'].widget.initial_text = "Rasmni ko'rish"
    self.fields['icon'].widget.input_text = "Yangi rasm tanlang"

# $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$



# $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$

class CreatelessonForm(forms.ModelForm):
  title = forms.CharField(max_length=300, widget = forms.TextInput(attrs = {'class': 'form-control', 'placeholder': 'Yozing ...'}))
  description = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control', 'rows': '3', 'placeholder': 'Yozing ...'}))


  class Meta:
    model = Createlesson
    fields = ('title', 'description', 'text')

  def __init__(self, *args, **kwargs):
    super().__init__(*args, **kwargs)
    self.fields['text'].widget.attrs.update({'class': 'form-control', 'style': 'with:100%'})

# $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$



# $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
# Yangilash
class UpdatelessonForm(forms.ModelForm):
  title = forms.CharField(max_length=300, widget = forms.TextInput(attrs = {'class': 'form-control', 'placeholder': 'Yozing ...'}))
  description = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control', 'rows': '3', 'placeholder': 'Yozing ...'}))


  class Meta:
    model = Createlesson
    fields = ('title', 'description', 'text')

  def __init__(self, *args, **kwargs):
    super().__init__(*args, **kwargs)
    self.fields['text'].widget.attrs.update({'class': 'form-control'})

# $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$

