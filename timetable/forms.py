from django import forms
from .models import Review, Table, Class

class TableForm(forms.ModelForm):
    class Meta:
        model = Table
        fields = '__all__'
        
        def __init__(self, *args, **kwargs):
            super(TableForm, self).__init__(*args, **kwargs)

            self.fields['name'].widget.attrs = {
                'class' : 'form-control',
                'placeholder' : '이름을 입력하세요',
                'rows' : 3
            }
            
class ClassForm(forms.ModelForm):
    class Meta:
        model = Class
        fields = '__all__'
        
        def __init__(self, *args, **kwargs):
            super(ClassForm, self).__init__(*args, **kwargs)
            self.fields['major'].widget.attrs = {
                'class' : 'form-control',
                'placeholder' : '전공',
                'rows' : 3
            }
            self.fields['name'].widget.attrs = {
                'class' : 'form-control',
                'placeholder' : '학점',
                'rows' : 3
            }
            self.fields['name'].widget.attrs = {
                'class' : 'form-control',
                'placeholder' : '과목명',
                'rows' : 3
            }
            self.fields['professor'].widget.attrs = {
                'class' : 'form-control',
                'placeholder' : '교수',
                'rows' : 3
            }
            self.fields['day'].widget.attrs = {
                'class' : 'form-control',
                'placeholder' : '요일',
                'rows' : 3
            }
            self.fields['start_time'].widget.attrs = {
                'class' : 'form-control',
                'placeholder' : '시작 시간',
                'rows' : 3
            }
            self.fields['end_time'].widget.attrs = {
                'class' : 'form-control',
                'placeholder' : '종료 시간',
                'rows' : 3
            }
            self.fields['classroom'].widget.attrs = {
                'class' : 'form-control',
                'placeholder' : '강의실',
                'rows' : 3
            }
            self.fields['class_id'].widget.attrs = {
                    'class' : 'form-control',
                    'placeholder' : '학수번호',
                    'rows' : 3
            }
            
        

class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = '__all__'
        def __init__(self, *args, **kwargs):
            super(ReviewForm, self).__init__(*args, **kwargs)
            self.fields['body'].widget.attrs = {
                'class' : 'form-control',
                'placeholder' : 'Please write a general review of this lecture',
                'rows' : 3
            }
            
       
        