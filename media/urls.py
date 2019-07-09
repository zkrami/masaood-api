
from rest_framework import routers
from .views import MediaViewSet
router = routers.SimpleRouter()
router.register('', MediaViewSet)


urlpatterns = router.get_urls() 
