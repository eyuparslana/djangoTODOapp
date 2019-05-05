from django.db import models
from django.contrib.auth.models import User


class Todo(models.Model):

    CHOISES = (
        (True, 'COMPLATED'),
        (False, 'NOT COMPLATED'),
    )

    id = models.IntegerField(primary_key=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    text = models.TextField()
    is_complated = models.BooleanField(choices=CHOISES)
    last_updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.text

