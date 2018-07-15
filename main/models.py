from django.db import models
from django.contrib.auth.models import User

class UserProfile(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField()
    
    def __str__(self):
        return "{}: {} {}".format(
            self.user.username,
            self.first_name,
            self.last_name)
    
class SignUpAttempt(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField()
    username = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    verification_code = models.CharField(max_length=100)
    verification_code_email_sent = models.BooleanField()
    
class ForumPost(models.Model):
    title = models.CharField(max_length=100)
    user_profile = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    content = models.TextField(max_length=10000)
    

# Create your models here.
