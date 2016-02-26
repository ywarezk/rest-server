"""
adding the api urls to our django project
"""

"""
imports
"""

from django.conf.urls import url
from user.user_viewset import UserRegisterView
from rest_framework.authtoken import views

"""
urls
"""

urlpatterns = [
     url(r'user$', UserRegisterView.as_view(), name='register-user'),
     url(r'user/login$', views.obtain_auth_token, name='login-user'),
]



