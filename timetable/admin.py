from django.contrib import admin
from .models import Semester, Table, Class, Review
# Register your models here.
admin.site.register(Semester)
admin.site.register(Table)
admin.site.register(Class)
admin.site.register(Review)