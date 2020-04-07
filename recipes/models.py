from django.db import models
from django.contrib.auth.models import User


from ckeditor.fields import RichTextField




class Recipe(models.Model):
    name = models.CharField(max_length=200, null=True)
    photo = models.ImageField(null=True, blank=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    publish_date = models.DateTimeField(auto_now_add=True, null=True)
    description = models.CharField(max_length=500, null=True)
    #content = HTMLField(default="", null=True, blank=True)
    # ingredients = models.TextField(max_length=1000, blank=True, null=True)
    # instructions = models.TextField(max_length=20000, blank=True, null=True)
    content = RichTextField(blank=True, null=True)
    comment_count = models.IntegerField(default=0)

    def __str__(self):
        return self.name
    
    # get all the comments related to the post
    @property
    def get_comments(self):
        return self.comments.all().order_by('-timestamp')


class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now_add=True)
    content = models.TextField()
    post = models.ForeignKey(Recipe, related_name='comments', on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username