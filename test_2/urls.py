from django.urls import path
from myapp import views

urlpatterns = [
    path('', views.index, name='index'),
    path('detail/<int:question_id>', views.detail, name='detail'),
    path('keepresults/<int:question_id>', views.keep_results, name='keep_results'),
    path('createpage/', views.create_page, name='create_page'),
    path('create/', views.create, name='create'),
]



