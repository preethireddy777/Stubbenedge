from django.urls import path

from . import views

urlpatterns = [
    path('', views.load_queeze, name='load_queeze'),
    path('prepare_data', views.prepare_data, name='prepare_data'),
    path('validate_answer', views.validate_answer, name='validate_answer')
]