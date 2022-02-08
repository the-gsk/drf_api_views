from .models import Student
from .serializers import StudentSerializers
from rest_framework import viewsets 
# or you can import directly ModelViewset 
# from rest_framework.viewsets import ModelViewSet

# Create your views here.
class StudentReadonlyModelViewset(viewsets.ReadOnlyModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializers