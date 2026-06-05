from rest_framework import serializers
from .models import Student, Program

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = '__all__'

class ProgramSerializer(serializers.ModelSerializer):
    class Meta:
        model = Program
        fields = '__all__'