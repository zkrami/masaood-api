
from rest_framework.routers import url, SimpleRouter
from user import views


router = SimpleRouter()
router.register("users", views.AdminUserViewSet)
router.register("groups", views.GroupsViewSet)

urlpatterns = [
    url(r'^me/', views.UserViewSet.as_view(), name='user-profile'),
]

urlpatterns += router.get_urls()
