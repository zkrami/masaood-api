
from rest_framework.routers import url
from user import views

urlpatterns = [
    url(r'^me/', views.UserViewSet.as_view() , name='user-profile'),

]
