import random
from django import forms
from django.contrib.auth.forms import PasswordResetForm
from django.contrib.auth.password_validation import validate_password
from . import models


AVATARS_CHOICES = [
    'male',
    'female',
    'human',
    'identicon',
    'initials',
    'bottts',
    'avataaars',
    'jdenticon',
    'gridy',
    'code',
]

AVATAR_URL_PREFIX = 'https://avatars.dicebear.com/v2/'


class LoginForm(forms.Form):

    email = forms.EmailField(widget=forms.EmailInput(
        attrs={"placeholder": "Email"}))
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={"placeholder": "Password"})
    )

    def clean(self):
        email = self.cleaned_data.get("email")
        password = self.cleaned_data.get("password")

        try:
            user = models.User.objects.get(email=email)
            if user.check_password(password):
                return self.cleaned_data
            else:
                self.add_error('password', forms.ValidationError(
                    "Password is wrong."))
        except:
            self.add_error("email", forms.ValidationError(
                "Password is wrong."))


class SignUpForm(forms.ModelForm):

    class Meta:
        model = models.User
        fields = ("first_name", "last_name", "email", "username",)
        widgets = {
            "first_name": forms.TextInput(attrs={"placeholder": "First Name"}),
            "last_name": forms.TextInput(attrs={"placeholder": "Last Name"}),
            "email": forms.EmailInput(attrs={"Placeholder": "Email"}),
            "username": forms.TextInput(attrs={"Placeholder": "Username"}),
        }

    password = forms.CharField(
        widget=forms.PasswordInput(attrs={"placeholder": "Password"})
    )
    password_confirm = forms.CharField(
        widget=forms.PasswordInput(attrs={"placeholder": "Password Confirm"})
    )

    def clean_email(self):
        email = self.cleaned_data.get("email")
        try:
            models.User.objects.get(email=email)
            raise forms.ValidationError(
                "That email is already exists", code="existing_user"
            )
        except models.User.DoesNotExist:
            return email

    def clean_password_confirm(self):
        password = self.cleaned_data.get("password")
        password_confirm = self.cleaned_data.get("password_confirm")

        if password != password_confirm:
            raise forms.ValidationError("Password is not matched.")
        else:
            validate_password(self.cleaned_data.get("password"), self.instance)
            return password

    def clean_username(self):
        username = self.cleaned_data.get("username")
        try:
            models.User.objects.get(username=username)
            raise forms.ValidationError(
                "That username is already taken!", code="exisiting_user"
            )
        except models.User.DoesNotExist:
            return username

    def save(self, *args, **kwargs):
        user = super().save(commit=False)
        email = self.cleaned_data.get("email")
        password = self.cleaned_data.get("password")
        user.default_avatar_img_url = self.generateRandomAvatarURL()
        user.username = email
        user.set_password(password)
        user.save()

    def generateRandomAvatarURL(self):
        url = AVATAR_URL_PREFIX + \
            random.choice(AVATARS_CHOICES) + '/' + \
            self.cleaned_data.get('first_name') + '.svg'
        print(url)
        return url


class EditProfileForm(forms.ModelForm):

    class Meta:
        model = models.User
        fields = (
            'first_name',
            'last_name',
            'avatar',
            'job_title',
            'email',
            'bio',
        )
