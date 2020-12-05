from django.shortcuts import render
import requests
import sys
from subprocess import run,PIPE
def button(request):

    return render(request,'home2.html')

def output(request):
    data=requests.get("https://reqres.in/api/users")
    print(data.text)
    data=data.text
    return render(request,'home2.html',{'data':data})

def external(request):
    inp= request.POST.get('param')
    out= run([sys.executable,'//vscode//django_testing//test.py',inp],shell=False,stdout=PIPE)
    print(out)

    return render(request,'home2.html',{'data1':out})