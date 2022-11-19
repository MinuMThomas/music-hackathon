from django.db import models


# Create your models here.
class Question(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField()
    audio_file = models.FileField(upload_to='media_audio/')
    description = models.TextField(max_length=550)
    clue1 = models.CharField(max_length=200)
    clue2 = models.CharField(max_length=200)
    clue3 = models.CharField(max_length=200)
    clue4 = models.CharField(max_length=200)
    answer_option1 = models.CharField(max_length=200)
    answer_option2 = models.CharField(max_length=200)
    answer_option3 = models.CharField(max_length=200)
    answer_option4 = models.CharField(max_length=200)
    answer = models.CharField(max_length=200)

    def __str__(self):
        return self.name
