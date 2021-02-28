from rest_framework import viewsets
from rest_framework.generics import RetrieveAPIView
from rest_framework.response import Response



from .models import (
    Menu,
    Dishes
)

from .serializers import (
    AdminMenuSerializer,
    MenuSerializer,
    AdminDishesSerializer,
    DishesSerializer,
    UserSerializer,
)
class AdminViewSetMixin:
    model = None
    admin_serializer_class = None
    user_serializer_class = None

    def get_queryset(self):
        if self.request.user.is_superuser:
            return self.model.objects.all()
        return self.model.objects.filter(user=self.request.user)

    def get_serializer_class(self):
        if self.request.user.is_superuser:
            return self.admin_serializer_class
        return self.user_serializer_class

    


class MenuViewSet(AdminViewSetMixin, viewsets.ModelViewSet):

    model = Menu
    admin_serializer_class = AdminMenuSerializer
    user_serializer_class = MenuSerializer
    

  
class DishesViewSet(AdminViewSetMixin, viewsets.ModelViewSet):
    
    model = Dishes
    admin_serializer_class = AdminDishesSerializer
    user_serializer_class = DishesSerializer


class ProfileRetrieveView(RetrieveAPIView):
    def retrieve(self, request, pk=None):
        serializer = UserSerializer(request.user)
        return Response(serializer.data)

    
