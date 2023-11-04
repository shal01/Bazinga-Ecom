from typing import Any
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView,UpdateView,DeleteView
from . models import TaskModel
from django.contrib.auth.views import LoginView
from django.contrib.auth.mixins import LoginRequiredMixin



class CustomLogin(LoginView):
   template_name = 'login.html'
   fields = '__all__'
   redirect_authenticated_user = True

   def get_success_url(self):
       return reverse_lazy('tasks')
    
    
           

class TaskList(LoginRequiredMixin,ListView):
    model = TaskModel
    context_object_name = 'tasklist'
    template_name = 'task_list.html'
    
    def get_context_data(self,**kwargs):
        context = super().get_context_data(**kwargs)
        context['tasklist'] = context['tasklist'].filter(User=self.request.user)
        context['count'] = context['tasklist'].filter(complete = False).count()
        return context
         
    


class TaskDetail(LoginRequiredMixin,DetailView):
    model = TaskModel
    template_name = 'task_detail.html'
    context_object_name = 'detail'

class CreateTask(LoginRequiredMixin,CreateView):
    model = TaskModel
    fields = ['title','description','complete']
    template_name = 'task_create.html'
    success_url = reverse_lazy('tasks')

class UpdateTask(LoginRequiredMixin,UpdateView):
    model = TaskModel
    fields = ['title','description','complete']
    template_name = 'task_create.html'
    success_url = reverse_lazy('tasks')

class DeleteTask(LoginRequiredMixin,DeleteView):
    model = TaskModel
    template_name = 'task_delete.html'
    context_object_name = 'task'
    success_url = reverse_lazy('tasks ')