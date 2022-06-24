from django.shortcuts import render, redirect, get_object_or_404
from .forms import TableForm, ClassForm, ReviewForm
from .models import Table, Class, Review

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


# 특정 과목 강의평 출력
def classreview(request,class_id):
    review_detail = get_object_or_404(Class,pk=class_id)
    class_detail = get_object_or_404(Class,pk=class_id)
    review_form = ReviewForm()
    return render(request, 'ReviewDetail.html',{'review_detail':review_detail,'review_form':review_form,'class_detail':class_detail})

# 강의평 추가

def new_review(request, class_id):
    filled_form = ReviewForm(request.POST)
    if filled_form.is_valid():
        finished_form = filled_form.save(commit=False)
        finished_form.post = get_object_or_404(Review,pk=class_id)
        finished_form.save()
    return redirect('reviewdetail', class_id)