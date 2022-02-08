from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from api import views

# creating router object
router = DefaultRouter()

# register StudentModelViewsets with router
router.register('studentapi', views.StudentReadonlyModelViewset, basename='student')
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
]
