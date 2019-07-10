
from rest_framework import routers
from .views import MediaViewSet
router = routers.SimpleRouter()
router.register('medias', MediaViewSet)


urlpatterns = router.get_urls() 
