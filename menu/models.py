from django.db import models
from django.conf import settings
from datetime import datetime
from django.db.models import Sum


# Create your models here.


class DateDescriptionMixin(models.Model):
    description = models.CharField(max_length=150)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.PROTECT)
    date_added = models.DateTimeField(auto_now_add=True,)
    date_uploaded = models.DateTimeField(auto_now=True,)
    image_url = models.URLField(default="")
  

    class Meta:
        abstract = True

    def __str__(self):
        return self.name


class Dishes(DateDescriptionMixin, models.Model):
    name = models.CharField(max_length=50) 
    # description = models.CharField(max_length=150)
    # user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.PROTECT())
    price = models.PositiveIntegerField()
    # date_added = models.DateTimeField(auto_now=True, default= "")
    # date_uploaded = models.DateTimeField(auto_now_add=True, default="")
    VEGETARIAN_CHOICES = [
    
        ("yes", "Yes"),
        ("no", "No"),
    ]
    vegetarian_food = models.CharField(
        max_length=10,
        choices=VEGETARIAN_CHOICES
    )
    
class Menu(DateDescriptionMixin, models.Model):
    name = models.CharField(max_length=50, unique=True,) 
    slug = models.SlugField(unique=True),
    # description = models.CharField(max_length=150)
    # user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.PROTECT())
    # date_added = models.DateTimeField(auto_now=True, default= "")
    # date_uploaded = models.DateTimeField(auto_now_add=True, default="")
    # image_url = models.URLField(default="")
    dishes = models.ManyToManyField(Dishes)


  

