from django.shortcuts import render


def weather_view(request):

        return render(request, 'weather/weather_api.html')