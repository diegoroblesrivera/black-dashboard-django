from django.urls import path

from . import views

urlpatterns = [
    # path('', views.index, name='index'),
    path('test', views.test, name='index'),
    path('crear-horario/', views.crear_horario, name='crear_horario'),
]
