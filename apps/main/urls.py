from django.conf.urls import include, url
from rest_framework import routers
from .views import EventViewSet, IndexView

router = routers.DefaultRouter()
router.register(r'eventos', EventViewSet)

urlpatterns = [
    url(r'^api/', include(router.urls)),
    url(r'^$', IndexView.as_view()),
]
