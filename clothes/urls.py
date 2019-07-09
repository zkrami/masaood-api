from rest_framework.urls import url
from . import views

from rest_framework import routers

router = routers.SimpleRouter()
#router.register('', views.ClothAPI)
urlpatterns = [
    url("", views.ClothAPI.as_view())
]
