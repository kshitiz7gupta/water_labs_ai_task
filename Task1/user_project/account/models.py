from django.db import models
from django.contrib.auth.hashers import make_password
from django.dispatch import receiver
from django.db.models.signals import pre_save
# Create your models here.

class ModelBase(models.Model):
    """
    This is a abstract model class to add is_deleted, created_at and modified at fields in any model
    """
    is_deleted = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True

    def delete(self, *args, **kwargs):
        """ Soft delete """
        self.is_deleted = True
        self.save()


class User(ModelBase):
    """
    User model
    """
    username = models.CharField('username', max_length=200)
    password = models.CharField('password', max_length=200)
    email = models.CharField('email', max_length=200, default="", blank=True, null=True)

@receiver(pre_save, sender=User)
def hash_password(sender, instance, **kwargs):
    """
    hash password method
    """
    instance.password = make_password(instance.password)

