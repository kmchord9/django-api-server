from django.contrib import admin
from django.urls import path, include
from rest_framework import routers

from api.views import LogViewSet
from api.views import MainView

router = routers.DefaultRouter()
router.resgister(r'logs', LogViewSet)

urlpatterns = [
  path('admin/', admin.site.urls),
  path('api/', include(router.urls)),
  path('', MainView.as_view),

]

admin.site.site_header = '気温と湿度の変化'