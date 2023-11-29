from django.shortcuts import render
from .models import Employee

def details(request):
    if request.method=='POST':
        name = request.POST.get('name')
        number = request.POST.get('num')
        age = request.POST.get('age')

        record = Employee.objects.create(name=name,number=number,age=age)
        record.save()
    return render(request,'details.html')
