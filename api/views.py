
from rest_framework import viewsets
from .models import Student, Program
from .serializers import StudentSerializer, ProgramSerializer

class StudentViewSet(viewsets.ModelViewSet):
    queryset=Student.objects.all()
    serializer_class=StudentSerializer

class ProgramViewSet(viewsets.ModelViewSet):
    queryset=Program.objects.all()
    serializer_class=ProgramSerializer