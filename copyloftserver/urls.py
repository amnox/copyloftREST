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
from copyloftserver.views.ServiceUserView import ServiceUserCartBooks
from copyloftserver.views.ServiceUserView import ServiceUserCartBook
from copyloftserver.views.PageView import PageList
from copyloftserver.views.PageView import PageSingle
from copyloftserver.views.PageView import PageQualityList
from copyloftserver.views.PageView import PageQualitySingle
from copyloftserver.views.PageView import PageInkList
from copyloftserver.views.PageView import PageInkSingle

urlpatterns = [
    url(r'^v1.0/user/$', UserList.as_view()),
    url(r'^v1.0/user/(?P<pk>[0-9]+)/$', UserDetail.as_view()),

    url(r'^v1.0/service_user/$', ServiceUserList.as_view()),
    url(r'^v1.0/service_user/(?P<pk>[0-9]+)/$', ServiceUserDetail.as_view()),
    url(r'^v1.0/service_user/(?P<user_id>[0-9]+)/address/$', GetServiceUserAddress.as_view()),
    url(r'^v1.0/service_user/(?P<user_id>[0-9]+)/address/(?P<pk>[0-9]+)/$', UpdateServiceUserAddress.as_view()),
    url(r'^v1.0/service_user/(?P<user_id>[0-9]+)/cart/$', GetServiceUserCart.as_view()),
    url(r'^v1.0/service_user/(?P<user_id>[0-9]+)/cart/create/$', CreateServiceUserCart.as_view()),
    url(r'^v1.0/service_user/(?P<user_id>[0-9]+)/cart/conclude/$', ConcludeServiceUserCart.as_view()),
    url(r'^v1.0/service_user/(?P<user_id>[0-9]+)/cart/books/$', ServiceUserCartBooks.as_view()),
    url(r'^v1.0/service_user/(?P<user_id>[0-9]+)/cart/book/(?P<pk>[0-9]+)/$', ServiceUserCartBook.as_view()),

    url(r'^v1.0/service/page_type/$', PageList.as_view()),
    url(r'^v1.0/service/page_type/(?P<pk>[0-9]+)/$', PageSingle.as_view()),
    url(r'^v1.0/service/page_quality/$', PageQualityList.as_view()),
    url(r'^v1.0/service/page_quality/(?P<pk>[0-9]+)/$', PageQualitySingle.as_view()),
    url(r'^v1.0/service/page_ink/$', PageInkList.as_view()),
    url(r'^v1.0/service/page_ink/(?P<pk>[0-9]+)/$', PageInkSingle.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)
