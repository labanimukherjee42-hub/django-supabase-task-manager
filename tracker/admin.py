from django.contrib import admin


from .models import Project, Tasks # Replace with your actual table names

admin.site.register(Project)
admin.site.register(Tasks)
