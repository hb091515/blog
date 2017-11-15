from django.shortcuts import render
import datetime
from django.core.paginator import Page

def main(request):
    '''
    Render the main page
    '''
    context={'like':'Django 很棒'}
    context.update({'now':datetime.datetime.now()})
    return render(request, 'main/main.html', context)

def about(request):
    '''
    Render the about Page
    '''
    return render(request, 'main/about.html')