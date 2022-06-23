from django.shortcuts import render, redirect
from .forms import TableForm
from .models import Table
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