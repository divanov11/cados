from django.db import models
from django.contrib.auth.models import User 
# Create your models here.


class Company(models.Model):
    name = models.CharField(max_length=200)
    logo = models.ImageField(default='', upload_to="", blank=True, null=True)
    bio = models.TextField(blank=True, null=True)
    #tags = 
    website =  models.CharField(max_length=200, null=True, blank=True)
    
    def __str__(self):
        return self.name

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True)
    avatar = models.ImageField(default='', upload_to="", blank=True, null=True)
    name = models.CharField(max_length=200)
    socials = models.ManyToManyField('Social', blank=True)
    skills = models.ManyToManyField('Skill', blank=True)

class Review(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    body = models.TextField()
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.body


class Social(models.Model):
    icon = models.ImageField(default='', upload_to="", blank=True, null=True)
    link = models.CharField(max_length=200, null=True, blank=True)

class Skill(models.Model):
    name = models.CharField(max_length=200, blank=True, null=True)


class Post(models.Model):
    OPTIONS = (
        ('collab','collab'),
        ('job','job'),
        ('default','default'),
        )

    owner = models.ForeignKey(User, models.CASCADE, blank=True, null=True)
    post_type = models.CharField(choices=OPTIONS, default=OPTIONS[2], max_length=1000)
    body = models.TextField()
    likes = models.ManyToManyField(User, related_name="likes",blank=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.body[0:50]

class Comment(models.Model):
    owner = models.ForeignKey(User, models.CASCADE, blank=True, null=True)
    post = models.ForeignKey(Post, models.CASCADE, blank=True, null=True)
    body = models.TextField()
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.body[0:50]
