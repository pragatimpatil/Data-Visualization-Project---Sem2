from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

#def tasks(request):
    #return HttpResponse("Hello world!")

from django.template import loader
'''
def tasks(request):
  template = loader.get_template('myfirst.html')
  return HttpResponse(template.render())
'''
from .models import task

def tasks(request):
  mytasks = task.objects.all().values()
  template = loader.get_template('all_tasks.html')
  context = {
    'mytasks': mytasks,
  }
  return HttpResponse(template.render(context, request))

def details1(request, id):
  mytask = task.objects.get(id=id)
  template = loader.get_template('details1.html')
  context = {
    'mytask': mytask,
  }
  return HttpResponse(template.render(context, request))

def details2(request, id):
  mytask = task.objects.get(id=id)
  template = loader.get_template('details2.html')
  context = {
    'mytask': mytask,
  }
  return HttpResponse(template.render(context, request))

def details3(request, id):
  mytask = task.objects.get(id=id)
  template = loader.get_template('details3.html')
  context = {
    'mytask': mytask,
  }
  return HttpResponse(template.render(context, request))

def details4(request, id):
  mytask = task.objects.get(id=id)
  template = loader.get_template('details4.html')
  context = {
    'mytask': mytask,
  }
  return HttpResponse(template.render(context, request))