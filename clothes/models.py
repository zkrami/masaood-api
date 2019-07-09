from django.db import models
from enum import Enum
# Create your models here.


class SizeEnum(Enum):
    Large = 'large'
    Xlarge = 'xlarge'
    Small = 'small'
    Medium = 'medium'


class Cloth(models.Model):
    size = models.IntegerField(default=0, blank=True, null=True)
    create_date = models.DateTimeField(auto_now=True)
    name = models.CharField(max_length=200)
    
    def __str__(self):
        return self.name
