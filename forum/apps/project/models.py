from django.db import models
from uuid import uuid4
from django.contrib.auth.models import User


class QuestionModel(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    user_id = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='questions')
    title = models.CharField(max_length=100)
    content = models.CharField(max_length=200)
    description = models.TextField()
    question_date = models.DateTimeField(auto_now_add=True)

class ProfilModel(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    profil_id = models.OneToOneField(User, on_delete = models.CASCADE)
    profil_image = models.ImageField(upload_to='profil_images/')
    profil_date = models.DateTimeField(auto_now_add=True)

class ResponseModel(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    user_id = models.ForeignKey(User, on_delete = models.CASCADE)
    response_id = models.ForeignKey(QuestionModel, on_delete = models.CASCADE)
    response = models.TextField()
    date_response = models.DateTimeField(auto_now_add = True)

class LikeModel(models.Model):
    id = models.UUIDField(primary_key = True, default = uuid4, editable = False)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    question_id = models.ForeignKey(QuestionModel, on_delete=models.SET_NULL, null=True)
    like = models.IntegerField(default = 0)


class Student(models.Model):
    class YearInSchool(models.TextChoices):
        FRESHMAN = 'FR'
        SOPHOORE = 'SP'
    
    class CarNumber(models.IntegerChoices):
        BENZ = 1
        TESLA = 2

    study = models.CharField(choices=YearInSchool.choices, max_length=50)
    CAR = models.CharField(max_length=20, choices=CarNumber.choices)


