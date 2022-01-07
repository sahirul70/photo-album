from django.urls import path
from .import views
#from .views import HomeView, PostDetail

app_name = 'myapp'

urlpatterns = [
    path('', views.index, name='index'),
    path('photo/<str:pk>/', views.viewPhoto, name='photo'),
    path('add/', views.addPhoto, name='add'),
    
]

