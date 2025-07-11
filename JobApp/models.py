from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class StudentUser(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    mobile = models.CharField(max_length=20, null=True)
    image = models.FileField(null=True)
    gender = models.CharField(max_length=10,null=True)
    type = models.CharField(max_length=50,null=True)


    def __str__(self):
        return self.user.username
    
class Recruiter(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    company = models.CharField(max_length=100,null=True)
    mobile = models.CharField(max_length=20, null=True)
    image = models.FileField()
    gender = models.CharField(max_length=10,null=True)
    type = models.CharField(max_length=50,null=True)
    status = models.CharField(max_length=50,null=True)


    def __str__(self):
        return self.user.username

class Job(models.Model):
    recruiter = models.ForeignKey(Recruiter, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    start_date = models.DateField(max_length=100)
    end_date = models.DateField(max_length=100)
    salary = models.CharField(max_length=100)
    company_logo = models.FileField(null=True)
    description = models.CharField(max_length=500)
    experience = models.CharField(max_length=500)
    location = models.CharField(max_length=500)
    skills = models.CharField(max_length=500)
    creation_date = models.DateField()

    def __str__(self):
        return self.title
    
class Apply(models.Model):
    job = models.ForeignKey(Job, on_delete=models.CASCADE)
    student = models.ForeignKey(StudentUser, on_delete=models.CASCADE)
    resume = models.FileField(null=True)
    apply_date = models.DateField(null=True)

    def __str__(self):
        return f"{self.student.user.first_name} {self.student.user.last_name}"
    