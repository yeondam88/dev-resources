from django.contrib import messages
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.contrib.auth.mixins import UserPassesTestMixin, LoginRequiredMixin


class LoggedOutOnlyView(UserPassesTestMixin):

    permission_denied_message = "Page not found"

    def test_func(self):
        return not self.request.user.is_authenticated

    def handle_no_permission(self):
        messages.error(self.request, "You already logged in")
        return redirect("core:home")


class LoggedInOnlyView(LoginRequiredMixin):

    login_url = reverse_lazy("users:login")
