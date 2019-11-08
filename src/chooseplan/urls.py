from django.urls import path

from . import views

urlpatterns = [
    path('', views.chooseplan, name='chooseplan'),
]

# path('', views.algorithm, name='iancrueldad')
