from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from copyloftserver.views.ServiceUserView import ServiceUserList
from copyloftserver.views.UserView import UserList

urlpatterns = [
	url(r'^user/$', UserList.as_view()),
    url(r'^serviceuser/$', ServiceUserList.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)