from django import forms
from .models import Table, Class

class TableForm(forms.ModelForm):
    class Meta:
        model = Table
        fields = '__all__'
        
        def __init__(self, *args, **kwargs):
            super(TableForm, self).__init__(*args, **kwargs)
