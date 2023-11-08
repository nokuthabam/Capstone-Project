from django.db import models

# Create your models here.
class Post(models.Model):
    """
    This class will create a post.
    Parameters:
        models.Model: model
    Attributes:
        title: str
        content: str
        date: date
    """
    title = models.CharField(max_length=100)
    content = models.TextField()
    image = models.ImageField(upload_to='images/', blank=True, null=True)
    date = models.DateField(auto_now_add=True)
    
    
    def __str__(self):
        """
        This method will return the title of the post.
        Parameters:
            self: Post object
        Returns:
            title: str
        """
        return self.title   