# from django.conf.urls import url

from django.urls import re_path
from UserApp import views

###------------------------------Note------------------------------###
#   Don't forget to update these URLS in the main urls.py file      #
###----------------------------------------------------------------###

urlpatterns = [
    re_path(r'^user/$',views.UserApi),
    re_path(r'^user/([0-9]+)/$',views.UserApi),
]

# urlpatters=[
#     url(r'^user/$',views.UserApi),
#     url(r'^user/([0-9]+)$',views.UserApi)
# ]