from django.contrib import admin
from .models import Student, Product
# Register your models here.
@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ('id','name','age','address')

@admin.register(Product)    
class ProductAdmin(admin.ModelAdmin):
    list_display = ('id','name','price','brand')