from django.db import models

class Post(models.Model):
    title = models.CharField(max_length = 100)
    text = models.TextField()
    img_url = models.TextField()
    up_vote = models.IntegerField()
    down_vote = models.IntegerField()
    user_id = models.IntegerField()
    sub_reddit_id = models.IntegerField()

    def __str__(self):
        return f"{self.title}"
