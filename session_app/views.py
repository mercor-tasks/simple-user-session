from django.http import JsonResponse
from django.shortcuts import render
from django.views import View

from utils.decorators import handle_exception
from utils.utils import sha256_string

from .models import SiteUser
from .session_manager import add_user_to_session, get_user_in_session


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
    @handle_exception
    def get(self, request):
        return render(
            request,
            'register.html',
        )

    @handle_exception
    def post(self, request):
        """
        DO NOT IMPLEMENT username unique check and email unique check!
        """

        data = request.POST

        name = data.get('name')
        username = data.get('username')
        email = data.get('email')
        password = data.get('password')

        password_hashed = sha256_string(password)

        user = SiteUser.objects.create(
            name=name,
            username=username,
            email=email,
            password=password_hashed,
        )

        return JsonResponse({
            "message": "ok",
        })


class LoginView(View):
    pass


class LogoutView(View):
    pass
