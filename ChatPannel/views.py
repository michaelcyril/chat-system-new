from rest_framework.decorators import api_view,permission_classes
from rest_framework.permissions import AllowAny,IsAuthenticated
from .models import *
from .serializers import *
from authentication.models import User
from rest_framework.response import Response
# Create your views here.
from django.db.models import Q


@api_view(['POST'])
@permission_classes([AllowAny])
def CreateMessageView(request):
    try:
        data = request.data
        from_user = User.objects.get(id=data['from_user'])
        to = User.objects.get(id=data['to'])
        message = data['message']
        file = data['file']
        new_message = Messages.objects.create(from_user=from_user, to=to, message=message, file=file)
        new_message.save()
        return Response({'message':'message sent'})
    except KeyError:
        pass

    try:
        data = request.data
        from_user = User.objects.get(id=data['from_user'])
        to = User.objects.get(id=data['to'])
        message = data['message']
        new_message = Messages.objects.create(from_user=from_user, to=to, message=message)
        new_message.save()
        return Response({'message':'message sent'})


    except KeyError:
        pass

    try:
        data = request.POST
        from_user = User.objects.get(id=data['from_user'])
        group = Groups.objects.get(id=data['group'])
        message = data['message']
        file = request.FILES.get('file')
        new_message = Messages.objects.create(from_user=from_user, group=group, message=message, file=file)
        new_message.save()
        return Response({'message':'message sent'})

    except KeyError:
        pass

    try:
        data = request.POST
        from_user = User.objects.get(id=data['from_user'])
        group = Groups.objects.get(id=data['group'])
        # message = data['message']
        file = request.FILES.get('file')
        new_message = Messages.objects.create(from_user=from_user, group=group, file=file)
        new_message.save()
        return Response({'message':'message sent'})

    except KeyError:
        pass

    try:
        data = request.POST
        from_user = User.objects.get(id=data['from_user'])
        to = User.objects.get(id=data['to'])
        # message = data['message']
        file = request.FILES.get('file')
        new_message = Messages.objects.create(from_user=from_user, to=to, file=file)
        new_message.save()
        return Response({'message':'message sent'})

    except KeyError:
        pass

    try:
        data = request.data
        from_user = User.objects.get(id=data['from_user'])
        group = Groups.objects.get(id=data['group'])
        message = data['message']
        new_message = Messages.objects.create(from_user=from_user, group=group, message=message)
        new_message.save()
        return Response({'message':'message sent'})
    except:
        return Response({'message': 'Fail'})


# {
#     "from_user":1,
#     "to":2,
#     "group":1,
#     "message":"hey group",
#     "file":""
# }


@api_view(['POST'])
@permission_classes([AllowAny])
def CreateGroupView(request):
    try:
        data = request.data
        created_by = User.objects.get(id=data['user_id'])
        group_name = data['name']
        description = data['description']
        new_group = Groups.objects.create(created_by=created_by, group_name=group_name, description=description)
        new_group.save()
        return Response({'sms': 'success'})
    except:
        data = request.data
        created_by = User.objects.get(id=data['user_id'])
        group_name = data['name']
        new_group = Groups.objects.create(created_by=created_by, group_name=group_name)
        new_group.save()
        return Response({'sms': 'success'})


# {
#     "user_id":1,
#     "name":"Myg",
#     "description":"hey there"
# }


@api_view(['POST'])
@permission_classes([AllowAny])
def CreateGroupMemberView(request):
    data = request.data
    members = data['members']
    group = Groups.objects.get(id=data['group_id'])
    for memb_id in members:
        user = User.objects.get(id=memb_id)
        group_user = UserGroup.objects.create(group_id=group, user_id=user)
        group_user.save()
    return Response({'message':'successful creating group members'})

# {
#     "group_id":1,
#     "members":[1,2]
# }


@api_view(['GET'])
@permission_classes([AllowAny])

def UserGetMessageView(request,from_, to_):
    from_ = User.objects.get(id=from_)
    to_ = User.objects.get(id=to_)
    queryset = Messages.objects.filter(Q(from_user=to_)&Q(to=from_))
    print(queryset)
    queryset1 = Messages.objects.filter(Q(from_user=from_)&Q(to=to_))
    print(queryset1)
    m = []
    if len(queryset) > 0:

        for data in queryset:
            if data.file:
                d = {
                    'from_user': data.from_user.username,
                    'from_user_id': data.from_user.id,
                    # 'to': data.group.id,
                    'file': data.file.name,
                    'message': data.message,
                    # 'file': data.file
                }
            else:
                d = {
                    'from_user': data.from_user.username,
                    'from_user_id': data.from_user.id,
                    # 'to': data.group.id,
                    # 'file': data.file,
                    'message': data.message,
                    # 'file': data.file
                }
            m.append(d)

    if len(queryset1) > 0:

        for data in queryset1:
            if data.file:
                d = {
                    'from_user': data.from_user.username,
                    'from_user_id': data.from_user.id,
                    # 'to': data.group.id,
                    'file': data.file.name,
                    'message': data.message,
                    # 'file': data.file
                }
            else:
                d = {
                    'from_user': data.from_user.username,
                    'from_user_id': data.from_user.id,
                    # 'to': data.group.id,
                    # 'file': data.file,
                    'message': data.message,
                    # 'file': data.file
                }
            m.append(d)


    return Response(m)



@api_view(['GET'])
@permission_classes([AllowAny])
def GroupGetMessageView(request,grp):
    group = Groups.objects.get(id=grp)
    message = Messages.objects.filter(group=group)
    m = []
    for data in message:
        if data.file:
            d = {
                'from_user': data.from_user.username,
                'from_user_id': data.from_user.id,
                # 'to': data.group.id,
                'file': data.file.name,
                'message': data.message,
                # 'file': data.file
            }
        else:
            d = {
                'from_user': data.from_user.username,
                'from_user_id': data.from_user.id,
                # 'to': data.group.id,
                # 'file': data.file,
                'message': data.message,
                # 'file': data.file
            }
        m.append(d)
        # d = {
        #     'from_user': data.from_user.username,
        #     'from_user_id': data.from_user.id,
        #     'group': data.group.id,
        #     'message': data.message,
        #     # 'file': data.file
        # }
        m.append(d)

    # list = [entry for entry in message]
    return Response(m)


@api_view(['GET'])
@permission_classes([AllowAny])
def GroupGetView(request):
    groups = Groups.objects.values('id', 'created_by', 'group_name', 'description', 'created_at').filter(is_deleted=False)

    return Response(groups)