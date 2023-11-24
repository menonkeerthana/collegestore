from django.db import models

# Create your models here.
class Departments(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Courses(models.Model):
    name = models.CharField(max_length=250)
    department= models.ForeignKey(Departments, on_delete=models.CASCADE)


    def __str__(self):
        return self.name
class Registeration(models.Model):
    name=models.CharField(max_length=250)
    dob = models.DateField()
    age=models.IntegerField()
    gender=models.CharField(max_length=150,choices = [('M','Male'),('F','Female')])
    phone=models.CharField(max_length=10)
    email=models.CharField(max_length=250)
    address=models.TextField()
    department=models.ForeignKey(Departments,on_delete=models.CASCADE)
    course=models.ForeignKey(Courses,on_delete=models.CASCADE)
    purpose=models.CharField(max_length=3,choices=(('R','Return'),('E','Exchange'),('O','Place Order')))
    materials=models.BooleanField(max_length=150,blank = True)
