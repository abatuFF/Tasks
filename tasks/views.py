from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView
from .models import Task, Category
from .forms import TaskForm
from django import forms
from django.db.models import Q


def index(request):
    return render(request, 'index.html')


class TaskFilterForm(forms.Form):
    category = forms.ModelChoiceField(queryset=Category.objects.all(), required=False)
    search = forms.CharField(max_length=100, required=False)


class TaskListView(ListView):
    model = Task
    template_name = 'tasks/task_list.html'
    context_object_name = 'tasks'
    form_class = TaskFilterForm

    def get_queryset(self):
        queryset = Task.objects.all()
        form = self.get_form()

        if form.is_valid():
            category = form.cleaned_data.get('category')
            search = form.cleaned_data.get('search')

            if category:
                queryset = queryset.filter(category=category)
            if search:
                queryset = queryset.filter(Q(title__icontains=search))

        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = self.get_form()
        return context


class TaskDetailView(DetailView):
    model = Task
    template_name = 'tasks/task_detail.html'
    context_object_name = 'task'


class TaskCreateView(CreateView):
    model = Task
    form_class = TaskForm
    template_name = 'tasks/task_form.html'
    success_url = '/tasks/'
