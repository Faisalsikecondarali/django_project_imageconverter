from django.urls import path
from . import views

urlpatterns = [
    path('convert-image', views.convert_image, name='convert_image'),
    path('', views.index, name='index'),

]
