"""
Urls for our project
"""

"""
imports
"""

from django.conf.urls import url, include
from django.contrib import admin

"""
urls
"""

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^api/v1.0/', include('rest_server.api.urls'))
]
