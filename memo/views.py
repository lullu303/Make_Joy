from django.shortcuts import render

# Create your views here.
def memo_view(request):

        return render(request, 'memo/diarymemo.html')