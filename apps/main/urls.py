from django.conf.urls import include, url
from rest_framework import routers
from .views import EventViewSet

router = routers.DefaultRouter()
router.register(r'eventos', EventViewSet)

urlpatterns = [
    url(r'^', include(router.urls)),
]
