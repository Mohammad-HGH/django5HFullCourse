from django.shortcuts import render

# Create your views here.
from django.shortcuts import render


# Create your views here.

def profiles(request):
    return render(request, 'users/profiles.html')
