from django.contrib import admin
from django.conf.urls import url, include

urlpatterns = [
    url('admin/', admin.site.urls),
    url(r'^', include('mainApp.urls'))
    url(r'^login/', include('login.urls'))
]
