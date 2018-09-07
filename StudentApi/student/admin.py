from django.contrib import admin
from student.models import Student
# Register your models here.

class StudentModel(admin.ModelAdmin):
    class Meta:
        model = Student

admin.site.register(Student, StudentModel)