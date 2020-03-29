from django.db import models

# Create your models here.
class course(models.Model):
    title= models.CharField(max_length=300)
    slug= models.SlugField(max_length=300, unique=True, blank=True)
    content= models.TextField()
    pub_date = models.DateTimeField(auto_now_add= True)
    last_edited= models.DateTimeField(auto_now= True)
    author= models.ForeignKey(User)
    likes= models.IntegerField(default=0)
    dislikes= models.IntegerField(default=0)


    def __str__(self):
        return self.title
class instructor(models.Model):
    title= models.CharField(max_length=300)
    slug= models.SlugField(max_length=300, unique=True, blank=True)
    content= models.TextField()
    pub_date = models.DateTimeField(auto_now_add= True)
    last_edited= models.DateTimeField(auto_now= True)
    author= models.ForeignKey(User)
    likes= models.IntegerField(default=0)
    dislikes= models.IntegerField(default=0)


    def __str__(self):
        return self.title        

