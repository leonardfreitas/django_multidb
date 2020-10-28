from django.db import models


class Note(models.Model):
    title = models.CharField(max_length=80)
    content = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.title
