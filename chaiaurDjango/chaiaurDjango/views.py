from django.http import HttpResponse
from django.shortcuts import render

def home(request):
    # return HttpResponse("Hello mister, you are at home page.")
    return render(request, 'website/index.html')

def about(request):
    return HttpResponse("Hello mister, welcome to about page.")

def contact(request):
    return HttpResponse("Hello mister, you can contact us on this page.")

