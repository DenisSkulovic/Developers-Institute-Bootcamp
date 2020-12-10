from django.db import models

class Family(models.Model):
    name = models.CharField(max_length=100)
        
    def __repr__(self):
        return self.name
    
class Animal(models.Model):
    legs = models.IntegerField()
    name = models.CharField(max_length=100)
    weight = models.FloatField()
    height = models.FloatField()
    speed = models.FloatField()
    family = models.ForeignKey(Family, on_delete=models.CASCADE)
    
    def __repr__(self):
        return self.name
    
    
