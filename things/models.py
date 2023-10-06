from django.db import models

# Create your models here.
class thing(Model):
    name = CharField(MaxLength = 30)
    description = CharField(MaxLength = 120)
    quantity = IntegerField()
