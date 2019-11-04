from django.urls import path, include
from . import views
from rest_framework import routers

router = routers.DefaultRouter()
router.register('Product', views.ProductView)
router.register('Category', views.CategoryView)


urlpatterns = [
    path('', include(router.urls))
]
