from django.shortcuts import render, HttpResponse, redirect
from time import gmtime, strftime, timezone

def index(request):

  context = {
  "time": strftime("%b %d, %Y %I:%M %p", gmtime())
  }
  return render(request,'timeDisplay/index.html', context)
