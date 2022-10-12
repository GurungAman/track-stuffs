from rest_framework import routers
from . import views


router = routers.SimpleRouter()

router.register(r'movie', views.MovieViewSet, basename='movie')

urlpatterns = router.urls
