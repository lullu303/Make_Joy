from django.shortcuts import render

# Create your views here.
def password_reset(request):
    return render(request, 'password/password_reset.html')