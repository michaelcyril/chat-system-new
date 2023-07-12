from django.db import models

# Create your models here.
class Follow(models.Model):
    from_user = models.IntegerField()
    to = models.IntegerField()
    is_accepted=models.BooleanField(default=False)
    created_at=models.DateTimeField(auto_now_add=True)
    accepted_at=models.DateTimeField(null=True)
    is_unfollowed=models.BooleanField(default=False)