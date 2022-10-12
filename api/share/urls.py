from django.urls import path
from . import views


list_detail = views.ShareListView.as_view({'get': 'list'})

urlpatterns = [
    path('<slug:category>/list/<uuid:user_id>/',
         list_detail, name='list-detail'),
]
