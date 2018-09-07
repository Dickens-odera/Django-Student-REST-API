from student.models import Student
from rest_framework import serializers
class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        #fields = ('surname', 'middle_name','last_nme','id_number','email','school','department', 'reg_number')
        fields = '__all__'
        #user = serializers.ReadOnlyField(source='user.username')