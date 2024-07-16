from django.urls import path
from .views import *
from . import views

app_name = 'board'

urlpatterns = [
    path('home/', board_list),
    path('home/<int:pk>/',board_detail),
    path('region/<str:region>/', board_region),
    path('name/<str:name>/',board_name)

]