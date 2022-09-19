from django.contrib import admin
from projects.models import Project


class ProjectAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'author', 'create_time', 'public')
    list_display_links = ('id', 'author')
    search_fields = ('author', 'name', 'id')
    list_filter = ('author',)
    prepopulated_fields = {'slug': ('name',)}


admin.site.register(Project, ProjectAdmin)