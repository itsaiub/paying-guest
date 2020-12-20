from django.urls import path
from . import views

app_name = 'couches'

urlpatterns = [
    path('', views.index, name='couches'),
    path('<int:couch_id>/', views.couch, name='couch'),
    path('search/', views.search, name='search'),
]
