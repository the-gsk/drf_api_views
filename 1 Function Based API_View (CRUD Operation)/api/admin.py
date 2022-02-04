from django.contrib import admin
from api.models import Student

# Register your models here.
@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ('id','name', 'age', 'address', 'created_at', 'updated_at')
    # list_display = ('__all__')