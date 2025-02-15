from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Expenses(models.Model):
 CATEGORY_CHOICES = [
    ('Food', 'Food'),
    ('Travel', 'Travel'),
    ('Bills', 'Bills'),
    ('Shopping', 'Shopping'),
    ('Misc', 'Misc'),
]

 user = models.ForeignKey(User, on_delete= models.CASCADE)
 category = models.CharField(max_length= 100, choices =CATEGORY_CHOICES)
 amount = models.DecimalField(max_digits=10, decimal_places=2)
 date = models.DateField()
 description = models.TextField(null= True, blank=True)
 
 def __str__(self):
  return f'{self.category} {self.amount}'