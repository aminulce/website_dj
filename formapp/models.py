from django.db import models

class Snippet(models.Model):
    job = models.TextField()
    resume = models.TextField()

    def __str__(self):
        self.job
        self.resume
