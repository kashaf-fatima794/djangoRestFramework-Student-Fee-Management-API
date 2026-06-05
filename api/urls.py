from django.urls import path,include
from rest_framework.routers import DefaultRouter
from .views import ProgramViewSet,StudentViewSet

router=DefaultRouter()
router.register(r'Programs',ProgramViewSet,basename='program')

router.register(r'Students',StudentViewSet,basename='student')

urlpatterns=[
    path('', include(router.urls)),
]
              