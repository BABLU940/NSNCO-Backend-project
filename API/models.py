from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token

# Create your models here.
class Artist(models.Model):
    Name=models.CharField(max_length=50,null=False,blank=False)
    User=models.ForeignKey(User,null=False,blank=False,on_delete=models.CASCADE)
    def __str__(self):
        return self.Name
    
class Work(models.Model):
    Work=models.ManyToManyField(User,null=True,blank=True)
    #Link=
    #Work_Type=

@receiver(sender=User,signal=post_save)
def after_save_user(sender,instance,created,**kwargs):
    if created:
        instance.is_staff=True
        instance.save()
        pd=Artist()
        pd.user=instance
        pd.save()
        t=Token()
        t.user=instance
        t.save()



