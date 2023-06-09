from django.db import models

# Create your models here.

class Actor(models.Model):
    name = models.CharField(max_length=100)


    def __str__(self) -> str:
        return super().__str__(self.name)
    

    class Meta : 
        ordering = ('name',)



class Movie(models.Model):
    title = models.CharField(max_length=100)
    actors = models.ManyToManyField(Actor)
    year = models.ImageField()



    def __str__(self) -> str:
        return super().__str__(self.title)
    

    class Meta : 
        ordering = ('title',)
 