from django.shortcuts import render

# Create your views here.
from .forms import UserForm


def index(request):
    userform = UserForm()
    return render(request, "index.html", {"form": userform})