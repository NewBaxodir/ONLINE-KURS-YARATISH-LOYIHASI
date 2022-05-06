from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.db import transaction
from django.dispatch import receiver
from django.contrib.auth.models import Group
from django.forms.widgets import ClearableFileInput


from moderator.models import User
from student.models import Userstudent



# MODERATOR BOSHQARISHI UCHUN FORMA 
# MODERATORLARNI RO'YHATDAN O'TKAZISH


SEX_CHOICES = (
  ('Erkak', 'Erkak'),
  ('Ayol', 'Ayol'),
  )
class UserstudentForm(UserCreationForm):
  last_name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'familya'}))
  first_name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'ism'}))
  email = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': "baxodirdavirov97@gmail.com"}))
  sex = forms.ChoiceField(choices = SEX_CHOICES)
  phone_number = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'type': 'number', 'placeholder': "+998(93)998-45-92"}))
  student_image = forms.ImageField(required=False)

  class Meta(UserCreationForm.Meta):
    model = User

  @transaction.atomic
  def save(self, commit=True):
    user = super().save(commit=False)
    user.is_active = True


    if commit:
      user.save()
      group = Group.objects.get(name="student")
      user.groups.add(group)

    user.first_name = self.cleaned_data.get('first_name')
    user.last_name = self.cleaned_data.get('last_name')
    user.email = self.cleaned_data.get('email')
    user.save()
    userstudent = Userstudent.objects.create(user=user)
    userstudent.sex = self.cleaned_data.get('sex')
    userstudent.phone_number = self.cleaned_data.get('phone_number')
    userstudent.student_image = self.cleaned_data.get('student_image')
    userstudent.save()
    return user
  def __init__(self, *args, **kwargs):
    super().__init__(*args, **kwargs)
    self.fields['username'].widget.attrs.update({'class': 'form-control'})
    self.fields['password1'].widget.attrs.update({'class': 'form-control'})
    self.fields['password2'].widget.attrs.update({'class': 'form-control'})
    self.fields['sex'].widget.attrs.update({'class': 'form-control custom-select'})
    # self.fields['student_image'].widget.attrs.update({'class': 'form-control'})


# MODERATOR BOSHQARISHI UCHUN FORMA 
# MODERATORLARNI RO'YHATDAN O'TKAZISH


class RegUserstudentForm(UserCreationForm):
  first_name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ism', 'autofocus': 'autofocus'}))
  email = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': "example@gmail.com"}))
  phone_number = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'type': 'number', 'placeholder': "+998(xx)xxx-xx-xx"}))
  username = forms.CharField(required=False, widget=forms.TextInput(
        attrs = {'class':'form-control rounded-1', 'placeholder': 'Login'}
        ))
  password1 = forms.CharField(required=False, widget=forms.TextInput(
        attrs = {'class':'form-control rounded-1', 'placeholder': 'parol-1'}
        ))
  password2 = forms.CharField(required=False, widget=forms.TextInput(
        attrs = {'class':'form-control rounded-1', 'placeholder': 'parol-qayta'}
        ))
  class Meta(UserCreationForm.Meta):
    model = User

  @transaction.atomic
  def save(self, commit=True):
    user = super().save(commit=False)
    user.is_active = True


    if commit:
      user.save()
      group = Group.objects.get(name="student")
      user.groups.add(group)

    user.first_name = self.cleaned_data.get('first_name')
    user.email = self.cleaned_data.get('email')
    user.save()
    userstudent = Userstudent.objects.create(user=user)
    userstudent.phone_number = self.cleaned_data.get('phone_number')
    userstudent.save()
    return user
  def __init__(self, *args, **kwargs):
    super().__init__(*args, **kwargs)
    self.fields['username'].widget.attrs.update({'class': 'form-control'})
    self.fields['password1'].widget.attrs.update({'class': 'form-control'})
    self.fields['password2'].widget.attrs.update({'class': 'form-control'})
    # self.fields['student_image'].widget.attrs.update({'class': 'form-control'})


# MODERATOR BOSHQARISHI UCHUN FORMA 
# MODERATORLARNI RO'YHATDAN O'TKAZISH




class UserstudentUpdate(forms.ModelForm):
    phone_number = forms.CharField(required=False, label="Yo'nalish", widget=forms.TextInput(
        attrs = {'class':'form-control rounded-1', 'autofocus': 'autofocus', 'placeholder': 'Tel nomer'}
        ))
    student_image = forms.ImageField(label='Select Profile Image',required = False, widget=ClearableFileInput)

    class Meta:
        model = Userstudent
        fields = ('sex', 'phone_number', 'student_image')

    def __init__(self, *args, **kwargs):
      super().__init__(*args, **kwargs)
      self.fields['sex'].widget.attrs.update({'class': 'form-control'})
      self.fields['student_image'].widget.attrs.update({'class': 'form-control'})
      self.fields['student_image'].widget.clear_checkbox_label = "Rasmni o'chirish"
      self.fields['student_image'].widget.initial_text = "Rasmni ko'rish"
      self.fields['student_image'].widget.input_text = "Yangi rasm tanlang"


