from django.db import models

class Post(models.Model):
    created_at     = models.DateTimeField(auto_now_add=True)
    posted_title   = models.CharField(max_length=100)
    posted_content = models.CharField(max_length=1000, blank=True)
    posted_image   = models.ImageField()
    user           = models.ForeignKey('users.User', on_delete=models.CASCADE)

    class Meta:
        db_table = 'posts'