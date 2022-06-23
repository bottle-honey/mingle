from django.shortcuts import render, redirect
from .forms import TableForm, ClassForm
from .models import Table, Class

# 시간표 페이지 
def timetable(request):
    return render(request, 'timetable.html')

# 시간표 추가
def timetablecreate(request):
    if request.method=='POST':
        form = TableForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('timetable')
    else:
        form = TableForm()
    return render(request, 'TablePostForm.html',{'form':form})

# 과목 추가
def classcreate(request):
    if request.method=='POST':
        form = ClassForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('timetable')
    else:
        form = ClassForm()
    return render(request, 'ClassPostForm.html',{'form':form})

# 과목 리스트 추가
def classsearch(request):
    classes = Class.objects.filter().order_by('name')
    return render(request, 'ClassList.html', {'classes':classes})

# 과목 필터링

def classfiltering(attribute):
    pass