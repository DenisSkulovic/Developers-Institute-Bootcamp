from django.db import models



CATEGORY_CHOICES = (
    (1, 'SUPER URGENT'),
    (2, 'URGENT'),
    (3, 'SORTA URGENT'),
    (4, 'NOT URGENT'),
    (5, 'CHILL')
)


class Category(models.Model):
    
    name = models.CharField(max_length=100, unique=True, null=False, default='default')
    image = models.URLField()
    
    def __str__(self):
        return self.name
    
    def __repr__(self):
        return self.name

class Todo(models.Model):
    
    title = models.CharField(max_length=100)
    details = models.CharField(max_length=100)
    has_been_done = models.BooleanField(default=False)
    date_creation = models.DateTimeField(auto_now_add=True)
    date_completion = models.DateTimeField(auto_now=True)
    deadline_date = models.DateTimeField()
    category = models.ManyToManyField(to=Category)
    urgency = models.CharField(max_length=100, choices=CATEGORY_CHOICES, default=3)
    
    def __str__(self):
        return self.title
    
    def __repr__(self):
        return self.title
    

    
    
