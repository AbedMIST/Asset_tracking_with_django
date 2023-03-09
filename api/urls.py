# from django.contrib import admin
# from django.urls import path, include
# from rest_framework import routers
# from .views import AssetViewSet
# from .views import AssignAssetView
# from .views import ReturnAssetView
#
# router = routers.DefaultRouter()
# router.register(r'assets', AssetViewSet)
#
# urlpatterns = [
#     path('', include(router.urls)),
# ]
#
# urlpatterns += [
#     path('assign/<int:pk>/', AssignAssetView.as_view(), name='assign_asset'),
#     path('return/<int:pk>/', ReturnAssetView.as_view(), name='return_asset'),
# ]

from django.urls import path, include
from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register(r'assets', views.AssetViewSet)
router.register(r'employees', views.EmployeeViewSet)

app_name = 'assets'

urlpatterns = [
    path('', include(router.urls)),
]

