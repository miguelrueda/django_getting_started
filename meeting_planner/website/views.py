from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime

def welcome(request):
    return HttpResponse("Welcome to the Meeting Planner!")

def date(request):
    return HttpResponse(f"This page was served at {str(datetime.now())}")

def about(request):
    return HttpResponse(f"This is some generated content for the about view")