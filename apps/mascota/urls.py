from django.urls import path
from django.contrib.auth.decorators import login_required
from apps.mascota.views import index, mascota_view, mascota_list, mascota_edit, mascota_delete, \
    MascotaList, MascotaCreate , MascotaUpdate, MascotaDelete, listado

app_name = 'mascota'

urlpatterns = [
    path('', index, name='index'),
    path('nuevo/', login_required(MascotaCreate.as_view()), name='mascota_create'),
    path('listar/', login_required(MascotaList.as_view()), name='mascota_list'),
    path('listado/', listado, name='mascota_listado'),
    path('editar/<pk>/', login_required(MascotaUpdate.as_view()), name='mascota_edit'),
    path('eliminar/<pk>/', login_required(MascotaDelete.as_view()), name='mascota_delete'),
]