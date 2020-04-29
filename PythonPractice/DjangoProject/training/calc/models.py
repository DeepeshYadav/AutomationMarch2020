from django.db import models

# Create your models here.

class Destination:
    name : str
    dec  : str
    price : int
    img   : str
    offer  : bool
