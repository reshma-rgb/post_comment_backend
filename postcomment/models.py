from django.db import models

# Create your models here.
class UserPost(models.Model):
    user_name = models.CharField(max_length=50,unique=True)
    full_name = models.CharField(max_length=200,blank=True)
    user_email = models.EmailField()
    website = models.URLField(max_length = 100,blank= True)
    company = models.CharField(max_length=200,blank=True)

    def __str__(self):
        return self.user_name

class Post(models.Model):
    title = models.CharField(max_length=200, unique=True)
    content = models.TextField()
    userpost = models.ForeignKey(UserPost,on_delete=models.CASCADE,related_name = 'posts')

    def __str__(self):
        return self.title

class Comment(models.Model):
    post = models.ForeignKey(Post,on_delete=models.CASCADE,related_name = 'comments')
    subject = models.CharField(max_length=80,unique=True)
    email = models.EmailField()
    body = models.TextField()

    def __str__(self):
        return self.subject
