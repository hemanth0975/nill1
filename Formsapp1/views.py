from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import Student
from .forms import Student_details

# Create your views here.
def home(request):
    # if request.method == 'POST':
    #     f = Student_details(data = request.POST)
    #     if f.is_valid():
    #         name = f.cleaned_data['name']
    #         usn = f.cleaned_data['usn']
    #         mobile = f.cleaned_data['mobile']
    #         course = f.cleaned_data['course']
    #         Student.objects.create(name = name, usn = usn, mobile = mobile, course = course)
    #         return redirect('home')

    #     else:
    #         print("No data")
    # var = Student.objects.all().order_by('-id')
        
        # return HttpResponse("Something went wrong")

    if request.method == 'POST':
        form = Student_details(data = request.POST)
        if form.is_valid():
            form.save()
    var = Student.objects.all().order_by('-id')
    

    form = Student_details()
    context = {
        'title' : 'Home Page', 
        'forms' : form,        
        'var' : var,
    }
    return render(request, 'home.html', context)


def update(request, id):
    try:
        u = Student.objects.get(id = id)
    except:
        return HttpResponse("Data doesn't exists")
    if request.method == 'POST':
        d = Student_details(data=request.POST)
        d.is_valid()
        u.name = request.POST['name']
        u.usn = request.POST['usn']
        u.mobile = request.POST['mobile']
        u.course = request.POST['course']
        u.save()
        return redirect('home')
    form = Student_details(instance = u)              #instance is newly updated
    context = {
        'title' : 'Update Page',
        'forms' : form,
    }
    return render(request, 'home.html', context)



def delete(request, id):
    try:
        delete_form = Student.objects.get(id = id)
    except:
        return HttpResponse('Unable to delete')
    delete_form.delete()
    return redirect('home')