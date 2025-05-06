from datetime import datetime
from django.core.paginator import Paginator
from django.db.models import Count,Q
from django.urls import reverse
from django.shortcuts import get_object_or_404, redirect, render

def home(request):
    return render(request, 'home.html')