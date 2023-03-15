from django.core.paginator import Paginator
from django.shortcuts import render, get_object_or_404

# from index.models import Question


def index(request):
    return render(request, 'index/index.html')
