from django.shortcuts import render,HttpResponse
from .models import Employee,Role,Department
from django.db.models import Q
from datetime import datetime

# Create your views here.
def index(request):
    return render(request,'index.html')

def all_emp(request):
    #How to view all the items in a model using django query set?
    #by using this command we can view 
    "User.Objects.all()"
    emps=Employee.objects.all() 
    context={
        'emps':emps
    }
    print(context)
    return render(request,'all_emp.html',context)

def add_emp(request):
    if request.method=='POST':
        First_name=request.POST["First_name"]
        last_name=request.POST["last_name"]
        salary=int(request.POST["salary"])
        dept=int(request.POST["dept"])
        bonus=int(request.POST["bonus"])
        phone=int(request.POST['phone'])
        role=int(request.POST['role'])
        new_emp=Employee(first_name=First_name,last_name=last_name,salary=salary,dept_id=dept,bonus=bonus,phone=phone,role_id=role,hire_date=datetime.now())
        new_emp.save()
        return HttpResponse("Employee added successfully")
    elif request.method=="GET":
            return render(request,'add_emp.html')
    else:
        return HttpResponse("An Exception Occured! Employee has not been added")
def remove_emp(request,emp_id=0):
    if emp_id:
        try:
            emp_to_be_removed=Employee.objects.get(id=emp_id)
            emp_to_be_removed.delete()
            return HttpResponse("Employee Removed Successfully")

        except:
            return HttpResponse("Please Enter a Valid Employee id")
    emps=Employee.objects.all()
    context={
        'emps':emps
    }
    return render(request,'remove_emp.html',context)

def filter_emp(request):
    if request.method=="POST":
        name=request.POST['name']
        dept=request.POST['dept']
        role=request.POST['role']
        emps=Employee.objects.all()

        if name:
            emps=emps.filter(Q(first_name__icontains=name) | Q(last_name__icontains=name))
        
        if dept:
            emps=emps.filter(dept__name__icontains=dept)
        if role:
            emps=emps.filter(role__name__icontains=role)

        context={
            "emps":emps
        }
        return render(request,"all_emp.html",context)
    elif request.method=="GET":
        return render(request,'filter_emp.html')

    else:
        return HttpResponse("An Exception occured")