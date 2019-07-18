
from rest_framework import routers
from state import views
router = routers.SimpleRouter()
router.register('states', views.StateViewSet)
urlpatterns = router.get_urls()