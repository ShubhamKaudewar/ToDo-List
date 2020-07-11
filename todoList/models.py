from django.db import models

# Create your models here.
class noteModel(models.Model):
    noteValue = models.TextField(blank=True, null=True)
    noteStar = models.BooleanField(default=False)
    noteStyle = models.CharField(max_length=200,blank=True,null=True)
    noteBold = models.BooleanField(default=False)
    noteItalic = models.BooleanField(default=False)
    noteUnderline = models.BooleanField(default=False)
    noteStrikeThrough = models.BooleanField(default=False)
    noteTextColor = models.CharField(max_length=200,blank=True,null=True,default='black')
    noteBackgroundColor = models.CharField(max_length=200,blank=True,null=True,default='transparent')
    noteCreationDate = models.CharField(max_length=200,blank=True,null=True)
    noteCreationTime = models.CharField(max_length=200,blank=True,null=True)