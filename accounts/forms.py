from django import forms
from django.contrib.auth import get_user_model, authenticate
from django.contrib.auth.hashers import check_password

User = get_user_model()


class UserLoginForm(forms.Form):
    username = forms.CharField(label='username', widget=forms.TextInput(attrs={  #Изменение формы
        'class': 'form-control',
        'placeholder': 'Введите Username'
    }))

    password = forms.CharField(label='password', widget=forms.PasswordInput(attrs={  # Изменение формы
        'class': 'form-control',
        'placeholder': 'Введите password'
    }))

    def clean(self, *args, **kwargs):
        username = self.cleaned_data.get('username')
        password = self.cleaned_data.get('password')
        if username and password:
            qs = User.objects.filter(username=username)
            if not qs.exists():
                raise forms.ValidationError('Такого пользователя нет')
            #Проверка зашифрованного пароля
            if not check_password(password, qs[0].password):
                raise forms.ValidationError('Неверный пароль')
            #Проверка пользователя на активность
            user = authenticate(username=username, password=password)
            if not user:
                raise forms.ValidationError('Данный пользователь невктивен')
        return super().clean(*args, **kwargs)


class UserRegistrationForm(forms.ModelForm):
    username = forms.CharField(label='username', widget=forms.TextInput(attrs={  #Изменение формы
        'class': 'form-control',
        'placeholder': 'Введите Username'
    }))

    password = forms.CharField(label='password', widget=forms.PasswordInput(attrs={  # Изменение формы
        'class': 'form-control',
        'placeholder': 'Введите password'
    }))
    password_2 = forms.CharField(label='password', widget=forms.PasswordInput(attrs={  # Изменение формы
        'class': 'form-control',
        'placeholder': 'Введите password'
    }))

    class Meta:
        model = User
        fields = ('username',)

    # Проверка совпадения двух паролей
    def clean_password_2(self):
        data = self.cleaned_data
        if data['password'] != data['password_2']:
            raise forms.ValidationError('Пароли не совпадают')
        return data['password_2']
