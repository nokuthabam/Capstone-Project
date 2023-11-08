from django.db import models

# Create your models here.
class Post(models.Model):
    """
        This class represents a blog post.

        :param models.Model: The base model class
        :type models.Model: django.db.models.Model

        :ivar title: The title of the blog post
        :vartype title: str
        :ivar content: The content of the blog post
        :vartype content: str
        :ivar image: An optional image for the blog post
        :vartype image: django.db.models.ImageField
        :ivar date: The date of the blog post creation
        :vartype date: datetime.date
    """
    title = models.CharField(max_length=100)
    content = models.TextField()
    image = models.ImageField(upload_to='images/', blank=True, null=True)
    date = models.DateField(auto_now_add=True)
    
    
    def __str__(self):
        """
        Return the title of the post.

        :param self: The Post object
        :type self: Post

        :return: The title of the post
        :rtype: str
        """
        return self.title   