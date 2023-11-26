from django import forms
from django.contrib.auth import get_user_model
from django.core.exceptions import ValidationError
from django.core.validators import RegexValidator, validate_email
from django.forms import ModelForm, PasswordInput


class LoginForm(forms.Form):
    username = forms.CharField(required=True, label='Введите логин')
    password = forms.CharField(required=True, label='Введите пароль')


class RegisterForm(ModelForm):
    class Meta:
        model = get_user_model()
        fields = ['username', 'email']
    username = forms.CharField(min_length=3, max_length=10, required=True, label='Введите логин', validators=[
        RegexValidator(
            regex='^[a-zA-Z0-9]*$',
            message='Может содержать только латинские буквы и цифры!',
            code='invalid_username'
        ),
    ])
    email = forms.CharField(min_length=3, required=True, label='Введите почту')
    password = forms.CharField(widget=PasswordInput(), required=True, label='Введите пароль')
    password_confirm = forms.CharField(widget=PasswordInput(), required=True, label='Введите пароль снова')
    icon = forms.ImageField(label="Файл")

    def clean(self):
        cleaned_data = super(RegisterForm, self).clean()
        password = cleaned_data.get("password")
        password_confirm = cleaned_data.get("password_confirm")
        if password != password_confirm:
            raise forms.ValidationError(
                {'password_confirm': "Пароли не совпадают!", 'password': ''}
            )
        username = self.cleaned_data.get("username")
        if get_user_model().objects.filter(username=username).exists():
            raise forms.ValidationError({'username': "Данный логин уже занят!"})
        try:
            validate_email(self.cleaned_data.get("email"))
        except ValidationError as e:
            raise forms.ValidationError({'email': "Введите электронную почту правильно!"})
        return cleaned_data