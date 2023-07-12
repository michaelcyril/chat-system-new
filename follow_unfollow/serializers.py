from rest_framework import serializers
from .models import *

class FollowSerializer(serializers.ModelSerializer):
    class Meta:
        model=Follow
        fields=['id','from_user','to','is_accepted','created_at','accepted_at']

    def create(self, validated_data):
        from_user = self.validated_data['from_user']
        to = self.validated_data['to']
        # is_accepted = self.validated_data['is_accepted']
        following = Follow.objects.create(from_user=from_user,to=to)
        return following