from django.urls import path
from rest_framework import routers
from . import views

router = routers.SimpleRouter()

router.register(r'movie', views.MovieViewSet, basename='movie')
router.register(r'tv-show', views.TvShowViewSet, basename='tv-show')
router.register(r'game', views.GameViewSet, basename='game')

urlpatterns = router.urls


list_detail = views.ShareListView.as_view({'get': 'list'})


urlpatterns += [
    path('<slug:category>/list/<uuid:user_id>/',
         list_detail, name='list-detail')
]
