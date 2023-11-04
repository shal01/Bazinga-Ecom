from django.urls import path
from . views import TaskList,TaskDetail,CreateTask,UpdateTask,DeleteTask,CustomLogin
from django.contrib.auth.views import LogoutView


urlpatterns = [
    path('login',CustomLogin.as_view(),name='login'),
    path('logout',LogoutView.as_view(next_page='login'),name='logout'),
    path('',TaskList.as_view(),name='tasks'),
    path('task/<int:pk>/',TaskDetail.as_view(),name='task'),
    path('task-create',CreateTask.as_view(),name='task-create'),
    path('task-update/<int:pk>',UpdateTask.as_view(),name='task-update'),
    path('task-Delete/<int:pk>',DeleteTask.as_view(),name='task-Delete'),
]