from django.shortcuts import render
import requests
import sys
from subprocess import run,PIPE
def button(request):

    return render(request,'index.html')

def output(request):
    data=requests.get("https://reqres.in/api/users")
    print(data.text)
    data=data.text
    return render(request,'index.html',{'data':data})

def external(request):
    inp= request.POST.get('param')
    inp2= request.POST.get('param2')  # //Users//kelter//Documents//GitHub//Study-Buddy-Dashboard//django_testing//test.py
    out= run([sys.executable,'/Users/kelter/Documents/GitHub/Study-Buddy-Dashboard/django_testing/test.py',inp,inp2],shell=False,stdout=PIPE)
    return render(request,'index.html',{'data1':out.stdout})


def tips(request):
    # inp= request.POST.get('param3')
    # inp2= request.POST.get('param4')
    out= run([sys.executable,'/Users/kelter/Documents/GitHub/Study-Buddy-Dashboard/django_testing/test2.py'],shell=False,stdout=PIPE)
    print(out)

    return render(request,'index.html',{'data2':out.stdout})
    
