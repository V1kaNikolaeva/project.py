from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('tests', views.tests),
    path('chCards', views.chCards),

]
