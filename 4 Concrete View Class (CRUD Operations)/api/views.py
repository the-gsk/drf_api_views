# Generic API_View and Model Mixin
from .models import Student, Product
from .serializers import StudentSerializer, ProductSerialzer
from rest_framework.generics import ListAPIView, CreateAPIView, RetrieveAPIView, UpdateAPIView, DestroyAPIView
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
# Create your views here.

# list(get) method -- pk not required
class StudentList(ListAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

# retrive(get) method -- pk required
class StudentRetrive(RetrieveAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
   
# create(post) method -- pk not required
class StudentCreate(CreateAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

# update(put) method -- pk required
class StudentUpdate(UpdateAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

# destroy(delet) method -- pk required
class StudentDestroy(DestroyAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer


# retrive(get) & create(post)  method -- pk not required
class Product_list_create(ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerialzer
    
# retrive(get), update(put) & destroy(delet) method -- pk required
class Product_retrive_update_destroy(RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerialzer      