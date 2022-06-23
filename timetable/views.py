from django.shortcuts import render, redirect
from .forms import TableForm, ClassForm
from .models import Table, Class
# Create your views here.
def timetable(request):
    return render(request, 'timetable.html')

def timetablecreate(request):
    if request.method=='POST':
        form = TableForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('timetable')
    else:
        form = TableForm()
    return render(request, 'TablePostForm.html',{'form':form})

def classcreate(request):
    if request.method=='POST':
        form = ClassForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('timetable')
    else:
        form = ClassForm()
    return render(request, 'ClassPostForm.html',{'form':form})

def classsearch(request):
    classes = Class.objects.filter().order_by('name')
    return render(request, 'ClassList.html', {'classes':classes})

