from django.http import HttpResponse
import os
from django.shortcuts import render
cutter_file=os.path.abspath(__file__)
print(cutter_file)
project_file=os.path.dirname(os.path.dirname(cutter_file))


 

def page1(request):
    return HttpResponse("<h1>hiii abc </h1>")

def page2(request):
    return render(request,"smail.html")


def page3(request):
    tem=os.path.join(project_file,"templates","sam.html")
    temp1=open(tem,'r')
    temp2=temp1.read()
    return HttpResponse(temp2)


