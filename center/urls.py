
from rest_framework import routers
from center import views
router = routers.SimpleRouter()
router.register('centers', views.CenterViewSet)

urlpatterns = router.get_urls()
