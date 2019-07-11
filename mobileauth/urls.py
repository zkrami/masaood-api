
from rest_framework import routers
from .views import MobileAuthViewSet
router = routers.SimpleRouter()
router.register('mobile-auth', MobileAuthViewSet)
urlpatterns = router.get_urls()
