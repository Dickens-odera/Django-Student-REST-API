from django.conf.urls import url
from django.urls import path, include
from . import views
urlpatterns = [
    url(r'^$', views.StudentFormHelper, name = 'index'),
    path(r'^update/<int:id>$', views.updateStudent, name = 'update'),
    
]