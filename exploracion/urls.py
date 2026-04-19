from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    # Astronauta
    path('astronautas/', views.AstronautaListView.as_view(), name='astronauta_list'),
    path('astronautas/<int:pk>/', views.AstronautaDetailView.as_view(), name='astronauta_detail'),
    path('astronautas/create/', views.AstronautaCreateView.as_view(), name='astronauta_create'),
    path('astronautas/<int:pk>/update/', views.AstronautaUpdateView.as_view(), name='astronauta_update'),
    path('astronautas/<int:pk>/delete/', views.AstronautaDeleteView.as_view(), name='astronauta_delete'),

    # Ingeniero
    path('ingenieros/', views.IngenieroListView.as_view(), name='ingeniero_list'),
    path('ingenieros/<int:pk>/', views.IngenieroDetailView.as_view(), name='ingeniero_detail'),
    path('ingenieros/create/', views.IngenieroCreateView.as_view(), name='ingeniero_create'),
    path('ingenieros/<int:pk>/update/', views.IngenieroUpdateView.as_view(), name='ingeniero_update'),
    path('ingenieros/<int:pk>/delete/', views.IngenieroDeleteView.as_view(), name='ingeniero_delete'),

    # Nave
    path('naves/', views.NaveListView.as_view(), name='nave_list'),
    path('naves/<int:pk>/', views.NaveDetailView.as_view(), name='nave_detail'),
    path('naves/create/', views.NaveCreateView.as_view(), name='nave_create'),
    path('naves/<int:pk>/update/', views.NaveUpdateView.as_view(), name='nave_update'),
    path('naves/<int:pk>/delete/', views.NaveDeleteView.as_view(), name='nave_delete'),

    # Mision
    path('misiones/', views.MisionListView.as_view(), name='mision_list'),
    path('misiones/<int:pk>/', views.MisionDetailView.as_view(), name='mision_detail'),
    path('misiones/create/', views.MisionCreateView.as_view(), name='mision_create'),
    path('misiones/<int:pk>/update/', views.MisionUpdateView.as_view(), name='mision_update'),
    path('misiones/<int:pk>/delete/', views.MisionDeleteView.as_view(), name='mision_delete'),

    # RegistroExploracion
    path('registros/', views.RegistroExploracionListView.as_view(), name='registroexploracion_list'),
    path('registros/<int:pk>/', views.RegistroExploracionDetailView.as_view(), name='registroexploracion_detail'),
    path('registros/create/', views.RegistroExploracionCreateView.as_view(), name='registroexploracion_create'),
    path('registros/<int:pk>/update/', views.RegistroExploracionUpdateView.as_view(), name='registroexploracion_update'),
    path('registros/<int:pk>/delete/', views.RegistroExploracionDeleteView.as_view(), name='registroexploracion_delete'),
]