from django.db import models


class Article(models.Model):
    title =models.CharField(max_length=100)
    slug = models.SlugField()
    body = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    #add in thumbnail later
    #add in aurthor later

    def __str__(self):
        return self.title
    '''
    def snippet(self):
        return self.body[:150]
    '''

