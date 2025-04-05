from django.db import models
from django.conf import settings
from django.contrib.auth.models import User

class Country(models.Model):
    name = models.CharField(max_length=50)
    abbr = models.CharField(max_length=5)
    is_active = models.BooleanField(default=True)
    
    class Meta:
        verbose_name = 'Country'
        verbose_name_plural = 'Countries'
        db_table = 'Countries'


class Profile(models.Model):
    user = models.OneToOneField(to=settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    phone_number = models.BigIntegerField(blank=True, null=True, unique=True)
    country = models.ForeignKey(Country, on_delete=models.CASCADE)
    avatar = models.ImageField(blank=True)
    
    class Meta:
        verbose_name = 'Profile'
        verbose_name_plural = 'Profiles'
        db_table = 'Profiles'
    

class Device(models.Model):
    WEB = 1
    IOS = 2
    ANDROID = 3
    DEVICE_TYPE_CHOICES = (
        (WEB, 'web'),
        (IOS, 'ios'),
        (ANDROID, 'android'),
    )
    
    user =  models.ForeignKey(to=settings.AUTH_USER_MODEL, related_name='devices' ,on_delete=models.CASCADE)
    device_uuid = models.UUIDField('Device UUID', null=True)
    last_login = models.DateTimeField('Last login date', null=True)
    device_type = models.SmallIntegerField('Device type', choices=DEVICE_TYPE_CHOICES, default=WEB)
    app_version = models.CharField('App version', max_length=20, blank=True)
    
    class Meta:
        db_table = 'User devices'
        verbose_name = 'device'
        verbose_name_plural = 'devices'