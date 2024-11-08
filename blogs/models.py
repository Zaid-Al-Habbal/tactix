from django.db import models

class Author(models.Model):

    MEMBERSHIP_BRONZE = 'B'
    MEMBERSHIP_SILVER = 'S'
    MEMBERSHIP_GOLD   = 'G'

    MEMBERSHIP_CHOICES = [
        (MEMBERSHIP_BRONZE, 'Bronze'),
        (MEMBERSHIP_SILVER, 'Silver'),
        (MEMBERSHIP_GOLD,   'Gold'),
    ]
    #author columns:
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    membership = models.CharField(max_length=1, choices=MEMBERSHIP_CHOICES, default='B')

    
class Article(models.Model):
    #article columns:
    #Article wrote by one user:
    author = models.ForeignKey(Author, on_delete=models.CASCADE, related_name="articles")
    #people who rate this article:
    users = models.ManyToManyField(Author, through="Rating")
    title = models.CharField(max_length=255)
    body = models.TextField()
    last_update = models.DateTimeField(auto_now=True)


class Comment(models.Model):
    #comment columns:
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    article = models.ForeignKey(Article, on_delete=models.CASCADE, related_name="comments")
    body = models.TextField()
    

class Rating(models.Model):
    #rated columns:
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    num_of_stars = models.IntegerField()


