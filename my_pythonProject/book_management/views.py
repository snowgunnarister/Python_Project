from django.shortcuts import render
from book_management.models import Category, Book
# from django.http import HttpResponse
# from django.template import loader
# Create your views here.
def index(request):
    
    
    # header_str = 'Hello, Python variable'
    # context = {
    #    'var1' : header_str
    # }
    return render(request, 'index.html', context)
