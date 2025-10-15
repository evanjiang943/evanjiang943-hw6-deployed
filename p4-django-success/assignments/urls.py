from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('create/', views.create_assignment, name='create_assignment'),
    path('assignment/<int:pk>/', views.assignment_detail, name='assignment_detail'),
    path('assignments/', views.assignment_list, name='assignment_list'),
    path('api/generate-rubric/', views.generate_rubric_ajax, name='generate_rubric_ajax'),
]

