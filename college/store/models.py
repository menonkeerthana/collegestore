from django.db import models

# Create your models here.
class Item(models.Model):
    name=models.CharField(max_length=250,unique=True)
    desc=models.TextField()
    img=models.ImageField(upload_to='pics')
    price=models.DecimalField(max_digits=5,decimal_places=2)
    stock=models.IntegerField()
    created=models.DateTimeField(auto_now_add=True)
    updated=models.DateTimeField(auto_now=True)

    class Meta:
        db_table='Items'
        ordering=['created']

    def __str__(self):
        return self.name


