from django.shortcuts import render

def home(request):
    render(request, 'halls/home.html')
