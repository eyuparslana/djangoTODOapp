from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone


class Todo(models.Model):

    CHOISES = (
        (True, 'COMPLATED'),
        (False, 'NOT COMPLATED'),
    )

    user = models.ForeignKey(User, on_delete=models.CASCADE, null=False)
    text = models.TextField(max_length=100, null=False)
    is_complated = models.BooleanField(choices=CHOISES, null=False)
    created = models.DateTimeField(auto_now=True)
    modified = models.DateTimeField(auto_now=True)

    def save(self, *args, **kwargs):
        if not self.id:
            self.created = timezone.now()
        self.modified = timezone.now()
        return super(Todo, self).save(*args, **kwargs)

