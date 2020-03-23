from django.urls import path

from core import views

urlpatterns = [
    path('stats/', views.get_stats, name='get_stats'),
    path('building/', views.building_new, name='building_new'),
    path('building/<int:pk>/', views.building_detail, name='building_detail'),
    path('building/<int:pk>/edit/', views.building_edit, name='building_edit'),
    path('building/<int:pk>/add-bricks/', views.add_bricks, name='add_bricks')
]