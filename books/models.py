from django.db import models


class Books(models.Model):
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=255)
    description = models.TextField()
    image = models.ImageField(
        upload_to="book/images", default="book/images/default.jpg"
    )

    def __str__(self) -> str:
        return self.title
