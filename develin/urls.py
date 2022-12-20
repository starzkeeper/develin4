
from django.contrib import admin
from django.urls import path, include, re_path
from rest_framework import routers

from electronic.views import ProductAPIView
router = routers.SimpleRouter()
router.register(r'products',ProductAPIView)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v2/',include(router.urls)),
    path('api/v2/drf-auth/',include('rest_framework.urls')),
    path('api/v2/auth/',include('djoser.urls')),
    re_path(r'^auth/',include('djoser.urls.authtoken')),
    path('',include('vision.urls'))

]
