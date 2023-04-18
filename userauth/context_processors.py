from userauth.forms import UserRegisterForm
from django.contrib import messages


def register_view(request):
    return {
        'form': UserRegisterForm,
    }

