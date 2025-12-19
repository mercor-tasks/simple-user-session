from django.http import JsonResponse
from django.shortcuts import render
from django.views import View

from utils.decorators import handle_exception

from .session_manager import get_user_in_session


class HomeView(View):
    @handle_exception
    def get(self, request):
        user = get_user_in_session(request)
        user_name = user.name if user else ''
        return render(
            request,
            template_name="home.html",
            context={
                'user_name': user_name,
            }
        )


class RegisterView(View):
    pass


class LoginView(View):
    pass


class LogoutView(View):
    pass
