from rest_framework import serializers
from . models import Student, Product

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = '__all__'


class ProductSerialzer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'