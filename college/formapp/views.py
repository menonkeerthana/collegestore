from django.shortcuts import render, redirect
from .forms import RegisterForm
from .models import Courses
# Create your views here.
def create_view(request):
    form = RegisterForm()

    if request.method=='POST':
        form=RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('store:submit')
    return render(request,'registerform.html',{'form':form})

def load_courses(request):
    department_id = request.GET.get('department_id')
    courses = Courses.objects.filter(department_id=department_id)
    return render(request,'courses_dropdown.html',{'courses':courses})