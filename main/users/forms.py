from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django import forms
from main.users.models import User


class UserRegisterForm(UserCreationForm):

    class Meta:
        model = User
        fields = ("email", "password1", "password2")


class UserProfileForm(UserChangeForm):

    class Meta:
        model = User
        fields = ("email",
                  "first_name",
                  "last_name",
                  "phone",
                  "country",
                  "avatar")

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)  # скрывает поле пароля

        self.fields['password'].widget = forms.HiddenInput()