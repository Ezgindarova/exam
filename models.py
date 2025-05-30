from django.db import models
from django.contrib.auth.models import User

class veexam(models.Model):
    exam_name = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)
    exam_date = models.DateTimeField()
    exam_image = models.ImageField(upload_to='exam_images/')
    users = models.ManyToManyField(User)
    is_public = models.BooleanField(default=False)

    def __str__(self):
        return self.exam_name