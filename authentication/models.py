from django.db import models


from django.contrib.auth.models import User

# Create your models here.

class Profile(models.Model):

    university_name=models.CharField(max_length=50)
    course_name=models.CharField(max_length=50)
    user=models.ForeignKey(User,on_delete=models.CASCADE, null=True)