from django.db import models
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    USER=[
        ('admin','Admin'),
        ('viewer','Viewer')
    ]
    usertype=models.CharField(choices=USER,null=True,max_length=100)

    def __str__(self):
        return f"{self.username}-{self.first_name}-{self.last_name}"
    
class ResumeModel(models.Model):
    Gender=[
        ('male','Male'),
        ('female','Female'),
        ('other','Other'),
    ]

    user=models.OneToOneField(CustomUser,null=True,on_delete=models.CASCADE)
    Designation=models.CharField(max_length=100,null=True)
    Contact_number=models.CharField(max_length=100,null=True)
    Career_Summary=models.TextField(max_length=100,null=True)
    Experience_Title=models.CharField(max_length=100,null=True)
    Skill_title=models.CharField(max_length=100,null=True)
    Education_Title=models.CharField(max_length=100,null=True)
    Language=models.CharField(max_length=100,null=True)
    Interest=models.CharField(max_length=100,null=True)
    Profile_Pic=models.ImageField(upload_to='Media/Profile_Pic',null=True)
    Linkedin_URL=models.URLField(max_length=100,null=True)
    Facebook_URL=models.URLField(max_length=100,null=True)
    Instagram_URL=models.URLField(max_length=100,null=True)
    GitHub_URL=models.URLField(max_length=100,null=True)

    gender=models.CharField(choices=Gender,max_length=100,null=True)

    def __str__(self):
        return f"Designation:{self.Designation} and username:{self.user.username}"
    
class Education_model(models.Model):
    user=models.ForeignKey(CustomUser,null=True,on_delete=models.CASCADE)
    title=models.CharField(max_length=100,null=True)
    start_date=models.DateField(null=True)
    end_date=models.DateField(null=True)

class Experience_model(models.Model):
    user=models.ForeignKey(CustomUser,null=True,on_delete=models.CASCADE)
    title=models.CharField(max_length=100,null=True)
    start_date=models.DateField(null=True)
    end_date=models.DateField(null=True)
    

class Skill_model(models.Model):
    Profecency=[
        ('high','High'),
        ('medium','Medium'),
        ('low','Low'),
    ]

    user=models.ForeignKey(CustomUser,null=True,on_delete=models.CASCADE)
    skill_name=models.CharField(max_length=100,null=True)
    profecency_level=models.CharField(choices=Profecency,max_length=100,null=True)

class interest_model(models.Model):
    user=models.ForeignKey(CustomUser,null=True,on_delete=models.CASCADE)
    interest_name=models.CharField(max_length=100,null=True)

class language_model(models.Model):
    Profecency=[
        ('high','High'),
        ('medium','Medium'),
        ('low','Low'),
    ]
    
    user=models.ForeignKey(CustomUser,null=True,on_delete=models.CASCADE)
    language_name=models.CharField(max_length=100,null=True)
    profecency_level=models.CharField(choices=Profecency,max_length=100,null=True)


class intermidiate_skill_Model(models.Model):
    skill_name=models.CharField(max_length=100,null=True)
  
    def __str__(self):
        return f"{self.skill_name}"
    
class intermidiate_interest_model(models.Model):
    interest_name=models.CharField(max_length=100,null=True)
  
    def __str__(self):
        return f"{self.interest_name}"





    
