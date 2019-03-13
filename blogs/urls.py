from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='blogs'),
    path('<int:blogcontent_id>', views.blogcontent, name='blogcontent')
]
