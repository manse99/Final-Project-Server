from django.db import models
from django.contrib.postgres.fields import ArrayField

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

class Subs(models.Model):
    title = models.CharField(max_length = 20)
    followers = ArrayField(models.IntegerField())
    creator = models.CharField(max_length = 20)
    post_id = ArrayField(models.IntegerField())
    descript = models.TextField()

    def __str__(self):
        return f"{self.title}"

class Comments(models.Model):
    comment =  models.TextField(max_length = 500)
    user_id = models.CharField(max_length = 20)
    post_id = models.CharField(max_length = 20)
    sub_id = models.CharField(max_length = 20)
    up_vote = models.IntegerField()
    down_vote = models.IntegerField()

    def __str__(self):
        return f"{self.comment}"

class User(models.Model):
    user_name = models.CharField(max_length = 20)
    sub_reddits = ArrayField(models.IntegerField())
    comments = ArrayField(models.IntegerField())
    profile_pic = models.TextField()

    def __str__(self):
        return f"{self.user_name}"