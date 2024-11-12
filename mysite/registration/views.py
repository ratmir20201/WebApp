from django.contrib.auth import authenticate, login
from django.contrib.auth.views import LogoutView
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, TemplateView

from .forms import CustomUserCreationForm
from .models import Profile


class UserRoomView(TemplateView):
    template_name = "registration/user_room.html"


class RegisterView(CreateView):
    form_class = CustomUserCreationForm
    template_name = "registration/register.html"
    success_url = reverse_lazy("registration:user_room")

    def form_valid(self, form):
        response = super().form_valid(form)

        username = form.cleaned_data.get("username")
        email = form.cleaned_data.get("email")
        phone_number = form.cleaned_data.get("phone_number")
        password = form.cleaned_data.get("password1")
        Profile.objects.create(
            user=self.object,
            email=email,
            phone_number=phone_number,
        )

        user = authenticate(self.request, username=username, password=password)
        print("Пользователь создан")
        if user is not None:
            login(self.request, user)
            print("Зашли в личный кабинет")

        return response
