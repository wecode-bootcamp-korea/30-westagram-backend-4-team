from django.db import models

class TimeStampedModel(models.Model):
    created_at   = models.DateTimeField(auto_now_add=True)
    updated_at   = models.DateTimeField(auto_now=True)
    
    class Meta:
        abstract = True

class Post(TimeStampedModel):
    post_title   = models.CharField(max_length=100)
    post_content = models.CharField(max_length=500)
    image_url    = models.CharField(max_length=200)

    user         = models.ForeignKey('users.User', related_name='posts', on_delete=models.CASCADE) 
    
    class Meta:
        db_table = "postings"

class Comment(TimeStampedModel):
    comment = models.CharField(max_length=300)
    user    = models.ForeignKey('users.User', related_name='comments', on_delete=models.PROTECT) 
    post    = models.ForeignKey('Post', related_name='comments', on_delete=models.CASCADE)
    
    class Meta:
        db_table = "comments"
        
class Like(TimeStampedModel):
    user = models.ForeignKey('users.User', related_name='likes', on_delete=models.PROTECT) 
    post = models.ForeignKey('Post', related_name='likes', on_delete=models.CASCADE)
    
    class Meta:
        db_table = "likes"