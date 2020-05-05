from django.db import models
import datetime

# Create your models here.


class Lesson(models.Model):
    name = models.CharField(max_length=200)
    file_question = models.FileField(upload_to='question', null=True)
    file_answers = models.FileField(upload_to='answers', null=True)

    def __str__(self):
        return self.name


class Feedback(models.Model):
    username = models.CharField(max_length=60, blank=False, null=False)
    email = models.EmailField(blank=False, null=False)
    text = models.TextField(blank=False, null=False)
    pub_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.username)
