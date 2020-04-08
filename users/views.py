import os
from django.conf import settings
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import (
    PasswordChangeView,
    PasswordResetConfirmView,
    PasswordResetDoneView,
    PasswordResetView,
)
from django.contrib.messages.views import SuccessMessageMixin
from django.core.files.base import ContentFile
from django.shortcuts import redirect, reverse
from django.urls import reverse_lazy
from django.views.generic import DetailView, FormView, UpdateView
from . import forms, mixins, models


class LoginView(mixins.LoggedOutOnlyView, FormView):

    template_name = "pages/signin-page.html"
    form_class = forms.LoginForm

    def form_valid(self, form):
        email = form.cleaned_data.get("email")
        password = form.cleaned_data.get("password")
        user = authenticate(self.request, username=email, password=password)
        if user is not None:
            login(self.request, user)
        return super().form_valid(form)

    def get_success_url(self):
        next_arg = self.request.GET.get("next")
        if next_arg is not None:
            return next_arg
        else:
            return reverse("core:home")


def log_out(request):
    messages.info(request, "See you later!")
    logout(request)
    return redirect(reverse("core:home"))


class SignUpView(FormView):

    template_name = "pages/signup-page.html"
    form_class = forms.SignUpForm
    success_url = reverse_lazy("core:home")

    def form_valid(self, form):
        form.save()
        email = form.cleaned_data.get("email")
        password = form.cleaned_data.get("password")
        user = authenticate(self.request, username=email, password=password)
        if user is not None:
            login(self.request, user)
        return super().form_valid(form)


class ResetPasswordView(PasswordResetView):

    template_name = "users/password-reset.html"
    email_template_name = "emails/password_reset_email.html"
    from_email = settings.EMAIL_FROM
    success_url = reverse_lazy("users:password_reset_done")

    def get_form(self, form_class=None):
        form = super().get_form(form_class=form_class)
        form.fields["email"].widget.attrs = {"placeholder": "Email"}
        return form


class ResetPasswordConfirmView(PasswordResetConfirmView):

    template_name = "users/password-reset-confirm.html"
    success_url = reverse_lazy("users:password_reset_complete")

    def get_form(self, form_class=None):
        form = super().get_form(form_class=form_class)
        form.fields["new_password1"].widget.attrs = {
            "placeholder": "New password"}
        form.fields["new_password2"].widget.attrs = {
            "placeholder": "New password confirm"
        }
        return form


class ProfileView(DetailView):

    model = models.User
    template_name = "users/profile.html"
