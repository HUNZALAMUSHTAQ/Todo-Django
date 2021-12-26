from django.db import models

# Create your models here.


class Task(models.Model):
    content = models.CharField(max_length=200)
    complete = models.BooleanField(default=False)
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return self.content
