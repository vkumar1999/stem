from django.db import models
class Category(models.Model):
    name = models.CharField(max_length=50)
    def __str__(self):
        return self.name
class BlogPost(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    image = models.ImageField(upload_to='blog_images/')
    category = models.ForeignKey(Category, on_delete=models.PROTECT)  # A post belongs to a category
    created_at = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.title






