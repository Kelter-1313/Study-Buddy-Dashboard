from django.shortcuts import render
import requests
import sys
from subprocess import run,PIPE

def button(request):

    return render(request,'index.html')


def external(request):
    inp= request.POST.get('param')
    inp2= request.POST.get('param2')
    out= run([sys.executable,'/Users/kelter/Documents/GitHub/Study-Buddy-Dashboard/django_testing/test.py',inp,inp2],shell=False,stdout=PIPE)

    return render(request,'index.html',{'data1':out.stdout})


def tips(request):
    out= run([sys.executable,'/Users/kelter/Documents/GitHub/Study-Buddy-Dashboard/django_testing/test2.py'],shell=False,stdout=PIPE)
    print(out)

    return render(request,'index.html',{'data2':out.stdout})
    

def translator(request):
    inp= request.POST.get('param3')
    inp2= request.POST.get('param4')
    inp3= request.POST.get('param5')
    out= run([sys.executable,'/Users/kelter/Documents/GitHub/Study-Buddy-Dashboard/django_testing/test3.py',inp,inp2,inp3],shell=False,stdout=PIPE)

    return render(request,'index.html',{'data3':out.stdout})

def wikispeed(request):
    inp= request.POST.get('param6')
    out= run([sys.executable,'/Users/kelter/Documents/GitHub/Study-Buddy-Dashboard/django_testing/test4.py',inp],shell=False,stdout=PIPE)

    return render(request,'index.html',{'data4':out.stdout})