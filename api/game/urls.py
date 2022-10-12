from rest_framework import routers
from . import views

router = routers.SimpleRouter()

router.register(r'game', views.GameViewSet, basename='game')

urlpatterns = router.urls
