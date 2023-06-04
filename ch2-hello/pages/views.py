from django.shortcuts import render
from django.http import HttpResponse


def home_page_view(req):
    return HttpResponse("Hello, World!")
