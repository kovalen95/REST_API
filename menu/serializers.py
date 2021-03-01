from rest_framework import serializers
from django.conf import settings
from django.contrib.auth import get_user_model


from.models import(
    Menu,
    Dishes
)

class UserMixin(serializers.Serializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())


class AdminMenuSerializer(serializers.ModelSerializer):
    class Meta:
        model = Menu
        fields = [
            "id",
            "name",
            # "slug",
            "description",
            "user",
            "image_url",
            "date_added", 
            "date_uploaded",
            "url",
            "dishes",
        ]


class MenuSerializer(UserMixin, AdminMenuSerializer):
    pass


class AdminDishesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Dishes
        fields =[
            "id",
            "name",
            "description",
            "user",
            "price",
            "image_url",
            "date_added",
            "date_uploaded",
            "vegetarian_food",
            "url",
        ]

class DishesSerializer(UserMixin, AdminDishesSerializer):
    pass
    

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = [
            "id",
            "username",
            "email",
            "first_name",
            "last_name",
        ]
