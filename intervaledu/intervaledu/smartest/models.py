from django.db import models

from web.models import CLASS_CHOICES


class Subject(models.Model):
    name = models.CharField(max_length=100)
    code = models.CharField(max_length=10)

    def __str__(self):
        return self.name


class TestLink(models.Model):
    name = models.CharField(max_length=100)
    board = models.ForeignKey("web.Board", on_delete=models.CASCADE)
    standard = models.CharField(max_length=10, choices=CLASS_CHOICES)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    link = models.URLField()

    def __str__(self):
        return f"{self.name} {self.board} {self.standard} {self.subject}"
