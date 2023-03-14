from django.shortcuts import render

# Create your views here.
def calendar1_view(request):

        return render(request, 'calendar1/calendar1.html')