from django.db import models

class Video(models.Model):
    video_file = models.FileField(upload_to='videos/')
    email = models.EmailField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Video uploaded by {self.email} at {self.timestamp}'
