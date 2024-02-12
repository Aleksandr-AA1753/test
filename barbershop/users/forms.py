import datetime

from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm, PasswordChangeForm


class ProfileUserForm(forms.ModelForm):
    username = forms.CharField(disabled = True, label = "Логин", 
        widget = forms.TextInput(attrs = {'class': 'form-input'}))
    email = forms.EmailField(disabled = True, label = "E-mail",
        widget = forms.TextInput(attrs= {'class': 'form-input'}))
    this_year = datetime.date.today().year
    birthday = forms.DateField(widget=forms.SelectDateWidget(years=tuple(range(this_year-100, this_year-5))))

    class Meta:
        model = get_user_model()
        fields = ['photo', 'username', 'email', 'birthday', 'first_name', 'last_name']
        labels = {
            'first_name' : 'Имя',
            'last_name' : 'Фамилия'
        }
        widgets = {
            'first_name': forms.TextInput(attrs={'class': 'form-input'}),
            'last_name': forms.TextInput(attrs={'class': 'form-input'}),
        }