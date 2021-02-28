from django.urls import path, include
from rest_framework import routers

from . import views

router = routers.DefaultRouter()
router.register("menu", views.MenuViewSet, basename="menu")
router.register("dishes", views.DishesViewSet, basename="dishes")


urlpatterns = [
    path("", include(router.urls)),
    path("profile/", views.ProfileRetrieveView.as_view(), name="profile"),
    
]
