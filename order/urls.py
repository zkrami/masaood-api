from rest_framework import routers
from order import views
router = routers.SimpleRouter()
router.register('me/orders', views.OrderViewSet)
router.register('orders', views.OrderAdminViewSet)

urlpatterns = router.get_urls()