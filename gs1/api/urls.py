from django.urls import path, include
from api import views


urlpatterns = [
    path('', views.task_list_and_retrieve_one_task),
    path('tasklist/', views.tasklist_with_pagination),
    path('task-create/', views.task_create),
    path('Update-task/', views.Update_task),
    path('delete-task/', views.delete_task)
    # path('saw/', views.saw)  # for checking
]

