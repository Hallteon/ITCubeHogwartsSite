from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, DetailView
from slugify import slugify

from articles.models import Category, Tag
from projects.forms import AddProjectForm
from projects.models import Project
from utils.utils import DataMixin


class AddProject(CreateView):
    form_class = AddProjectForm
    template_name = 'projects/add_project.html'
    success_url = reverse_lazy('projects')

    def form_valid(self, form):
        self.obj = form.save(commit=False)
        self.obj.author = self.request.user
        self.obj.slug = slugify(self.obj.name)
        self.obj.save()

        self.obj.members.add(self.request.user)
        self.obj.save()

        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Добавить проект'

        return context


class ShowProjects(ListView):
    model = Project
    template_name = 'projects/projects.html'
    context_object_name = 'projects'

    def get_queryset(self):
        return Project.objects.filter(public=True).order_by('-create_time')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Проекты'
        context['categories'] = Category.objects.all()
        context['tags'] = Tag.objects.all()

        return context


class ShowProject(LoginRequiredMixin, DataMixin, DetailView):
    model = Project
    template_name = 'projects/project.html'
    slug_url_kwarg = 'project_slug'
    context_object_name = 'project'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = context['project']

        return context