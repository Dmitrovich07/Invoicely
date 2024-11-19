from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import TeamViesSet

router = DefaultRouter()
router.register("teams", TeamViesSet, basename="teams")

urlpatterns = [
  path('', include(router.urls))
]