
from rest_framework import routers
from .views import PasswordAuthTokenView
router = routers.SimpleRouter()
router.register('password-auth', PasswordAuthTokenView , basename='password-auth')
urlpatterns = router.get_urls()
