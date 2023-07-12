from rest_framework.decorators import api_view,permission_classes
from rest_framework.permissions import AllowAny,IsAuthenticated
from rest_framework.response import Response
from .models import *
from .serializers import *

# Create your views here.

@api_view(['POST'])
@permission_classes([IsAuthenticated])

def follow(request):
    from_user=request.user.id
    me = {'from_user':from_user}
    data=request.data
    data.update(me)
    serializer = FollowSerializer(data=data)
    if serializer.is_valid():
        serializer.save()
        return Response({'message':'request send'})
    return Response({'message':'failed to follow'})

# {
#     "to":3
# }

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def accept(request):
    follow_id=request.data['follow_id']
    Follow.objects.filter(id=follow_id).update(is_accepted=True)
    return Response({'message':'You have a new friend'})

# {
#     "follow_id":1
# }


@api_view(['POST'])
def unfollow(request):
    follow_id = request.data['follow_id']
    Follow.objects.filter(id=follow_id).update(is_unfollowed=True)
    return Response({'message':'successful unfollowing'})

# {
#     "follow_id":1
# }