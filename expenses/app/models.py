from django.db import models
from django.contrib.auth.models import User


class Expense(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    description = models.TextField()
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    date = models.DateField()
    
    def __str__(self) -> str:
        return f"{self.user} {self.title} {self.date}"
    

    
