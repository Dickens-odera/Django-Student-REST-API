from django.contrib import admin
from django.urls import path, include
from django.conf.urls import url
from student.views import ListStudent, RetrieveStudent
urlpatterns = [
    path('admin/', admin.site.urls),
    path('students/',ListStudent.as_view(), name = 'list_students'),
    #path(r'^studentslist/(?P<pk>[0-9]+)/$',RetrieveStudent.as_view(), name ='student'),
    path(r'^students/(P<pk>\d+)/$',RetrieveStudent.as_view(), name = 'student'),
    url('listStudent/', include('student.urls'), name='list_student'),
    url(r'^api-auth/', include('rest_framework.urls'))
]