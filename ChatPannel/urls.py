from django.urls import path
from .views import *
app_name = 'ChatPannel'
urlpatterns = [
    path('createmessage',CreateMessageView),
    path('groupmember',CreateGroupMemberView),
    path('creategroup',CreateGroupView),
    path('usermessages/<int:from_>/<int:to_>',UserGetMessageView),
    path('groupmessages/<int:grp>',GroupGetMessageView),
    path('all-groups', GroupGetView),
    path('all-files', FilesView),

]
