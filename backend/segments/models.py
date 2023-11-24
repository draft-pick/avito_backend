from django.db import models
from django.utils.text import slugify
from datetime import datetime


class Users(models.Model):
    nickname = models.CharField(max_length=255)

    def __str__(self):
        return self.nickname


class SegmentsList(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField(unique=True)
    users = models.ManyToManyField(
        Users,
        through='SegmentsUser',
        related_name='segments',
    )

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title


class SegmentsUser(models.Model):
    user = models.ForeignKey(
        Users,
        on_delete=models.CASCADE,
    )
    segment = models.ForeignKey(
        SegmentsList,
        on_delete=models.CASCADE,
    )


class Actions(models.Model):
    user = models.ForeignKey(
        Users,
        on_delete=models.CASCADE,
        related_name='actions'
    )
    segment = models.ForeignKey(SegmentsList, on_delete=models.CASCADE)
    action = models.CharField(max_length=255)
    date_time = models.DateField(default=datetime.today)

    def __str__(self):
        return f'{self.user} - {self.action}: {self.date_time}'
