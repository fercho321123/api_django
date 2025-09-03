from django.urls import path
from .views import (
    PersonaListCreateView,
    PersonaDetailView,
    PersonaByDocumentoList,
    TareaListCreateView,
    TareaDetailView,
    TareaByFechaList,
    TareasPorRangoList,
    TareasPorPersonaList,
    PersonaByDocumentoList,
    TareaListCreate, TareaRetrieveUpdateDestroy,
)

urlpatterns = [
    # CRUD Persona
    path("personas/", PersonaListCreateView.as_view(), name="persona-list-create"),
    path("personas/<int:pk>/", PersonaDetailView.as_view(), name="persona-detail"),
    path("personas/documento/<str:documento>/", PersonaByDocumentoList.as_view(), name="persona-por-documento"),

    # CRUD Tarea
    path("tareas/<int:pk>/", TareaDetailView.as_view(), name="tarea-detail"),

    # Filtros de Tarea
    path("tareas/fecha/<str:fecha_limite>/", TareaByFechaList.as_view(), name="tareas-por-fecha"),
    path('tareas/rango/<str:fecha_inicio>/<str:fecha_fin>/', TareasPorRangoList.as_view(), name='tareas-por-rango'),
    path("tareas/persona/<str:tipo_doc>/<str:documento>/", TareasPorPersonaList.as_view(), name="tareas-por-persona"),
    
    path('tareas/persona/<str:tipo_doc>/<str:documento>/',TareasPorPersonaList.as_view(),name='tareas-por-persona'),

    path('personas/filtro/', PersonaByDocumentoList.as_view(), name='persona-filtro'),


    path('tareas/', TareaListCreate.as_view(), name='tareas-list-create'),
    path('tareas/<int:pk>/', TareaRetrieveUpdateDestroy.as_view(), name='tareas-detail'),
    path('personas/filtro/', PersonaByDocumentoList.as_view(), name='persona-filtro'),

] 
