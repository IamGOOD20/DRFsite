"""DRFproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include, re_path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView, TokenVerifyView

from stars.views import *
from rest_framework import routers

'''
class MyCustomRouters(routers.SimpleRouter):
    routes = [
        routers.Route(
            url=r'^{prefix}$',
            mapping={'get': 'list'},
            name='{basename}-list',
            detail=False,
            initkwargs={'suffix': 'List'}),

        routers.Route(
            url=r'^{prefix}/{lookup}$',
            mapping={'get': 'retrieve'},
            name='{basename}-detail',
            detail=True,
            initkwargs={'suffix': 'Detail'}),

        routers.DynamicRoute(
            url=r'^{prefix}/{lookup}/{url_path}$',
            name='{basename}-{url_name}',
            detail=True,
            initkwargs={}
        )
    ]
'''
'''
router = MyCustomRouters()
router.register(r'stars', StarsViewSet, basename= 'ModelStars')
print(router.urls)
'''


urlpatterns = [
    path('admin/', admin.site.urls),
    #path('api/v1/', include(router.urls)), #http://127.0.0.1:8000/api/v1/stars/
    #path('api/v1/starslist/', StarsViewSet.as_view({'get': 'list'})),
    #path('api/v1/starslist/<int:pk>/', StarsViewSet.as_view({'put': 'update'})),
    path('api/v1/drf-auth/', include('rest_framework.urls')),
    path('api/v1/starslist/', StarsAPIList.as_view()),
    path('api/v1/starsupdate/<int:pk>/', StarsAPIUpdate.as_view()),
    path('api/v1/starsdelete/<int:pk>/', StarsAPIDestroy.as_view()),
    path('api/v1/auth/', include('djoser.urls')),
    re_path(r'^auth/', include('djoser.urls.authtoken')),
    path('api/v1/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/v1/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/v1/token/verify/', TokenVerifyView.as_view(), name='token_verify'),
]