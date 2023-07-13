from rest_framework import serializers
from .models import *


class GroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = Groups
        fields = ['id','created_by', 'group_name', 'description', 'created_at', 'is_deleted']


class UserGroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserGroup
        fields = ['id', 'group_id', 'user_id']


class MessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Messages
        fields = ['id', 'from_user', 'to', 'message', 'file', 'is_deleted', 'is_group']


# class GroupMessageSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = GroupMessage
#         fields = ['id', 'message_id', 'group_id']
