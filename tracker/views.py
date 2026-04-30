from django.shortcuts import render, get_object_or_404
from .models import Project, Tasks # Use the plural names you found!

def dashboard(request):
    # Fetch all records from Supabase
    all_projects = Project.objects.all()
    
    context = {
        'projects': all_projects
    }
    return render(request, 'tracker/dashboard.html', context)
def project_detail(request, pk):
    # pk is the primary key (id) of the project
    project = get_object_or_404(Project, pk=pk)
    
    # Filter tasks that belong to this specific project
    # Note: Ensure 'project' matches the field name in your Tasks model
    tasks = Tasks.objects.filter(project=project)
    
    return render(request, 'tracker/project_detail.html', {
        'project': project,
        'tasks': tasks
    })    