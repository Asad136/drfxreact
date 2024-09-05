from django.urls import path
from . import views
from django.conf.urls.static import static

urlpatterns = [
    path('register/', views.signup, name='register'),
    path('login/', views.loginuser, name='login'),
    path('tasks/', views.get_task_list, name='get_task_list'),
    path('tasks/create/', views.create_task, name='create_task'),
    path('tasks/<int:pk>/', views.get_task_detail, name='get_task_detail'),
    path('tasks/<int:pk>/update/', views.update_task, name='update_task'),
    path('tasks/<int:pk>/delete/', views.delete_task, name='delete_task'),
]
