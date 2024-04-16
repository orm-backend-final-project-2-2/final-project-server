from django.urls import path, include
from rest_framework.routers import DefaultRouter
from exercises_info.views import ExercisesInfoViewSet

router = DefaultRouter()
router.register(r"exercises-info", ExercisesInfoViewSet, basename="exercises-info")

urlpatterns = [
    path("", include(router.urls)),
]
