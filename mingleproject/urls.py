"""mingleproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from timetable import views as timetable_views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('timetable/', timetable_views.timetable, name='timetable'),
    path('timetablecreate/', timetable_views.timetablecreate, name='timetablecreate'),
    path('classcreate/', timetable_views.classcreate, name='classcreate'),
    path('classlist/', timetable_views.classsearch, name='classlist'),
    path('reviewdetail/<int:class_id>', timetable_views.classreview, name='reviewdetail')
]
