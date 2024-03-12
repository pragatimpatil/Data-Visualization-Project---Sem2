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
from .models import voption
from .models import module
def tasks(request):
  mytasks = task.objects.all().values()
  myvoptions = voption.objects.all().values()
  mymodules = module.objects.all().values()
  template = loader.get_template('all_tasks.html')
  context = {
    'mytasks': mytasks,
    'myvoptions':myvoptions,
    'mymodules':mymodules,
  }
  return HttpResponse(template.render(context, request))

def knn(request, id):
  mymodule = module.objects.get(id=id)
  template = loader.get_template('knn.html')
  context = {
    'mymodule': mymodule,
  }
  return HttpResponse(template.render(context, request))

def ift(request, id):
  mymodule = module.objects.get(id=id)
  template = loader.get_template('ift.html')
  context = {
    'mymodule': mymodule,
  }
  return HttpResponse(template.render(context, request))

def gmm(request, id):
  mymodule = module.objects.get(id=id)
  template = loader.get_template('gmm.html')
  context = {
    'mymodule': mymodule,
  }
  return HttpResponse(template.render(context, request))

def kms(request, id):
  mymodule = module.objects.get(id=id)
  template = loader.get_template('kms.html')
  context = {
    'mymodule': mymodule,
  }
  return HttpResponse(template.render(context, request))

def lr(request, id):
  mymodule = module.objects.get(id=id)
  template = loader.get_template('lr.html')
  context = {
    'mymodule': mymodule,
  }
  return HttpResponse(template.render(context, request))

def details1(request, id):
  mytask = task.objects.get(id=id)
  template = loader.get_template('details1.html')
  context = {
    'mytask': mytask,
  }
  return HttpResponse(template.render(context, request))

def dot(request, id):
  myvoption = voption.objects.get(id=id)
  template = loader.get_template('dot.html')
  context = {
    'myvoption': myvoption,
  }
  return HttpResponse(template.render(context, request))

def line(request, id):
  myvoption = voption.objects.get(id=id)
  template = loader.get_template('line.html')
  context = {
    'myvoption': myvoption,
  }
  return HttpResponse(template.render(context, request))

def scatter(request, id):
  myvoption = voption.objects.get(id=id)
  template = loader.get_template('scatter.html')
  context = {
    'myvoption': myvoption,
  }
  return HttpResponse(template.render(context, request))

def boxplot(request, id):
  myvoption = voption.objects.get(id=id)
  template = loader.get_template('boxplot.html')
  context = {
    'myvoption': myvoption,
  }
  return HttpResponse(template.render(context, request))

def bar(request, id):
  myvoption = voption.objects.get(id=id)
  template = loader.get_template('bar.html')
  context = {
    'myvoption': myvoption,
  }
  return HttpResponse(template.render(context, request))

def qq(request, id):
  myvoption = voption.objects.get(id=id)
  template = loader.get_template('qq.html')
  context = {
    'myvoption': myvoption,
  }
  return HttpResponse(template.render(context, request))

def histogram(request, id):
  myvoption = voption.objects.get(id=id)
  template = loader.get_template('histogram.html')
  context = {
    'myvoption': myvoption,
  }
  return HttpResponse(template.render(context, request))

def dendogram(request, id):
  myvoption = voption.objects.get(id=id)
  template = loader.get_template('dendogram.html')
  context = {
    'myvoption': myvoption,
  }
  return HttpResponse(template.render(context, request))

def pie(request, id):
  myvoption = voption.objects.get(id=id)
  template = loader.get_template('pie.html')
  context = {
    'myvoption': myvoption,
  }
  return HttpResponse(template.render(context, request))

def heatmap(request, id):
  myvoption = voption.objects.get(id=id)
  template = loader.get_template('heatmap.html')
  context = {
    'myvoption': myvoption,
  }
  return HttpResponse(template.render(context, request))


def dv(request, id):
  myvoption = voption.objects.get(id=id)
  template = loader.get_template('dv.html')
  context = {
    'myvoption': myvoption,
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