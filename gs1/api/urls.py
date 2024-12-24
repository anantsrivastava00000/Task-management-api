from django.urls import path, include
from api import views


urlpatterns = [
    path('', views.task_list_and_retrieve_one_task),
    # path('tasklist/', views.tasklist_with_pagination),
    path('task-create/', views.task_create),
    path('Update-task/', views.Update_task),
    path('delete-task/', views.delete_task),
    # path('filter-task-and-due-date-range/', views.filter_task_and_due_date_range)
    # path('saw/', views.saw)  # for checking
    path('Task_manager_Api/',views.Task_manager_Api)
]

