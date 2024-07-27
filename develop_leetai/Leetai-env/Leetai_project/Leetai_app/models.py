from django.db import models
from accounts.models import CustomUser
# Create your models here.
class Question(models.Model):
    users = models.ForeignKey(CustomUser,models.PROTECT)
    title = models.CharField(max_length=200)
    content = models.TextField(max_length=500,blank=True,null=True)
    datetime = models.DateField(verbose_name='投稿日時',auto_now_add=True)
    photo = models.ImageField(verbose_name="参考画像",blank=True,null=True)
    solve = models.BooleanField(default=False)
    
    class Meta:
        verbose_name_plural = 'Question'
        
    def __str__(self):
        return self.title
    
class Answer(models.Model):
    Question = models.ForeignKey(Question,models.PROTECT)
    title = models.CharField(max_length=200)
    content = models.TextField(max_length=500,blank=True,null=True)
    datetime = models.DateField(verbose_name='投稿日時',auto_now_add=True)
    photo = models.ImageField(verbose_name="参考画像",blank=True,null=True)
    bestanswer = models.BooleanField(default=False)
    users = models.ForeignKey(CustomUser,models.PROTECT,default=1)
    
    class Meta:
        verbose_name_plural = 'Answer'
        
    def __str__(self):
        return self.title
    
    