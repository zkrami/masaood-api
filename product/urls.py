
from rest_framework import routers
from product import views
router = routers.SimpleRouter()
router.register('abstract-products', views.AbstractProductViewSet)
router.register('sizes', views.SizeViewSet)
router.register('grades', views.GradeViewSet)
router.register('products', views.ProductViewSet)
urlpatterns = router.get_urls()