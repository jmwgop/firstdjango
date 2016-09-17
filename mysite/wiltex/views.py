from django.shortcuts import render

def index(request):
    return render(request, 'docpull/home.html')

def upload(request):
    return render(request, 'docpull/upload.html')
