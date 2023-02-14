from django.db import models

class Userdata(models.Model):
    user_id = models.AutoField(primary_key=True)
    email = models.EmailField(max_length=255,unique=True)
    username = models.CharField(max_length=255, unique=True)
    password = models.CharField(max_length=255)
    profile_picture = models.CharField(max_length=255, blank=True, null=True)
    bio = models.TextField(blank=True, null=True)
    location = models.CharField(max_length=255, blank=True, null=True)
    # last_login = models.DateTimeField(auto_now=True)
    # is_authorized = models.BooleanField(default=False)
    # is_banned = models.BooleanField(default=False)
    # is_superuser =  models.BooleanField(default=False)

    class Meta:
        managed = False
        db_table = 'userdata'