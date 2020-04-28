from django.urls import path
from django.contrib.auth.decorators import login_required

from apps.adopcion.views import index, SolicitudList ,SolicitudCreate, SolicitudUpdate, SolicitudDelete

app_name = 'adopcion'

urlpatterns = [
    path('',index),
    path('solicitud/listar',login_required(SolicitudList.as_view()),name='solicitud_list'),
    path('solicitud/nueva',login_required(SolicitudCreate.as_view()),name='solicitud_create'),
    path('solicitud/editar/<pk>',login_required(SolicitudUpdate.as_view()),name='solicitud_update'),
    path('solicitud/eliminar/<pk>',login_required(SolicitudDelete.as_view()),name='solicitud_delete'),
]