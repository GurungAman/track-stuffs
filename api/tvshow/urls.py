from rest_framework import routers
from . import views

router = routers.SimpleRouter()

router.register(r'tv-show', views.TvShowViewSet, basename='tv-show')

urlpatterns = router.urls
