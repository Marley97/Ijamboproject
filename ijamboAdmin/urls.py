from django.urls import path
from .import views
urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    path('umuziki/', views.music, name='imiziki'),
    path('urukurikirane/', views.musicalbum, name='albumu'),
    path('iyukwezi/', views.songmonth, name='yukwezi'),
    path('listMusic/', views.ListMusic, name='listeM'),
    path('show/', views.EventRegester, name='ikirori'),
    
    
]
