from django.db import models
from django_extensions.db.models import TimeStampedModel
from django.contrib.auth import get_user_model
from posts.models import Post

User = get_user_model()

class Comment(TimeStampedModel):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    text = models.TextField()
   
   
class Like(TimeStampedModel):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    comment = models.ForeignKey(Comment, on_delete=models.CASCADE)
    

