from django.db import models

# Create your models here.
class VerificationToken(models.Model):
    key = models.CharField(max_length=255) # mobile or email 
    code = models.CharField(max_length=255) # verification code 
    createdAt = models.DateTimeField(auto_now_add=True) 

