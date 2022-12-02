from django.urls import path
from . import views
urlpatterns = [
    path('',views.home, name = 'inicio'),
    path('facultad/<id>',views.homeFacultad),
    path('publicacion/<id>',views.publicacion),
    path('crearPublicacion/',views.crearPublicacion),
    path('gestionarPublicacion/',views.gestionarPublicacion,name='gestionarPublicacion'),
    path('gestionarPublicacion/edicionPublicacion/<id>',views.edicionPublicacion),
    path('gestionarPublicacion/eliminarPublicacion/<id>',views.eliminarPublicacion),
    path('editarPublicacion/',views.editarPublicacion),
    path('favoritos',views.favoritos,name='favoritos'),
    path('listas',views.listas,name='listas'),
    path('crearFavorito',views.publicacionFavorita),
    path('eliminarFavorito',views.eliminarFavorita),
    path('eliminarFavorito/<id>',views.deleteFavoritoList),
    path('registrar/',views.registrarCuenta,name='registrar'),
    path('comentarPublicacion',views.comentarPublicacion)
]
