from django.db import models

# Create your models here.

class Aadhar(models.Model):
    aadhar = models.IntegerField()
    def __str__(self):
        return str(self.aadhar)

class Student(models.Model):
    stu_name = models.CharField(max_length=50)
    stu_email = models.EmailField()
    stu_contact = models.IntegerField()
    aadhar = models.OneToOneField(Aadhar,on_delete=models.CASCADE)
    def __str__(self):
        return self.stu_name

