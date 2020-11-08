from django.conf.urls import url, include
from rest_framework.routers import DefaultRouter
from account import views

router = DefaultRouter()
router.register('user', views.UserViewSet)

urlpatterns = [
    url(r'^register/', include(router.urls)),
    url(r'^authenticate/', views.Authenticate.as_view(), name='authenticate')
]