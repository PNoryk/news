from django.db import models

# Create your models here.


class Topic(models.Model):
    title = models.CharField("Наименование", max_length=255)


class TopicImage(models.Model):
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE)
    image = models.ImageField("Картинка")
