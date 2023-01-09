from django.conf import settings
from django.db import models
from django.utils import timezone

# Create your models here.


"""Model with name getting from loged in user, title of the post displayed as identifier, text of post, created at data which is taken at creation time automatically and published at date, which is taken when publish method is called. """


class Post(models.Model):

    name = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True
    )
    title = models.CharField("Title of post", max_length=125)
    text = models.TextField("Enter the text here")
    created_at = models.DateTimeField(default=timezone.now)
    published_at = models.DateTimeField(null=True, blank=True, auto_now_add=True)

    def __str__(self):
        return self.title


# Feedback model, one post
class FeedbackPost(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    name = models.CharField(max_length=150)  # username
    email = models.EmailField("Enter your email.", max_length=254)
    feedback = models.TextField("Write your feedback.")

    def __str__(self):
        return self.name
