from django.db import models
from django.conf import settings

# Create your models here.


class DateDescriptionMixin(models.Model):
    description = models.CharField(max_length=150)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.PROTECT)
    date_added = models.DateTimeField(auto_now=True, )
    date_uploaded = models.DateTimeField(auto_now_add=True,)
    image_url = models.URLField(default="")

    class Meta:
        abstract = True

    def __str__(self):
        return self.name


class Menu(DateDescriptionMixin, models.Model):
    name = models.CharField(max_length=50, unique=True,) 
    # description = models.CharField(max_length=150)
    # user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.PROTECT())
    # date_added = models.DateTimeField(auto_now=True, default= "")
    # date_uploaded = models.DateTimeField(auto_now_add=True, default="")
    # image_url = models.URLField(default="")


class Dishes(DateDescriptionMixin, models.Model):
    name = models.CharField(max_length=50) 
    # description = models.CharField(max_length=150)
    # user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.PROTECT())
    menu = models.ForeignKey(Menu, on_delete=models.PROTECT)
    price = models.PositiveIntegerField()
    # date_added = models.DateTimeField(auto_now=True, default= "")
    # date_uploaded = models.DateTimeField(auto_now_add=True, default="")
    VEGETARIAN = [
        ("yes", "Yes"),
        ("no", "No")
    ]
    vegetarian_food = models.BooleanField(
        default=False,
        blank=True,
        null=False,
        verbose_name="vege?"
    )


