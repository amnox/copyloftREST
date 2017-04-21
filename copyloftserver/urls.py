from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from copyloftserver.views.ServiceUserView import ServiceUserList
from copyloftserver.views.UserView import UserList
from copyloftserver.views.ServiceUserView import ServiceUserDetail
from copyloftserver.views.UserView import UserDetail
from copyloftserver.views.ServiceUserView import GetServiceUserAddress
from copyloftserver.views.ServiceUserView import UpdateServiceUserAddress
from copyloftserver.views.ServiceUserView import GetServiceUserCart
from copyloftserver.views.ServiceUserView import CreateServiceUserCart
from copyloftserver.views.ServiceUserView import ConcludeServiceUserCart

urlpatterns = [
	url(r'^user/$', UserList.as_view()),
	url(r'^user/(?P<pk>[0-9]+)/$', UserDetail.as_view()),
    url(r'^serviceuser/$', ServiceUserList.as_view()),
    url(r'^serviceuser/(?P<pk>[0-9]+)/$', ServiceUserDetail.as_view()),
    url(r'^serviceuser/(?P<user_id>[0-9]+)/address/$', GetServiceUserAddress.as_view()),
    url(r'^serviceuser/(?P<user_id>[0-9]+)/address/(?P<pk>[0-9]+)/$', UpdateServiceUserAddress.as_view()),
    url(r'^serviceuser/(?P<user_id>[0-9]+)/cart/$', GetServiceUserCart.as_view()),
    url(r'^serviceuser/(?P<user_id>[0-9]+)/cart/create/$', CreateServiceUserCart.as_view()),
    url(r'^serviceuser/(?P<user_id>[0-9]+)/cart/conclude/$', ConcludeServiceUserCart.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)