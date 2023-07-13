from django.db import models
from authentication.models import User

# Create your models here.
class Groups(models.Model):
    created_by = models.ForeignKey(User,on_delete=models.CASCADE,related_name='group_creator')
    group_name = models.CharField(max_length=30)
    description = models.TextField(null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    is_deleted = models.BooleanField(default=False)

class UserGroup(models.Model):
    group_id = models.ForeignKey(Groups,on_delete=models.CASCADE)
    user_id = models.ForeignKey(User,on_delete=models.CASCADE)

class Messages(models.Model):
    from_user = models.ForeignKey(User,on_delete=models.CASCADE,related_name='sender')
    to = models.ForeignKey(User,on_delete=models.CASCADE,related_name='receiver',null=True)
    group = models.ForeignKey(Groups, on_delete=models.CASCADE,null=True)
    message = models.TextField()
    file = models.ImageField(upload_to="uploads/", null=True, blank=True)
    is_deleted = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    # is_group = models.BooleanField(default=False)

# class GroupMessage(models.Model):
#     message_id = models.ForeignKey(Messages,on_delete=models.CASCADE)
#     group_id = models.ForeignKey(Groups,on_delete=models.CASCADE)
