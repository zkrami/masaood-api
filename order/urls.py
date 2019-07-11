from rest_framework import routers
from order import views
router = routers.SimpleRouter()
router.register('orders', views.OrderViewSet)
urlpatterns = router.get_urls()