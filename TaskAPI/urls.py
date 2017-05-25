
from django.conf.urls import include, url
from django.contrib import admin
from rest_framework import routers
from TaskApp.views import TaskViewSet

router = routers.DefaultRouter()
router.register(r'task',TaskViewSet)

urlpatterns = [
    url(r'^', include(router.urls)),
    url(r'^admin/', include(admin.site.urls)),
]
