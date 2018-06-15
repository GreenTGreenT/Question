from django.urls import path
from myapp import views

urlpatterns = [
    path('', views.index, name='index'),
    path('detail/', views.detail, name='detail'),
    path('results/', views.results, name='results'),

]



