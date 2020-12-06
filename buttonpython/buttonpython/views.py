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
    # inp= request.POST.get('param')                     #Here          Added Kelter-1313             #Here
    # inp2= request.POST.get('param2')
    # out= run([sys.executable,'//Users//ebbyrd//Documents//vscode//django_testing//test.py',inp,inp2],shell=False,stdout=PIPE)
    # print(out)

    return render(request,'index.html',{'data1':out.stdout})
    
