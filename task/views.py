from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import (ListView,
                                  CreateView,
                                  DetailView,
                                  DeleteView,
                                  UpdateView)

from .models import Task


# Create your views here.

class TaskListView(ListView):
    model = Task
    template_name = 'task/home.html'
    context_object_name = 'tasks'  # this will be sended to the template : context =tasks

    # we try to filter what user see ,
    # user can see only his created tasks
    def get_queryset(self):
        user = self.request.user
        if user.is_authenticated:
            return Task.objects.filter(user=user)  # filtering the tasks
        else:
            return Task.objects.none()  # here if is no user login , no tasks to display : tasks are empty


class TaskDetailView(DetailView):
    model = Task


# UserPassesTestMixin is required for the function test_func , that test the authorization of user to do specific task

class TaskDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Task
    success_url = '/'

    def test_func(self):
        task = self.get_object()
        if self.request.user == task.user:
            return True
        return False


# by convention task create and task update share the same template task_form.html since both needs form and has same fields
class TaskCreateView(LoginRequiredMixin, CreateView):
    model = Task
    fields = ['title', 'details', 'deadline']

    # after creation , we should redirect it to any place,otherwise it through error
    # its redirected to details of the created task ,in models.py by method:    def get_absolute_url(self):
    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form) # super.form_valid  redirect to a a succuss url


class TaskUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Task
    fields = ['title', 'details', 'deadline']

    # the function below will be called when form data is valid and ready to be proccessed

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(
            form)  # This line calls the form_valid method of the parent clas and save the form data to the database.

    def test_func(self):
        task = self.get_object()
        if self.request.user == task.user:
            return True
        return False
